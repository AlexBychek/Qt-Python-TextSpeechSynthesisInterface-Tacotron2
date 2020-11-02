import os
import numpy as np
import torch
from hparams import create_hparams
from text import text_to_sequence
from model import Tacotron2
from scipy.io.wavfile import write

class Synthesis:
	def __init__(self):

		self.currentAudioParameters = 1
		self.AudioParameters = [[32768.0, 16000, 743, 186, 743, 80, 0.0, 8000.0],
								[32768.0, 22050, 1024, 256, 1024, 80, 0.0, 8000.0],
								[32768.0, 44100, 2048, 512, 2048, 80, 0.0, 8000.0]]

	def SetCurrentAudioParameters(self, i):
		self.currentAudioParameters = i

	def GetAuidoParameters(self):
		return self.AudioParameters[self.currentAudioParameters]

	def T2LoadModel(self, T2Model, Cleaners):
		if os.path.isfile(T2Model):

			ExperimentDataParameters = [ 500, 500, True, False, False, "", "", Cleaners]
			EncoderDecoderParameters = [ 5, 3, 512, 1024, 256, 1000, 0.5, 0.1, 0.1 ]
			AttentionLocationLayerParameters = [ 1024, 128, 32, 31 ]
			MelProcessingNetworkNarameters = [ 512, 5, 5 ]
			OptimizationHyperparameters = [ False, True, 1 * pow(10, -3), 1 * pow(10, -6), 8 ]

			hparams  =  create_hparams(ExperimentDataParameters,
                   self.AudioParameters[self.currentAudioParameters],
                   EncoderDecoderParameters,
                   AttentionLocationLayerParameters,
                   MelProcessingNetworkNarameters,
                   OptimizationHyperparameters)

			self.Cleaners = Cleaners

			self.model = Tacotron2(hparams).cuda()
			self.model.load_state_dict(torch.load(T2Model)['state_dict'])
			self._ = self.model.cuda().eval().half()

	def WGLoadModel(self, WGModel):
		if os.path.isfile(WGModel):
			self._waveglow = torch.load(WGModel)['model']
			self._waveglow.cuda().eval().half()
			for k in self._waveglow.convinv:
				k.float()

	def SyntethisFunc(self, Text, SampleRate, bool):
		sequence = np.array(text_to_sequence(Text, [self.Cleaners]))[None, :]
		sequence = torch.autograd.Variable(torch.from_numpy(sequence)).cuda().long()
		mel_outputs, mel_outputs_postnet, self._, alignments = self.model.inference(sequence)

		if bool :
			with torch.no_grad():
				add = 32768.0 * self._waveglow.infer(mel_outputs_postnet, sigma=0.666)
				self.add = np.concatenate((self.add, add[0].data.cpu().numpy()), axis=0)

			self.SaveFile("TempFile/test.wav", SampleRate, add=1)
		else:
			with torch.no_grad():
				self.audio = 32768.0*self._waveglow.infer(mel_outputs_postnet, sigma=0.666)

			self.add = self.audio[0].data.cpu().numpy()

			self.SaveFile("TempFile/test.wav", SampleRate)

		return [mel_outputs.float().data.cpu().numpy()[0], mel_outputs_postnet.float().data.cpu().numpy()[0],
				alignments.float().data.cpu().numpy()[0].T]

	def SaveFile(self, file_name, SampleRate, add=0):
		if add == 1 :
			write(file_name, SampleRate, self.add.astype('int16'))
		else:
			write(file_name, SampleRate, self.audio[0].data.cpu().numpy().astype('int16'))