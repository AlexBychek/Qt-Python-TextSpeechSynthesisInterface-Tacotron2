import os
import time
from PyQt5 import QtCore
import torch
from torch.utils.data.distributed import DistributedSampler
from torch.utils.data import DataLoader
from model import Tacotron2
from data_utils import TextMelLoader, TextMelCollate
from loss_function import Tacotron2Loss
from logger import Tacotron2Logger
class Train(QtCore.QObject):
    log_signal = QtCore.pyqtSignal(object)

    def b_train(self, bool):
        self.check_train = True

    def prepare_dataloaders(self, hparams):
        trainset = TextMelLoader(hparams.training_files, hparams)
        valset = TextMelLoader(hparams.validation_files, hparams)
        collate_fn = TextMelCollate(hparams.n_frames_per_step)

        train_sampler = None
        shuffle = True

        train_loader = DataLoader(trainset, num_workers=1, shuffle=shuffle,
                                  sampler=train_sampler,
                                  batch_size=hparams.batch_size, pin_memory=False,
                                  drop_last=True, collate_fn=collate_fn)
        return train_loader, valset, collate_fn

    def dir_and_log(self, output_directory, log_directory, rank):
        if rank == 0:
            if not os.path.isdir(output_directory):
                os.makedirs(output_directory)
                os.chmod(output_directory, 0o775)
            logger = Tacotron2Logger(os.path.join(output_directory, log_directory))
        else:
            logger = None
        return logger

    def load_model(self, hparams):
        model = Tacotron2(hparams).cuda()
        return model

    def warm_start_model(self, checkpoint_path, model, ignore_layers):
        assert os.path.isfile(checkpoint_path)
        self.log_signal.emit("Warm starting model from checkpoint '{}]'\n".format(checkpoint_path))

        checkpoint_dict = torch.load(checkpoint_path, map_location='cpu')
        model_dict = checkpoint_dict['state_dict']
        if len(ignore_layers) > 0:
            model_dict = {k: v for k, v in model_dict.items()
                          if k not in ignore_layers}
            dummy_dict = model.state_dict()
            dummy_dict.update(model_dict)
            model_dict = dummy_dict
        model.load_state_dict(model_dict)
        return model

    def load_checkpoint(self, checkpoint_path, model, optimizer):
        assert os.path.isfile(checkpoint_path)
        self.log_signal.emit("Loading checkpoint '{}'\n".format(checkpoint_path))
        checkpoint_dict = torch.load(checkpoint_path, map_location='cpu')
        model.load_state_dict(checkpoint_dict['state_dict'])
        optimizer.load_state_dict(checkpoint_dict['optimizer'])
        learning_rate = checkpoint_dict['learning_rate']
        iteration = checkpoint_dict['iteration']

        self.log_signal.emit("Loaded checkpoint '{}' from iteration {}\n".format(
            checkpoint_path, iteration))
        return model, optimizer, learning_rate, iteration

    def save_checkpoint(self, model, optimizer, learning_rate, iteration, filepath):
        self.log_signal.emit("Saving model and optimizer state at iteration {} to {}\n".format(
            iteration, filepath))

        torch.save({'iteration': iteration,
                    'state_dict': model.state_dict(),
                    'optimizer': optimizer.state_dict(),
                    'learning_rate': learning_rate}, filepath)

    def validate(self, model, criterion, valset, iteration, batch_size, n_gpus,
                 collate_fn, logger, distributed_run, rank):
        """Handles all the validation scoring and printing"""
        model.eval()
        with torch.no_grad():
            val_sampler = DistributedSampler(valset) if distributed_run else None
            val_loader = DataLoader(valset, sampler=val_sampler, num_workers=1,
                                    shuffle=False, batch_size=batch_size,
                                    pin_memory=False, collate_fn=collate_fn)

            val_loss = 0.0
            for i, batch in enumerate(val_loader):
                x, y = model.parse_batch(batch)
                y_pred = model(x)
                loss = criterion(y_pred, y)
                reduced_val_loss = loss.item()
                val_loss += reduced_val_loss
            val_loss = val_loss / (i + 1)

        model.train()
        if rank == 0:
            self.log_signal.emit("Validation loss {}: {:9f}  \n".format(iteration, val_loss))
            logger.log_validation(val_loss, model, y, y_pred, iteration)

    def train(self, output_directory, log_directory, checkpoint_path, warm_start, n_gpus,
              rank, group_name, hparams):

        self.check_train = False
        self.break_train = False


        torch.manual_seed(hparams.seed)
        torch.cuda.manual_seed(hparams.seed)

        model = self.load_model(hparams)
        learning_rate = hparams.learning_rate
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate,
                                     weight_decay=hparams.weight_decay)

        criterion = Tacotron2Loss()

        logger =  self.dir_and_log(
            output_directory, log_directory, rank)

        train_loader, valset, collate_fn =  self.prepare_dataloaders(hparams)

        iteration = 0
        epoch_offset = 0
        if checkpoint_path is not None:
            if warm_start:
                model =  self.warm_start_model(
                    checkpoint_path, model, hparams.ignore_layers)
            else:
                model, optimizer, _learning_rate, iteration =  self.load_checkpoint(
                    checkpoint_path, model, optimizer)
                if hparams.use_saved_learning_rate:
                    learning_rate = _learning_rate
                iteration += 1  # next iteration is iteration + 1
                epoch_offset = max(0, int(iteration / len(train_loader)))

        model.train()
        is_overflow = False

        for epoch in range(epoch_offset, hparams.epochs):
            if self.break_train == True:
                break

            self.log_signal.emit("Epoch: {}\n".format(epoch))

            for i, batch in enumerate(train_loader):
                start = time.perf_counter()
                for param_group in optimizer.param_groups:
                    param_group['lr'] = learning_rate

                model.zero_grad()
                x, y = model.parse_batch(batch)
                y_pred = model(x)

                loss = criterion(y_pred, y)

                reduced_loss = loss.item()

                loss.backward()

                grad_norm = torch.nn.utils.clip_grad_norm_(
                    model.parameters(), hparams.grad_clip_thresh)

                optimizer.step()

                if self.check_train == True:
                    self.break_train = True
                    break

                if not is_overflow and rank == 0:
                    duration = time.perf_counter() - start
                    self.log_signal.emit("Train loss {} {:.6f} Grad Norm {:.6f} {:.2f}s/it\n".format(
                        iteration, reduced_loss, grad_norm, duration))

                    logger.log_training(
                        reduced_loss, grad_norm, learning_rate, duration, iteration)

                if not is_overflow and (iteration % hparams.iters_per_checkpoint == 0):
                    self.validate(model, criterion, valset, iteration,
                             hparams.batch_size, n_gpus, collate_fn, logger,
                             hparams.distributed_run, rank)
                    if rank == 0:
                        checkpoint_path = os.path.join(
                            output_directory, "checkpoint_{}".format(iteration))
                        self.save_checkpoint(model, optimizer, learning_rate, iteration,
                                        checkpoint_path)

                iteration += 1