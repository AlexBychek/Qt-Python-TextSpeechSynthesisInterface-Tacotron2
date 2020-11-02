from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import wave
import sys

class Canvas(FigureCanvas):
	def __init__(self, fig=Figure(figsize=(16, 4)), parent = None):
		self.fig = fig
		self.fig.patch.set_facecolor((49/255,54/255,59/255))


		FigureCanvas.__init__(self, self.fig)
		FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding,
								   QtWidgets.QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

	def update_g(self, data):
		self.fig.clf()
		self.fig.subplots(1, len(data))
		for i in range(len(data)):
			self.fig.axes[i].imshow(data[i], aspect='auto', origin='bottom', interpolation='none')
			self.fig.axes[i].spines['bottom'].set_color('#ffffff')
			self.fig.axes[i].spines['top'].set_color('#ffffff')
			self.fig.axes[i].spines['right'].set_color('#ffffff')
			self.fig.axes[i].spines['left'].set_color('#ffffff')
			self.fig.axes[i].tick_params(axis='x', colors='white')
			self.fig.axes[i].tick_params(axis='y', colors='white')
			self.fig.axes[i].yaxis.label.set_color('white')
			self.fig.axes[i].xaxis.label.set_color('white')
			self.fig.axes[i].title.set_color('white')

		self.draw_idle()

		FigureCanvas.updateGeometry(self)

class Canvas_spectr(FigureCanvas): # Холст для рисования
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		self.fig = Figure(figsize=(width, height), dpi=dpi)
		self.fig.patch.set_facecolor('black')
		self.axes = self.fig.add_subplot(111)
		super(Canvas_spectr, self).__init__(self.fig)
		self.axes.get_xaxis().set_ticklabels([])
		self.axes.get_yaxis().set_ticklabels([])
		self.axes.axis('off')

	def print_spec(self, file):
		self.axes.cla()
		self.axes.get_xaxis().set_ticklabels([])
		self.axes.get_yaxis().set_ticklabels([])
		self.axes.axis('off')
		spf = wave.open(file, "r")

		signal = spf.readframes(-1)
		signal = np.fromstring(signal, "Int16")
		fs = spf.getframerate()

		if spf.getnchannels() == 2:
			print("Just mono files")
			sys.exit(0)

		Time = np.linspace(0, len(signal) / fs, num=len(signal))
		self.fig.subplots_adjust(left=-0.0, bottom=0.0, right=1, top=1)
		self.axes.plot(Time, signal)
		self.draw_idle()
		FigureCanvas.updateGeometry(self)

