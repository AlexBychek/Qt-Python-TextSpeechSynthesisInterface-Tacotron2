from PyQt5 import QtCore, QtMultimedia

class AudioPlayer(QtMultimedia.QMediaPlayer):
    def set_file(self, file):
        self.fullpath = QtCore.QDir.current().absoluteFilePath(file)
        self.url = QtCore.QUrl.fromLocalFile(self.fullpath)
        self.content = QtMultimedia.QMediaContent(self.url)
        self.setMedia(self.content)
        self.setNotifyInterval(100)

    def _stop(self):
        self.stop()
        self.setMedia(QtMultimedia.QMediaContent())

    def set_voulume(self, volume):
        self.setVolume(volume)

