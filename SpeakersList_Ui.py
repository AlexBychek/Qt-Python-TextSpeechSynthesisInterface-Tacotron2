# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speakerslist.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListSpeakers(object):
    def setupUi(self, ListSpeakers):
        ListSpeakers.setObjectName("ListSpeakers")
        ListSpeakers.resize(666, 89)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ListSpeakers.sizePolicy().hasHeightForWidth())
        ListSpeakers.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(ListSpeakers)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(ListSpeakers)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 646, 69))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SpeakersList = QtWidgets.QHBoxLayout()
        self.SpeakersList.setSpacing(6)
        self.SpeakersList.setObjectName("SpeakersList")
        self.gridLayout_2.addLayout(self.SpeakersList, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(ListSpeakers)
        QtCore.QMetaObject.connectSlotsByName(ListSpeakers)

    def retranslateUi(self, ListSpeakers):
        _translate = QtCore.QCoreApplication.translate
        ListSpeakers.setWindowTitle(_translate("ListSpeakers", "SpeakerList"))
