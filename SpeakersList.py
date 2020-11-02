import SpeakersList_Ui
import SpeakerSetting_Ui
from PyQt5 import  QtCore, QtWidgets, QtGui
from Serialization import Serializ
import os

class AddSpeaker(QtWidgets.QWidget, SpeakerSetting_Ui.Ui_ModelSetting):
    push_data = QtCore.pyqtSignal('QString','QString','QString','QString')
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.CloseWindow.clicked.connect(self.push_d)
        self.GenderModel.currentIndexChanged.connect(self.chang)
        self.LoadModel.clicked.connect(self.modelload)
        self.man = QtGui.QImage()
        self.man.load("Resorce/Man_white.png")
        self.man.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.woman = QtGui.QImage()
        self.woman.load("Resorce/woman_white.png")
        self.woman.scaled(250,250,QtCore.Qt.KeepAspectRatio)
        self.ImageSpeaker.setPixmap(QtGui.QPixmap.fromImage(self.man))
    def closeEvent(self, QCloseEvent):
        self.push_data.emit(self.NameModel.text(),
                            self.GenderModel.currentText(),
                            self.CleanersModel.currentText(),
                            self.ModelPath.text())

    def push_d(self):
        self.push_data.emit(self.NameModel.text(),
                            self.GenderModel.currentText(),
                            self.CleanersModel.currentText(),
                            self.ModelPath.text())
        self.close()

    def chang(self, i):
        if i == 0:
            self.ImageSpeaker.setPixmap(QtGui.QPixmap.fromImage(self.man))
        else:
            self.ImageSpeaker.setPixmap(QtGui.QPixmap.fromImage(self.woman))

    def modelload(self):
        text = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл модели/контрольной нейронной сети")[0]
        self.ModelPath.setText(text)

class Speakr(QtWidgets.QRadioButton):
    get_model_path = QtCore.pyqtSignal('QString', 'QString')
    signal_save_speaker = QtCore.pyqtSignal()
    signal_on_delete = QtCore.pyqtSignal('int')
    def __init__(self, setting=1):
        super().__init__()
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        self.menu = QtWidgets.QMenu(self)
        edit = self.menu.addAction("Edit")
        edit.triggered.connect(lambda: self.SpeakerSetting.show())
        delete = self.menu.addAction("Delete")
        delete.triggered.connect(self.selfdel)
        self.index_button = 0
        self.SpeakerSetting = AddSpeaker()
        self.SpeakerSetting.push_data.connect(self.ParametrSet)
        self.toggled.connect(self.trow)
        if setting == 1:
            self.SpeakerSetting.show()

    def setindex(self, i):
        self.index_button = i

    def selfdel(self):
        self.signal_on_delete.emit(self.index_button)

    def show_context_menu(self, point):
        self.menu.exec(self.mapToGlobal(point))

    def ParametrSet(self, name, Gender, Cleaners, Model):
        self.name = name
        self.gender = Gender
        self.cleaners = Cleaners
        self.model_path = Model
        self.setToolTip("{0}\n{1}\n{2}\n{3}".format(name, Gender, Cleaners, Model))

        if (Gender == "Man"):
            self.setStyleSheet("QRadioButton{ border:0; }"
                "QRadioButton::indicator::unchecked  {image: url(Resorce/Man_white.png);  width: 50px; height: 50px;}"
                "QRadioButton::indicator::checked  {image: url(Resorce/ManC.png);  width: 50px; height: 50px;}");
        else:
            self.setStyleSheet("QRadioButton{ border:0; }"
                "QRadioButton::indicator::unchecked  {border:0;  image: url(Resorce/woman_white.png); width: 50px; height: 50px;}"
                "QRadioButton::indicator::checked  {border:0; image: url(Resorce/womanC.png);  width: 50px; height: 50px;}");

        if self.isChecked():
            self.get_model_path.emit(self.model_path, self.cleaners)
        self.repaint()
        self.signal_save_speaker.emit()
    def trow(self):
        self.get_model_path.emit(self.model_path, self.cleaners)
        self.signal_save_speaker.emit()

class SpeakerList(QtWidgets.QWidget, SpeakersList_Ui.Ui_ListSpeakers):
    set_model = QtCore.pyqtSignal('QString', 'QString')
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.list = []
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        self.menu = QtWidgets.QMenu(self)
        Add = self.menu.addAction("Add")
        Add.triggered.connect(self.add_speaker)

    def show_context_menu(self, point):
        self.menu.exec(self.mapToGlobal(point))

    def add_speaker(self):
        self.speaker = Speakr(setting=1)
        self.speaker.get_model_path.connect(self.get_model)
        self.speaker.signal_save_speaker.connect(self.save_data)
        self.speaker.signal_on_delete.connect(self.delete_speaker)
        self.speaker.setindex(len(self.list))
        self.list.insert(len(self.list), self.speaker)
        self.SpeakersList.addWidget(self.speaker, 0, QtCore.Qt.AlignCenter)
        print("ok")

    def delete_speaker(self, i):
        self.SpeakersList.removeWidget(self.list[i])
        self.list[i].deleteLater()
        self.list[i] = None
        self.list.pop(i)
        self.save_data()
        for i in range(0, len(self.list)):
            self.list[i].setindex(i)

    def get_model(self, model, cleaners):
        self.set_model.emit(model,cleaners)

    def save_data(self):
        self.repaint()
        speaker_list_save = []
        for i in range(0, len(self.list)):
            speaker_list_save.append([self.list[i].name,
                                      self.list[i].gender,
                                      self.list[i].cleaners,
                                      self.list[i].model_path,
                                      self.list[i].isChecked()
                                      ])

        Serializ.dump("speakers_list.txt", speaker_list_save)

    def load_data(self):
        if os.path.isfile("speakers_list.txt"):
            speaker_list_load = Serializ.load("speakers_list.txt")
            for i in range(0, len(speaker_list_load)):
                self.speaker = Speakr(setting=0)
                self.speaker.get_model_path.connect(self.get_model)
                self.speaker.ParametrSet(speaker_list_load[i][0], speaker_list_load[i][1], speaker_list_load[i][2], speaker_list_load[i][3])
                self.speaker.signal_save_speaker.connect(self.save_data)
                self.speaker.signal_on_delete.connect(self.delete_speaker)
                self.speaker.setindex(i)
                self.list.insert(len(self.list), self.speaker)
                self.SpeakersList.addWidget(self.speaker, 0, QtCore.Qt.AlignCenter)
                if speaker_list_load[i][4] == True:
                    self.speaker.setChecked(True)