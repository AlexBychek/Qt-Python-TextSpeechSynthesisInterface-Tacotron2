import tensorflow as tf
from text import symbols


def create_hparams(ExperimentDataParameters,
                   AudioParameters,
                   EncoderDecoderParameters,
                   AttentionLocationLayerParameters,
                   MelProcessingNetworkNarameters,
                   OptimizationHyperparameters,
                   hparams_string=None, verbose=False):

    """Create model hyperparameters. Parse nondefault from given string."""
    hparams = tf.contrib.training.HParams(
        ################################
        # Experiment Parameters        #
        ################################
        epochs=ExperimentDataParameters[0],
        iters_per_checkpoint=ExperimentDataParameters[1],
        seed=1234,
        dynamic_loss_scaling=True,
        fp16_run=False,
        distributed_run=False,
        dist_backend="nccl",
        dist_url="tcp://localhost:54321",
        cudnn_enabled=ExperimentDataParameters[2],
        cudnn_benchmark=ExperimentDataParameters[3],
        ignore_layers=['embedding.weight'],

        ################################
        # Data Parameters             #
        ################################
        load_mel_from_disk=ExperimentDataParameters[4],
        training_files=ExperimentDataParameters[5],
        validation_files= ExperimentDataParameters[6],
        text_cleaners=[ExperimentDataParameters[7]],

        ################################
        # Audio Parameters             #
        ################################
        max_wav_value=AudioParameters[0],
        sampling_rate=AudioParameters[1],
        filter_length=AudioParameters[2],
        hop_length=AudioParameters[3],
        win_length=AudioParameters[4],
        n_mel_channels=AudioParameters[5],
        mel_fmin=AudioParameters[6],
        mel_fmax=AudioParameters[7],

        ################################
        # Model Parameters             #
        ################################
        n_symbols=len(symbols),
        symbols_embedding_dim=512,

        # Encoder parameters
        encoder_kernel_size=EncoderDecoderParameters[0],
        encoder_n_convolutions=EncoderDecoderParameters[1],
        encoder_embedding_dim=EncoderDecoderParameters[2],

        # Decoder parameters
        n_frames_per_step=1,  # currently only 1 is supported
        decoder_rnn_dim=EncoderDecoderParameters[3],
        prenet_dim=EncoderDecoderParameters[4],
        max_decoder_steps=EncoderDecoderParameters[5],
        gate_threshold=EncoderDecoderParameters[6],
        p_attention_dropout=EncoderDecoderParameters[7],
        p_decoder_dropout=EncoderDecoderParameters[8],

        # Attention parameters
        attention_rnn_dim=AttentionLocationLayerParameters[0],
        attention_dim=AttentionLocationLayerParameters[1],

        # Location Layer parameters
        attention_location_n_filters=AttentionLocationLayerParameters[2],
        attention_location_kernel_size=AttentionLocationLayerParameters[3],

        # Mel-post processing network parameters
        postnet_embedding_dim=MelProcessingNetworkNarameters[0],
        postnet_kernel_size=MelProcessingNetworkNarameters[1],
        postnet_n_convolutions=MelProcessingNetworkNarameters[2],

        ################################
        # Optimization Hyperparameters #
        ################################
        use_saved_learning_rate=OptimizationHyperparameters[0],
        learning_rate=1 * pow(10, -OptimizationHyperparameters[2]),
        weight_decay=1 * pow(10, -OptimizationHyperparameters[3]),
        grad_clip_thresh=1.0,
        batch_size=OptimizationHyperparameters[4],
        mask_padding=OptimizationHyperparameters[1]  # set model's padded outputs to padded values
    )

    if hparams_string:
        tf.logging.info('Parsing command line hparams: %s', hparams_string)
        hparams.parse(hparams_string)

    if verbose:
        tf.logging.info('Final parsed hparams: %s', hparams.values())

    return hparams
