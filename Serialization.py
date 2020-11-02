import yaml
from PyQt5 import QtCore

class Serializ:
    @staticmethod
    def load(file_name):
        train_read = QtCore.QFile(file_name)
        if train_read.exists():
            train_read.open(QtCore.QFile.ReadWrite | QtCore.QFile.Text)
            load = QtCore.QTextStream(train_read)
            temp = load.readAll()
            train_read.close()
            return yaml.load(temp)
        else:
            return False
    @staticmethod
    def dump(file_name, param):
        start_param = yaml.dump(param)
        train_read = QtCore.QFile(file_name)
        train_read.open(QtCore.QFile.WriteOnly | QtCore.QFile.Text)
        load = QtCore.QTextStream(train_read)
        load << start_param
        train_read.close()