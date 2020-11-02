import sys
import os
from PyQt5 import QtWidgets, QtCore, QtMultimedia, QtGui
from QDoubleSlider import DoubleSlider
import interface
sys.path.append('waveglow/')
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from Serialization import Serializ
from hparams import create_hparams
from Canvas import Canvas, Canvas_spectr
from Synthesis import Synthesis
from AudioPlayer import AudioPlayer
from Training import  Train
from threading import Thread
from SpeakersList import SpeakerList
class MainInterface(QtWidgets.QMainWindow, interface.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.text_to_speach_list = [ self.Text_to_Speech, self.Text_to_Speech_2, self.Text_to_Speech_3, self.Text_to_Speech_4 ]
		self.canvas = Canvas()
		self.canvas_comp = QtWidgets.QVBoxLayout(self.Mel_spec)
		self.canvas_comp.addWidget(self.canvas)
		self.toolbar = NavigationToolbar(self.canvas, self)
		self.canvas_comp.addWidget(self.toolbar)
		self.canvas1 = Canvas_spectr(self, width=21, height=4)
		self.Spectrum.setStyleSheet(" background-color: none; selection-background-color: none;")
		self.canvas1.setStyleSheet("background-color: none; selection-background-color: none;")
		self.SpectrAudio = QtWidgets.QStackedLayout(self.Spectrum)
		self.SpectrAudio.insertWidget(0, self.canvas1)
		self._Syntethis = Synthesis()
		self.player = AudioPlayer()
		self.speakerlist = SpeakerList()
		self.speakerlist.setStyleSheet("border: 0; height: 50px;")

		self.speakerlist_layout = QtWidgets.QVBoxLayout(self.SpeakerList)
		self.speakerlist_layout.addWidget(self.speakerlist)
		self.speakerlist.set_model.connect(self._Syntethis.T2LoadModel)
		self.speakerlist.load_data()
		self.LoadWaveGlowModel.clicked.connect(self.WGSelectModel)
		self.Syntethis.clicked.connect(self.SyntethisFunc)
		self.PlayWav.clicked.connect(self.playSpeeck)
		self.output_directory_button.clicked.connect(self._output_directory)
		self.log_directory_button.clicked.connect(self._log_directory)
		self.checkpoint_path_Box.stateChanged.connect(self._path_checkpoint_enabled)
		self.path_checkpoint_button.clicked.connect(self._path_checkpoint)
		self.training_files_button.clicked.connect(self._training_files)
		self.validation_files_button.clicked.connect(self._validation_files)
		self.AudioParametersBox.currentIndexChanged.connect(self._Syntethis.SetCurrentAudioParameters)
		self.AudioParametersBox.currentIndexChanged.connect(self.SetAudioParameters)

		self.StartTrain.clicked.connect(self._start_train)
		self.SaveAudio.clicked.connect(self.saveFile)
		self.Stop.clicked.connect(self._stop_train)
		self.VolumeSlider.valueChanged.connect(self.player.set_voulume)
		self.PauseWav.clicked.connect(self.player.pause)
		self.StopWav.clicked.connect(self.player.stop)
		self.double_slider = DoubleSlider()
		self.double_slider.setOrientation(QtCore.Qt.Horizontal)
		self.SpectrAudio.insertWidget(0, self.double_slider)
		self.SpectrAudio.setStackingMode(self.SpectrAudio.StackAll)
		self.SpectrAudio.setCurrentWidget(self.double_slider)

		self.double_slider.setStyleSheet("QSlider{ border: 0; background-color: none; selection-background-color: none;}"
										 "QSlider::groove:horizontal {border: 1px solid #000000; }"
										 "QSlider::handle:horizontal{ border: 10px solide #5c5c5c;"
										 "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f); }"
										 "  }"
										 "QSlider::add-page:horizontal{ background: rgba(255, 255, 255, 10%);}"
										 "QSlider::sub-page:horizontal{ background: rgba(255,140,0, 40%);}")

		self.player.positionChanged.connect(self.setPosMax)

		self.StartTrain.setToolTip(
			"checkpoint_path + warm_start - если модель уже обученная и начать обучение новой модели \n"
			" только checkpoint_path - не модель обученная модель а точка остановки, продолжит \n "
			"без checkpoint_path и warm_start - модель с нуля \n "
			)

		self.SetAudioParameters()
		self.load_data()


	def SetAudioParameters(self):
		self.max_wav_value.setValue(self._Syntethis.AudioParameters[self._Syntethis.currentAudioParameters][0])
		self.sampling_rate.setValue(self._Syntethis.AudioParameters[self._Syntethis.currentAudioParameters][1])
		self.filter_length.setValue(self._Syntethis.AudioParameters[self._Syntethis.currentAudioParameters][2])
		self.hop_length.setValue(self._Syntethis.AudioParameters[self._Syntethis.currentAudioParameters][3])
		self.win_length.setValue(self._Syntethis.AudioParameters[self._Syntethis.currentAudioParameters][4])
		self.n_mel_channels.setValue(self._Syntethis.AudioParameters[self._Syntethis.currentAudioParameters][5])
		self.mel_fmin.setValue(self._Syntethis.AudioParameters[self._Syntethis.currentAudioParameters][6])
		self.mel_fmax.setValue(self._Syntethis.AudioParameters[self._Syntethis.currentAudioParameters][7])
		self.batch_size.setValue(8)


	def _train_param_load(self):
		if os.path.isfile("train_param.txt"):
			start_param = Serializ.load("train_param.txt")

			self.epoch.setValue(start_param[0][0])
			self.iters_per_checkpoint.setValue(start_param[0][1])
			self.cudnn_enabled.setChecked(start_param[0][2])
			self.cudnn_benchmark.setChecked(start_param[0][3])
			self.load_mel_from_disk.setChecked(start_param[0][4])
			self.training_files.setText(start_param[0][5])
			self.validation_files.setText(start_param[0][6])

			self.encoder_kernel_size.setValue(start_param[1][0])
			self.encoder_n_convolutions.setValue(start_param[1][1])
			self.encoder_embedding_dim.setValue(start_param[1][2])
			self.decoder_rnn_dim.setValue(start_param[1][3])
			self.prenet_dim.setValue(start_param[1][4])
			self.max_decoder_steps.setValue(start_param[1][5])
			self.gate_threshold.setValue(start_param[1][6])
			self.p_attention_dropout.setValue(start_param[1][7])
			self.p_decoder_dropout.setValue(start_param[1][8])

			self.attention_rnn_dim.setValue(start_param[2][0])
			self.attention_dim.setValue(start_param[2][1])
			self.attention_location_n_filters.setValue(start_param[2][2])
			self.attention_location_kernel_size.setValue(start_param[2][3])

			self.postnet_embedding_dim.setValue(start_param[3][0])
			self.postnet_kernel_size.setValue(start_param[3][1])
			self.postnet_n_convolutions.setValue(start_param[3][2])

			self.use_saved_learning_rate.setChecked(start_param[4][0])
			self.mask_padding.setChecked(start_param[4][1])
			self.learning_rate.setValue(start_param[4][2])
			self.weight_decay.setValue(start_param[4][3])
			self.batch_size.setValue(start_param[4][4])

	def _start_train(self):

		ExperimentDataParameters = [
			self.epoch.value(),
			self.iters_per_checkpoint.value(),
			self.cudnn_enabled.isChecked(),
			self.cudnn_benchmark.isChecked(),
			self.load_mel_from_disk.isChecked(),
			self.training_files.text(),
			self.validation_files.text(),
			self.text_cleaners_box.currentText()]

		EncoderDecoderParameters = [
			self.encoder_kernel_size.value(),
			self.encoder_n_convolutions.value(),
			self.encoder_embedding_dim.value(),
			self.decoder_rnn_dim.value(),
			self.prenet_dim.value(),
			self.max_decoder_steps.value(),
			self.gate_threshold.value(),
			self.p_attention_dropout.value(),
			self.p_decoder_dropout.value()
		]

		AttentionLocationLayerParameters = [
			self.attention_rnn_dim.value(),
			self.attention_dim.value(),
			self.attention_location_n_filters.value(),
			self.attention_location_kernel_size.value()
		]

		MelProcessingNetworkNarameters = [
			self.postnet_embedding_dim.value(),
			self.postnet_kernel_size.value(),
			self.postnet_n_convolutions.value()
		]

		OptimizationHyperparameters = [
			self.use_saved_learning_rate.isChecked(),
			self.mask_padding.isChecked(),
			self.learning_rate.value(),
			self.weight_decay.value(),
			self.batch_size.value()
		]

		Serializ.dump("train_param.txt", [ExperimentDataParameters,
			 EncoderDecoderParameters,
			 AttentionLocationLayerParameters,
			 MelProcessingNetworkNarameters,
			 OptimizationHyperparameters])

		hpr =  create_hparams(ExperimentDataParameters,
                   self._Syntethis.AudioParameters[self.AudioParametersBox.currentIndex()],
                   EncoderDecoderParameters,
                   AttentionLocationLayerParameters,
                   MelProcessingNetworkNarameters,
                   OptimizationHyperparameters)

		self._train_param_load()
		self.train = Train()
		self.train.log_signal.connect(self.setLog)

		self.x = Thread(target=self.train.train, args=(self.output_directory.text(),
			  self.log_directory.text(),
			  [None, [None, self.path_checkpoint.text()][os.path.isfile(self.path_checkpoint.text())]][self.checkpoint_path_Box.isChecked()],
			  self.warm_start.isChecked(),
			  False,
			  False,
			  False,
			  hpr,))
		self.logBox.setPlainText("")
		self.x.start()

	def _stop_train(self):
		self.train.check_train = True
		self.x.join()
		self.x._stop()
		self.setLog("train stopped")

	def _output_directory(self):
		self.out_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку вывода модели")
		self.output_directory.setText(self.out_dir)

	def _log_directory(self):
		self.log_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку вывода логов")
		self.log_directory.setText(self.log_dir)

	def _path_checkpoint_enabled(self, state):
		if state == 2:
			self.path_checkpoint.setEnabled(True)
			self.path_checkpoint_button.setEnabled(True)
		else:
			self.path_checkpoint.setEnabled(False)
			self.path_checkpoint_button.setEnabled(False)

	def _path_checkpoint(self):
		self.checkpoint_model = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл модели/контрольной точки от которой продолжить обучение")[0]
		self.path_checkpoint.setText(self.checkpoint_model)

	def _training_files(self):
		self.train_file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл модели/контрольной точки от которой продолжить обучение")[0]
		self.training_files.setText(self.train_file)

	def _validation_files(self):
		self.valid_file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл модели/контрольной точки от которой продолжить обучение")[0]
		self.validation_files.setText(self.valid_file)

	def load_data(self):
		self._train_param_load()
		data_load = Serializ.load("config.txt")
		if data_load != False:
			self._WGModel = data_load[0]
			self._Syntethis.WGLoadModel(self._WGModel)
			self.WaveGlowModel.setText(self._WGModel)

	def WGSelectModel(self):
		self._WGModel = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл модели/контрольной вокодера")[0]
		self._Syntethis.WGLoadModel(self._WGModel)
		self.WaveGlowModel.setText(self._WGModel)
		self.LoadWaveGlowModel.setEnabled(True)

	def SyntethisFunc(self):
		if self.text_to_speach_list[self.tabWidget.currentIndex()].toPlainText() != "":
			model_param = [self._WGModel]
			Serializ.dump("config.txt", model_param)
			self.player._stop()
			self.canvas.update_g(self._Syntethis.SyntethisFunc(self.text_to_speach_list[self.tabWidget.currentIndex()].toPlainText(), int(self.SampleRate.currentText()), self.AddSpeech.isChecked()))
			self.player.set_file('TempFile/test.wav')
			self.canvas1.print_spec('TempFile/test.wav')
			self.canvas_comp.update()
			self.Mel_spec.repaint()
			self.repaint()

	def playSpeeck(self):
		print(self.player.duration())
		self.double_slider.setMaximum(self.player.duration() / 1000)
		self.player.play()

	def saveFile(self):
		file_name = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить речь",'', 'WAV (*.wav)')[0]
		if file_name != "":
			if self.AddSpeech.isChecked() == False:
				self._Syntethis.SaveFile(file_name, int(self.SampleRate.currentText()))
			else:
				self._Syntethis.SaveFile(file_name, int(self.SampleRate.currentText()), add=1)

	def setLog(self, text):
		temp = self.logBox.toPlainText()
		self.logBox.setText(temp + text)
		self.logBox.moveCursor(QtGui.QTextCursor.End)

	def setPosMax(self, MAX):
		self.double_slider.setValue(MAX / 1000)
		print(MAX / 1000)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainInterface()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()