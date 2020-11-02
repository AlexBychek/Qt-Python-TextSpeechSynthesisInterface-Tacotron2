# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 873)
        MainWindow.setMinimumSize(QtCore.QSize(950, 0))
        MainWindow.setMaximumSize(QtCore.QSize(950, 16777215))
        MainWindow.setStyleSheet("QToolTip\n"
"{\n"
"    border: 0.1ex solid #eff0f1;\n"
"    background-color: #31363b;\n"
"    alternate-background-color: #3b4045;\n"
"    color: #eff0f1;\n"
"    padding: 0.5ex;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #31363b;\n"
"    selection-background-color:#3daee9;\n"
"    selection-color: #eff0f1;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    border: 0px transparent black;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #3daee9;\n"
"}\n"
"\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 0.2ex;\n"
"}\n"
"\n"
"\n"
"QGroupBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"    border: none;\n"
"    border-image: url(:/dark/checkbox_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    border-image: url(:/dark/checkbox_checked.svg);\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"    border: none;\n"
"    border-image: url(:/dark/checkbox_checked.svg);\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    border-image: url(:/dark/checkbox_checked_disabled.svg);\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    border-image: url(:/dark/checkbox_unchecked_disabled.svg);\n"
"}\n"
"\n"
"#cpu_button,\n"
"#gpu_button\n"
"{\n"
"    spacing: 0.5ex;\n"
"    outline: none;\n"
"    color: #eff0f1;\n"
"    margin-bottom: 0.2ex;\n"
"}\n"
"\n"
"#cpu_button:disabled,\n"
"#gpu_button:disabled\n"
"{\n"
"    color: #76797c;\n"
"}\n"
"\n"
"#cpu_button::indicator:unchecked,\n"
"#cpu_button::indicator:unchecked:focus,\n"
"#gpu_button::indicator:unchecked,\n"
"#gpu_button::indicator:unchecked:focus\n"
"{\n"
"    border-image: url(:/dark/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"\n"
"#cpu_button::indicator:unchecked:hover,\n"
"#cpu_button::indicator:unchecked:pressed,\n"
"#gpu_button::indicator:unchecked:hover,\n"
"#gpu_button::indicator:unchecked:pressed\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    border-image: url(:/dark/radio_unchecked.svg);\n"
"}\n"
"\n"
"\n"
"#cpu_button::indicator:checked,\n"
"#gpu_button::indicator:checked\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    border-image: url(:/dark/radio_checked.svg);\n"
"}\n"
"\n"
"#cpu_button::indicator:checked:hover,\n"
"#cpu_button::indicator:checked:focus,\n"
"#cpu_button::indicator:checked:pressed,\n"
"#gpu_button::indicator:checked:hover,\n"
"#gpu_button::indicator:checked:focus,\n"
"#gpu_button::indicator:checked:pressed\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    border-image: url(:/dark/radio_checked.svg);\n"
"}\n"
"\n"
"#cpu_button::indicator:checked:disabled,\n"
"#gpu_button::indicator:checked:disabled\n"
"{\n"
"    outline: none;\n"
"    border-image: url(:/dark/radio_checked_disabled.svg);\n"
"}\n"
"\n"
"#cpu_button::indicator:unchecked:disabled,\n"
"#gpu_button::indicator:unchecked:disabled\n"
"{\n"
"    border-image: url(:/dark/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #31363b;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    background-color: #3daee9;\n"
"    color: #eff0f1;\n"
"    margin-bottom: -0.1ex;\n"
"    padding-bottom: 0.1ex;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    color: #eff0f1;\n"
"    margin: 0.2ex;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 0.5ex;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 0.5ex 3ex 0.5ex 3ex;\n"
"    margin-left: 0.5ex;\n"
"    border: 0.1ex solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 0.2ex;\n"
"    background: lightblue;\n"
"    margin-left: 1ex;\n"
"    margin-right: 0.5ex;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked\n"
"{\n"
"    border-image: url(:/dark/checkbox_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected\n"
"{\n"
"    border-image: url(:/dark/checkbox_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked\n"
"{\n"
"    border-image: url(:/dark/checkbox_checked.svg);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected\n"
"{\n"
"    border-image: url(:/dark/checkbox_checked.svg);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked\n"
"{\n"
"    border-image: url(:/dark/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected\n"
"{\n"
"    border-image: url(:/dark/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked\n"
"{\n"
"    border-image: url(:/dark/radio_checked.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected\n"
"{\n"
"    border-image: url(:/dark/radio_checked.svg);\n"
"}\n"
"\n"
"QMenu::right-arrow\n"
"{\n"
"    margin: 0.5ex;\n"
"    border-image: url(:/light/right_arrow.svg);\n"
"    width: 0.6ex;\n"
"    height: 0.9ex;\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #454545;\n"
"    background-color: #31363b;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #31363b;\n"
"    color: #eff0f1;\n"
"    border: 0.1ex solid 3A3939;\n"
"    border-radius: 0.2ex;\n"
"}\n"
"\n"
"QWidget:focus,\n"
"QMenuBar:focus\n"
"{\n"
"    border: 0.1ex solid #3daee9;\n"
"}\n"
"\n"
"QTabWidget:focus,\n"
"QCheckBox:focus,\n"
"#cpu_button:focus,\n"
"#gpu_button:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #232629;\n"
"    padding: 0.5ex;\n"
"    border-style: solid;\n"
"    border: 0.1ex solid #76797c;\n"
"    border-radius: 0.2ex;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    border-radius: 0.2ex;\n"
"    padding-top: 1ex;\n"
"    margin-top: 1ex;\n"
"}\n"
"\n"
"QGroupBox::title\n"
"{\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 0.1ex;\n"
"    padding-right: 0.1ex;\n"
"    margin-top: -0.7ex;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 0.2ex;\n"
"    border: 0.1ex solid #76797c;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 1.5ex;\n"
"    margin: 0.3ex 1.5ex 0.3ex 1.5ex;\n"
"    border: 0.1ex transparent #2A2929;\n"
"    border-radius: 0.4ex;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #3daee9;\n"
"    min-width: 0.5ex;\n"
"    border-radius: 0.4ex;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 0.3ex 0px 0.3ex;\n"
"    border-image: url(:/dark/right_arrow_disabled.svg);\n"
"    width: 1ex;\n"
"    height: 1ex;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0ex 0.3ex 0ex 0.3ex;\n"
"    border-image: url(:/dark/left_arrow_disabled.svg);\n"
"    width: 1ex;\n"
"    height: 1ex;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,\n"
"QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark/right_arrow.svg);\n"
"    width: 1ex;\n"
"    height: 1ex;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover,\n"
"QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark/left_arrow.svg);\n"
"    width: 1ex;\n"
"    height: 1ex;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 1.5ex;\n"
"    margin: 1.5ex 0.3ex 1.5ex 0.3ex;\n"
"    border: 0.1ex transparent #2A2929;\n"
"    border-radius: 0.4ex;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #3daee9;\n"
"    min-height: 0.5ex;\n"
"    border-radius: 0.4ex;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 0.3ex 0ex 0.3ex 0ex;\n"
"    border-image: url(:/dark/up_arrow_disabled.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 0.3ex 0ex 0.3ex 0ex;\n"
"    border-image: url(:/dark/down_arrow_disabled.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,\n"
"QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/dark/up_arrow.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/dark/down_arrow.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #232629;\n"
"    color: #eff0f1;\n"
"    border: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #232629;;\n"
"    color: #eff0f1;\n"
"    border-radius: 0.2ex;\n"
"    border: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #76797c;\n"
"    color: #eff0f1;\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QSizeGrip\n"
"{\n"
"    border-image: url(:/dark/sizegrip.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #31363b;\n"
"    color: white;\n"
"    padding-left: 0.4ex;\n"
"    spacing: 0.2ex;\n"
"    border: 0.1ex dashed #76797c;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 0.4ex;\n"
"    border: 0.1ex solid #76797c;\n"
"    spacing: 0.2ex;\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 0.1ex;\n"
"    background-color: #76797c;\n"
"    color: white;\n"
"    padding-left: 0.4ex;\n"
"    margin-left: 1ex;\n"
"    margin-right: 0.5ex;\n"
"}\n"
"\n"
"QFrame[frameShape=\"2\"],  /* QFrame::Panel == 0x0003 */\n"
"QFrame[frameShape=\"3\"],  /* QFrame::WinPanel == 0x0003 */\n"
"QFrame[frameShape=\"4\"],  /* QFrame::HLine == 0x0004 */\n"
"QFrame[frameShape=\"5\"],  /* QFrame::VLine == 0x0005 */\n"
"QFrame[frameShape=\"6\"]  /* QFrame::StyledPanel == 0x0006 */\n"
"{\n"
"    border-width: 0.1ex;\n"
"    padding: 0.1ex;\n"
"    border-style: solid;\n"
"    border-color: #31363b;\n"
"    background-color: #76797c;\n"
"    border-radius: 0.5ex;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    border: 0.1ex transparent black;\n"
"}\n"
"\n"
"QToolBar\n"
"{\n"
"    border: 0.1ex transparent #393838;\n"
"    background: 0.1ex solid #31363b;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal\n"
"{\n"
"    border-image: url(:/dark/hmovetoolbar.svg);\n"
"    width = 1.6ex;\n"
"    height = 6.4ex;\n"
"}\n"
"\n"
"QToolBar::handle:vertical\n"
"{\n"
"    border-image: url(:/dark/vmovetoolbar.svg);\n"
"    width = 5.4ex;\n"
"    height = 1ex;\n"
"}\n"
"\n"
"QToolBar::separator:horizontal\n"
"{\n"
"    border-image: url(:/dark/hsepartoolbar.svg);\n"
"    width = 0.7ex;\n"
"    height = 6.3ex;\n"
"}\n"
"\n"
"QToolBar::separator:vertical\n"
"{\n"
"    border-image: url(:/dark/vsepartoolbars.svg);\n"
"    width = 6.3ex;\n"
"    height = 0.7ex;\n"
"}\n"
"\n"
"#LoadWaveGlowModel,\n"
"#StartTrain,\n"
"#Stop,\n"
"#output_directory_button,\n"
"#log_directory_button,\n"
"#path_checkpoint_button,\n"
"#training_files_button,\n"
"#validation_files_button\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #3b4045, stop: 0.5 #31363b);\n"
"    border-width: 0.1ex;\n"
"    border-color: #76797c;\n"
"    border-style: solid;\n"
"    padding: 0.5ex;\n"
"    border-radius: 0.2ex;\n"
"    outline: none;\n"
"}\n"
"\n"
"#LoadWaveGlowModel:disabled,\n"
"#StartTrain:disabled,\n"
"#Stop:disabled,\n"
"#output_directory_button:disabled,\n"
"#log_directory_button:disabled,\n"
"#path_checkpoint_button:disabled,\n"
"#training_files_button:disabled,\n"
"#validation_files_button:disabled\n"
"{\n"
"    background-color: #31363b;\n"
"    border-width: 0.1ex;\n"
"    border-color: #454545;\n"
"    border-style: solid;\n"
"    padding-top: 0.5ex;\n"
"    padding-bottom: 0.5ex;\n"
"    padding-left: 1ex;\n"
"    padding-right: 1ex;\n"
"    border-radius: 0.2ex;\n"
"    color: #454545;\n"
"}\n"
"\n"
"#LoadWaveGlowModel:focus,\n"
"#StartTrain:focus,\n"
"#Stop:focus,\n"
"#output_directory_button:focus,\n"
"#log_directory_button:focus,\n"
"#path_checkpoint_button:focus,\n"
"#training_files_button:focus,\n"
"#validation_files_button:focus\n"
"{\n"
"    color: white;\n"
"}\n"
"\n"
"#LoadWaveGlowModel:pressed,\n"
"#StartTrain:pressed,\n"
"#Stop:pressed,\n"
"#output_directory_button:pressed,\n"
"#log_directory_button:pressed,\n"
"#path_checkpoint_button:pressed,\n"
"#training_files_button:pressed,\n"
"#validation_files_button:pressed\n"
"{\n"
"    background-color: #31363b;\n"
"    padding-top: -1.5ex;\n"
"    padding-bottom: -1.7ex;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3daee9;\n"
"    border-style: solid;\n"
"    border: 0.1ex solid #76797c;\n"
"    border-radius: 0.2ex;\n"
"    padding: 0.5ex;\n"
"    min-width: 7.5ex;\n"
"}\n"
"\n"
"#LoadWaveGlowModel:checked,\n"
"#StartTrain:checked,\n"
"#Stop:checked,\n"
"#output_directory_button:checked,\n"
"#log_directory_button:checked,\n"
"#path_checkpoint_button:checked,\n"
"#training_files_button:checked,\n"
"#validation_files_button:checked\n"
"{\n"
"    background-color: #76797c;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"#LoadWaveGlowModel:hover,\n"
"#StartTrain:hover,\n"
"#Stop:hover,\n"
"#output_directory_button:hover,\n"
"#log_directory_button:hover,\n"
"#path_checkpoint_button:hover,\n"
"#training_files_button:hover,\n"
"#validation_files_button:hover\n"
"{\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #454a4f, stop: 0.5 #3b4045);\n"
"    border: 0.1ex solid #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"#LoadWaveGlowModel:checked:hover,\n"
"#StartTrain:checked:hover,\n"
"#Stop:checked:hover,\n"
"#output_directory_button:checked:hover,\n"
"#log_directory_button:checked:hover,\n"
"#path_checkpoint_button:checked:hover,\n"
"#training_files_button:checked:hover,\n"
"#validation_files_button:checked:hover\n"
"{\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #808386, stop: 0.5 #76797c);\n"
"    border: 0.1ex solid #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QComboBox:hover,\n"
"QAbstractSpinBox:hover,\n"
"QLineEdit:hover,\n"
"QTextEdit:hover,\n"
"QPlainTextEdit:hover,\n"
"QAbstractView:hover,\n"
"QTreeView:hover\n"
"{\n"
"    border: 0.1ex solid #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QComboBox:hover:pressed,\n"
"#LoadWaveGlowModel:hover:pressed,\n"
"#StartTrain:hover:pressed,\n"
"#Stop:hover:pressed,\n"
"#output_directory_button:hover:pressed,\n"
"#log_directory_button:hover:pressed,\n"
"#path_checkpoint_button:hover:pressed,\n"
"#training_files_button:hover:pressed,\n"
"#validation_files_button:hover:pressed,\n"
"QAbstractSpinBox:hover:pressed,\n"
"QLineEdit:hover:pressed,\n"
"QTextEdit:hover:pressed,\n"
"QPlainTextEdit:hover:pressed,\n"
"QAbstractView:hover:pressed,\n"
"QTreeView:hover:pressed\n"
"{\n"
"    background-color: #31363b;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0.3ex;\n"
"    padding-left: 0.4ex;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #232629;\n"
"    border-radius: 0.2ex;\n"
"    border: 0.1ex solid #76797c;\n"
"    selection-background-color: #3daee9;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 1.5ex;\n"
"\n"
"    border-left-width: 0ex;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 0.3ex;\n"
"    border-bottom-right-radius: 0.3ex;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    border-image: url(:/dark/down_arrow_disabled.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on,\n"
"QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    border-image: url(:/dark/down_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox\n"
"{\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex solid #76797c;\n"
"    background-color: #232629;\n"
"    color: #eff0f1;\n"
"    border-radius: 0.2ex;\n"
"    min-width: 7.5ex;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center left;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,\n"
"QAbstractSpinBox::up-arrow:disabled,\n"
"QAbstractSpinBox::up-arrow:off\n"
"{\n"
"    border-image: url(:/dark/up_arrow_disabled.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    border-image: url(:/dark/up_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow,\n"
"QAbstractSpinBox::down-arrow:disabled,\n"
"QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    border-image: url(:/dark/down_arrow_disabled.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    border-image: url(:/dark/down_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0ex solid black;\n"
"}\n"
"\n"
"/* BORDERS */\n"
"QTabWidget::pane\n"
"{\n"
"    padding: 0.5ex;\n"
"    margin: 0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:top\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    top: -0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:bottom\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    bottom: -0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:left\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    right: -0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:right\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    left: -0.1ex;\n"
"}\n"
"\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 0.5ex; /* move to the right by 0.5ex */\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0ex transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button\n"
"{\n"
"    border-image: url(:/dark/close.svg);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    border-image: url(:/dark/close-hover.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed\n"
"{\n"
"    border-image: url(:/dark/close-pressed.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    border-top: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    min-width: 50px;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:last,\n"
"QTabBar::tab:top:only-one\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    border-right: 0.1ex solid #76797c;\n"
"    border-top: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    min-width: 50px;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:first:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"    border-left: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"\n"
"QTabBar::tab:bottom\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    border-bottom: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-width: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:last,\n"
"QTabBar::tab:bottom:only-one\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    border-right: 0.1ex solid #76797c;\n"
"    border-bottom: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-width: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:first:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"    border-left: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #76797c;\n"
"    border-right: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-height: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:left:last,\n"
"QTabBar::tab:left:only-one\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #76797c;\n"
"    border-bottom: 0.1ex solid #76797c;\n"
"    border-right: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-height: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #76797c;\n"
"    border-top-right-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"    border-top: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"}\n"
"\n"
"#VolumeSlider::groove:horizontal\n"
"{\n"
"    border: 0.1ex solid #31363b;\n"
"    height: 0.4ex;\n"
"    background: #565a5e;\n"
"    margin: 0ex;\n"
"    border-radius: 0.2ex;\n"
"}\n"
"\n"
"#VolumeSlider::handle:horizontal\n"
"{\n"
"    background: #232629;\n"
"    border: 0.1ex solid #626568;\n"
"    width: 1.6ex;\n"
"    height: 1.6ex;\n"
"    margin: -0.8ex 0;\n"
"    border-radius: 0.9ex;\n"
"}\n"
"\n"
"#VolumeSlider::groove:vertical\n"
"{\n"
"    border: 0.1ex solid #31363b;\n"
"    width: 0.4ex;\n"
"    background: #565a5e;\n"
"    margin: 0ex;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"#VolumeSlider::handle:vertical\n"
"{\n"
"    background: #232629;\n"
"    border: 0.1ex solid #626568;\n"
"    width: 1.6ex;\n"
"    height: 1.6ex;\n"
"    margin: 0 -0.8ex;\n"
"    border-radius: 0.9ex;\n"
"}\n"
"\n"
"#VolumeSlider::handle:horizontal:hover,\n"
"#VolumeSlider::handle:horizontal:focus,\n"
"#VolumeSlider::handle:vertical:hover,\n"
"#VolumeSlider::handle:vertical:focus\n"
"{\n"
"    border: 0.1ex solid #3daee9;\n"
"}\n"
"\n"
"#VolumeSlider::sub-page:horizontal,\n"
"#VolumeSlider::add-page:vertical\n"
"{\n"
"    background: #3daee9;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"#VolumeSlider::add-page:horizontal,\n"
"#VolumeSlider::sub-page:vertical\n"
"{\n"
"    background: #626568;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"#LoadWaveGlowModel::menu-indicator,\n"
"#StartTrain::menu-indicator,\n"
"#Stop::menu-indicator,\n"
"#output_directory_button::menu-indicator,\n"
"#log_directory_button::menu-indicator,\n"
"#path_checkpoint_button::menu-indicator,\n"
"#training_files_button::menu-indicator,\n"
"#validation_files_button::menu-indicator\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 0.8ex;\n"
"}\n"
"\n"
"QFrame[height=\"3\"],\n"
"QFrame[width=\"3\"]\n"
"{\n"
"    background-color: #76797c;\n"
"}\n"
"\n"
"QSplitter::handle\n"
"{\n"
"    border: 0.1ex dashed #76797c;\n"
"}\n"
"\n"
"QSplitter::handle:hover\n"
"{\n"
"    background-color: #787876;\n"
"    border: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal\n"
"{\n"
"    width: 0.1ex;\n"
"}\n"
"\n"
"QSplitter::handle:vertical\n"
"{\n"
"    height: 0.1ex;\n"
"}\n"
"\n"
"QSpinBox,\n"
"QDoubleSpinBox\n"
"{\n"
"    padding-right: 1.5ex;\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: right top;\n"
"\n"
"    width: 1.6ex;\n"
"    border-width: 0.1ex;\n"
"}\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow\n"
"{\n"
"    border-image: url(:/dark/up_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:hover,\n"
"QSpinBox::up-arrow:pressed,\n"
"QDoubleSpinBox::up-arrow:hover,\n"
"QDoubleSpinBox::up-arrow:pressed\n"
"{\n"
"    border-image: url(:/dark/up_arrow-hover.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled,\n"
"QSpinBox::up-arrow:off,\n"
"QDoubleSpinBox::up-arrow:disabled,\n"
"QDoubleSpinBox::up-arrow:off\n"
"{\n"
"   border-image: url(:/dark/up_arrow_disabled.svg);\n"
"}\n"
"\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: right bottom;\n"
"\n"
"    width: 1.6ex;\n"
"    border-width: 0.1ex;\n"
"}\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"    border-image: url(:/dark/down_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::down-arrow:hover,\n"
"QSpinBox::down-arrow:pressed,\n"
"QDoubleSpinBox::down-arrow:hover,\n"
"QDoubleSpinBox::down-arrow:pressed\n"
"{\n"
"    border-image: url(:/dark/down_arrow-hover.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::down-arrow:disabled,\n"
"QSpinBox::down-arrow:off,\n"
"QDoubleSpinBox::down-arrow:disabled,\n"
"QDoubleSpinBox::down-arrow:off\n"
"{\n"
"   border-image: url(:/dark/down_arrow_disabled.svg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkpoint_path = QtWidgets.QTabWidget(self.centralwidget)
        self.checkpoint_path.setObjectName("checkpoint_path")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.tabWidget = QtWidgets.QTabWidget(self.tab)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"  border: 1px solid#31363b; \n"
"  padding: 5px;\n"
"} ")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.Text_to_Speech = QtWidgets.QTextEdit(self.tab_3)
        self.Text_to_Speech.setMinimumSize(QtCore.QSize(0, 150))
        self.Text_to_Speech.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Text_to_Speech.setFont(font)
        self.Text_to_Speech.setStyleSheet("border-radius: 5px;")
        self.Text_to_Speech.setObjectName("Text_to_Speech")
        self.gridLayout_14.addWidget(self.Text_to_Speech, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.Text_to_Speech_2 = QtWidgets.QTextEdit(self.tab_4)
        self.Text_to_Speech_2.setMinimumSize(QtCore.QSize(0, 150))
        self.Text_to_Speech_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Text_to_Speech_2.setFont(font)
        self.Text_to_Speech_2.setStyleSheet("border-radius: 5px;")
        self.Text_to_Speech_2.setObjectName("Text_to_Speech_2")
        self.gridLayout_16.addWidget(self.Text_to_Speech_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.Text_to_Speech_3 = QtWidgets.QTextEdit(self.tab_5)
        self.Text_to_Speech_3.setMinimumSize(QtCore.QSize(0, 150))
        self.Text_to_Speech_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Text_to_Speech_3.setFont(font)
        self.Text_to_Speech_3.setStyleSheet("border-radius: 5px;")
        self.Text_to_Speech_3.setObjectName("Text_to_Speech_3")
        self.gridLayout_17.addWidget(self.Text_to_Speech_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.Text_to_Speech_4 = QtWidgets.QTextEdit(self.tab_6)
        self.Text_to_Speech_4.setMinimumSize(QtCore.QSize(0, 150))
        self.Text_to_Speech_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Text_to_Speech_4.setFont(font)
        self.Text_to_Speech_4.setStyleSheet("border-radius: 5px;")
        self.Text_to_Speech_4.setObjectName("Text_to_Speech_4")
        self.gridLayout_18.addWidget(self.Text_to_Speech_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout_15.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.Mel_spec = QtWidgets.QWidget(self.tab)
        self.Mel_spec.setMinimumSize(QtCore.QSize(0, 250))
        self.Mel_spec.setObjectName("Mel_spec")
        self.gridLayout_15.addWidget(self.Mel_spec, 3, 0, 1, 1)
        self.ControlBox = QtWidgets.QGroupBox(self.tab)
        self.ControlBox.setMinimumSize(QtCore.QSize(0, 0))
        self.ControlBox.setMaximumSize(QtCore.QSize(16777215, 150))
        self.ControlBox.setStyleSheet("font: 87 14pt \"Arial\";\n"
"color: black;\n"
"border: 0;")
        self.ControlBox.setObjectName("ControlBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.ControlBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem = QtWidgets.QSpacerItem(35, 25, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 0, 1, 1)
        self.SaveAudio = QtWidgets.QPushButton(self.ControlBox)
        self.SaveAudio.setMinimumSize(QtCore.QSize(25, 25))
        self.SaveAudio.setMaximumSize(QtCore.QSize(35, 25))
        self.SaveAudio.setStyleSheet("QPushButton{\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"color: white;\n"
"font-size: 10px;\n"
"border-image:url(:/icon_pack/Resorce/IconPack1/save_white.png);\n"
"}\n"
"QPushButton:pressed{ \n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"border-image:url(:/icon_pack/Resorce/IconPack1/save_click.png);\n"
"}\n"
"\n"
"")
        self.SaveAudio.setText("")
        self.SaveAudio.setObjectName("SaveAudio")
        self.gridLayout_6.addWidget(self.SaveAudio, 0, 2, 1, 1)
        self.SpeakerList = QtWidgets.QWidget(self.ControlBox)
        self.SpeakerList.setMinimumSize(QtCore.QSize(0, 120))
        self.SpeakerList.setStyleSheet("color: white;\n"
"font-size: 14px;")
        self.SpeakerList.setObjectName("SpeakerList")
        self.gridLayout_6.addWidget(self.SpeakerList, 0, 1, 1, 1)
        self.gridLayout_15.addWidget(self.ControlBox, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 11, 1, 1)
        self.LoadWaveGlowModel = QtWidgets.QPushButton(self.groupBox_3)
        self.LoadWaveGlowModel.setEnabled(True)
        self.LoadWaveGlowModel.setMinimumSize(QtCore.QSize(80, 30))
        self.LoadWaveGlowModel.setMaximumSize(QtCore.QSize(80, 30))
        self.LoadWaveGlowModel.setStyleSheet("border: 1px solid black;")
        self.LoadWaveGlowModel.setObjectName("LoadWaveGlowModel")
        self.gridLayout.addWidget(self.LoadWaveGlowModel, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setMinimumSize(QtCore.QSize(150, 65))
        self.groupBox.setMaximumSize(QtCore.QSize(150, 65))
        self.groupBox.setStyleSheet("background-color: rgb(71,77,82);\n"
"border-radius: 30px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.PlayWav = QtWidgets.QPushButton(self.groupBox)
        self.PlayWav.setMinimumSize(QtCore.QSize(50, 35))
        self.PlayWav.setStyleSheet("QPushButton{\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"border-image:url(:/icon_pack/Resorce/IconPack1/Play_white.png);\n"
"}\n"
"QPushButton:pressed{ \n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"border-image:url(:/icon_pack/Resorce/IconPack1/Play_click.png);\n"
"}\n"
"\n"
"")
        self.PlayWav.setText("")
        self.PlayWav.setObjectName("PlayWav")
        self.gridLayout_10.addWidget(self.PlayWav, 0, 1, 1, 1)
        self.PauseWav = QtWidgets.QPushButton(self.groupBox)
        self.PauseWav.setMinimumSize(QtCore.QSize(25, 25))
        self.PauseWav.setStyleSheet("QPushButton{\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"border-image:url(:/icon_pack/Resorce/IconPack1/Pause_white.png);\n"
"}\n"
"QPushButton:pressed{ \n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"border-image:url(:/icon_pack/Resorce/IconPack1/Pause_click.png);\n"
"}\n"
"\n"
"")
        self.PauseWav.setText("")
        self.PauseWav.setObjectName("PauseWav")
        self.gridLayout_10.addWidget(self.PauseWav, 0, 2, 1, 1)
        self.StopWav = QtWidgets.QPushButton(self.groupBox)
        self.StopWav.setMinimumSize(QtCore.QSize(25, 25))
        self.StopWav.setStyleSheet("QPushButton{\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"border-image:url(:/icon_pack/Resorce/IconPack1/Stop_white.png);\n"
"}\n"
"QPushButton:pressed{ \n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"border-image:url(:/icon_pack/Resorce/IconPack1/Stop_click.png);\n"
"}\n"
"\n"
"")
        self.StopWav.setText("")
        self.StopWav.setObjectName("StopWav")
        self.gridLayout_10.addWidget(self.StopWav, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 6, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setMinimumSize(QtCore.QSize(150, 50))
        self.groupBox_2.setMaximumSize(QtCore.QSize(150, 50))
        self.groupBox_2.setStyleSheet("background-color: rgb(71,77,82);\n"
"border-radius: 20px;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.VolumeSlider = QtWidgets.QSlider(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.VolumeSlider.setFont(font)
        self.VolumeSlider.setStyleSheet("QSlider::groove:horizontal {  \n"
"                height: 10px;\n"
"\n"
"}\n"
"\n"
"QSlider{\n"
"      border-radius: 10px;\n"
"}")
        self.VolumeSlider.setMaximum(100)
        self.VolumeSlider.setProperty("value", 20)
        self.VolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.gridLayout_13.addWidget(self.VolumeSlider, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 9, 1, 1)
        self.SampleRate = QtWidgets.QComboBox(self.groupBox_3)
        self.SampleRate.setMinimumSize(QtCore.QSize(29, 30))
        self.SampleRate.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.SampleRate.setFont(font)
        self.SampleRate.setAcceptDrops(False)
        self.SampleRate.setAutoFillBackground(False)
        self.SampleRate.setStyleSheet("border: 1px solid black;")
        self.SampleRate.setEditable(False)
        self.SampleRate.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.SampleRate.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.SampleRate.setDuplicatesEnabled(False)
        self.SampleRate.setFrame(True)
        self.SampleRate.setObjectName("SampleRate")
        self.SampleRate.addItem("")
        self.SampleRate.addItem("")
        self.SampleRate.addItem("")
        self.SampleRate.addItem("")
        self.gridLayout.addWidget(self.SampleRate, 0, 4, 1, 1)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.AddSpeech = QtWidgets.QCheckBox(self.groupBox_3)
        self.AddSpeech.setMinimumSize(QtCore.QSize(0, 30))
        self.AddSpeech.setSizeIncrement(QtCore.QSize(0, 0))
        self.AddSpeech.setStyleSheet("QCheckBox::indicator:unchecked{\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"    width: 18px;\n"
"    height: 30px;\n"
"border-image:url(:/icon_pack/Resorce/IconPack1/add_wave_white.png);\n"
"}\n"
"QCheckBox::indicator:checked{ \n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"    width: 18px;\n"
"    height: 30px;\n"
"border-image:url(:/icon_pack/Resorce/IconPack1/add_wave_click.png);\n"
"}\n"
"\n"
"")
        self.AddSpeech.setText("")
        self.AddSpeech.setObjectName("AddSpeech")
        self.horizontalLayout_23.addWidget(self.AddSpeech)
        self.Syntethis = QtWidgets.QPushButton(self.groupBox_3)
        self.Syntethis.setMinimumSize(QtCore.QSize(25, 25))
        self.Syntethis.setStyleSheet("QPushButton{\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"border-image:url(:/icon_pack/Resorce/IconPack1/wave_white.png);\n"
"}\n"
"QPushButton:pressed{ \n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"border-image:url(:/icon_pack/Resorce/IconPack1/wave_click.png);\n"
"}\n"
"\n"
"")
        self.Syntethis.setText("")
        self.Syntethis.setObjectName("Syntethis")
        self.horizontalLayout_23.addWidget(self.Syntethis)
        self.gridLayout.addLayout(self.horizontalLayout_23, 0, 10, 1, 1)
        self.WaveGlowModel = QtWidgets.QLineEdit(self.groupBox_3)
        self.WaveGlowModel.setMinimumSize(QtCore.QSize(200, 25))
        self.WaveGlowModel.setMaximumSize(QtCore.QSize(135, 16777215))
        self.WaveGlowModel.setStyleSheet("border: 1px solid black;")
        self.WaveGlowModel.setObjectName("WaveGlowModel")
        self.gridLayout.addWidget(self.WaveGlowModel, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 7, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 5, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.Spectrum = QtWidgets.QWidget(self.tab)
        self.Spectrum.setMinimumSize(QtCore.QSize(0, 70))
        self.Spectrum.setMaximumSize(QtCore.QSize(16777215, 80))
        self.Spectrum.setObjectName("Spectrum")
        self.verticalLayout_5.addWidget(self.Spectrum)
        self.gridLayout_15.addLayout(self.verticalLayout_5, 2, 0, 1, 1)
        self.checkpoint_path.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.logBox = QtWidgets.QTextEdit(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.logBox.setFont(font)
        self.logBox.setStyleSheet("border: 1px solid black;")
        self.logBox.setObjectName("logBox")
        self.gridLayout_2.addWidget(self.logBox, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.output_directory_label = QtWidgets.QLabel(self.tab_2)
        self.output_directory_label.setMinimumSize(QtCore.QSize(120, 0))
        self.output_directory_label.setObjectName("output_directory_label")
        self.horizontalLayout.addWidget(self.output_directory_label)
        self.output_directory = QtWidgets.QLineEdit(self.tab_2)
        self.output_directory.setMinimumSize(QtCore.QSize(200, 0))
        self.output_directory.setText("")
        self.output_directory.setObjectName("output_directory")
        self.horizontalLayout.addWidget(self.output_directory)
        self.output_directory_button = QtWidgets.QPushButton(self.tab_2)
        self.output_directory_button.setStyleSheet("border: 1px solid black;")
        self.output_directory_button.setObjectName("output_directory_button")
        self.horizontalLayout.addWidget(self.output_directory_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.log_directory_label = QtWidgets.QLabel(self.tab_2)
        self.log_directory_label.setMinimumSize(QtCore.QSize(120, 0))
        self.log_directory_label.setObjectName("log_directory_label")
        self.horizontalLayout_2.addWidget(self.log_directory_label)
        self.log_directory = QtWidgets.QLineEdit(self.tab_2)
        self.log_directory.setMinimumSize(QtCore.QSize(200, 0))
        self.log_directory.setText("")
        self.log_directory.setObjectName("log_directory")
        self.horizontalLayout_2.addWidget(self.log_directory)
        self.log_directory_button = QtWidgets.QPushButton(self.tab_2)
        self.log_directory_button.setStyleSheet("border: 1px solid black;")
        self.log_directory_button.setObjectName("log_directory_button")
        self.horizontalLayout_2.addWidget(self.log_directory_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkpoint_path_Box = QtWidgets.QCheckBox(self.tab_2)
        self.checkpoint_path_Box.setEnabled(True)
        self.checkpoint_path_Box.setMinimumSize(QtCore.QSize(120, 0))
        self.checkpoint_path_Box.setObjectName("checkpoint_path_Box")
        self.horizontalLayout_3.addWidget(self.checkpoint_path_Box)
        self.path_checkpoint = QtWidgets.QLineEdit(self.tab_2)
        self.path_checkpoint.setEnabled(False)
        self.path_checkpoint.setMinimumSize(QtCore.QSize(200, 0))
        self.path_checkpoint.setStyleSheet("border: 1px solid black;")
        self.path_checkpoint.setText("")
        self.path_checkpoint.setObjectName("path_checkpoint")
        self.horizontalLayout_3.addWidget(self.path_checkpoint)
        self.path_checkpoint_button = QtWidgets.QPushButton(self.tab_2)
        self.path_checkpoint_button.setEnabled(False)
        self.path_checkpoint_button.setStyleSheet("border: 1px solid black;")
        self.path_checkpoint_button.setObjectName("path_checkpoint_button")
        self.horizontalLayout_3.addWidget(self.path_checkpoint_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.training_files_label = QtWidgets.QLabel(self.tab_2)
        self.training_files_label.setMinimumSize(QtCore.QSize(120, 0))
        self.training_files_label.setObjectName("training_files_label")
        self.horizontalLayout_5.addWidget(self.training_files_label)
        self.training_files = QtWidgets.QLineEdit(self.tab_2)
        self.training_files.setMinimumSize(QtCore.QSize(200, 0))
        self.training_files.setText("")
        self.training_files.setObjectName("training_files")
        self.horizontalLayout_5.addWidget(self.training_files)
        self.training_files_button = QtWidgets.QPushButton(self.tab_2)
        self.training_files_button.setStyleSheet("border: 1px solid black;")
        self.training_files_button.setObjectName("training_files_button")
        self.horizontalLayout_5.addWidget(self.training_files_button)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.validation_files_label = QtWidgets.QLabel(self.tab_2)
        self.validation_files_label.setMinimumSize(QtCore.QSize(120, 0))
        self.validation_files_label.setObjectName("validation_files_label")
        self.horizontalLayout_6.addWidget(self.validation_files_label)
        self.validation_files = QtWidgets.QLineEdit(self.tab_2)
        self.validation_files.setMinimumSize(QtCore.QSize(200, 0))
        self.validation_files.setText("")
        self.validation_files.setObjectName("validation_files")
        self.horizontalLayout_6.addWidget(self.validation_files)
        self.validation_files_button = QtWidgets.QPushButton(self.tab_2)
        self.validation_files_button.setStyleSheet("border: 1px solid black;")
        self.validation_files_button.setObjectName("validation_files_button")
        self.horizontalLayout_6.addWidget(self.validation_files_button)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.warm_start = QtWidgets.QCheckBox(self.tab_2)
        self.warm_start.setObjectName("warm_start")
        self.verticalLayout_2.addWidget(self.warm_start)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.StartTrain = QtWidgets.QPushButton(self.tab_2)
        self.StartTrain.setMinimumSize(QtCore.QSize(0, 50))
        self.StartTrain.setStyleSheet("border: 1px solid black;")
        self.StartTrain.setObjectName("StartTrain")
        self.verticalLayout_3.addWidget(self.StartTrain)
        self.Stop = QtWidgets.QPushButton(self.tab_2)
        self.Stop.setMinimumSize(QtCore.QSize(0, 50))
        self.Stop.setStyleSheet("border: 1px solid black;")
        self.Stop.setObjectName("Stop")
        self.verticalLayout_3.addWidget(self.Stop)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.AudioParametersVariable = QtWidgets.QGroupBox(self.tab_2)
        self.AudioParametersVariable.setMinimumSize(QtCore.QSize(200, 0))
        self.AudioParametersVariable.setStyleSheet("border: 1px solid black;")
        self.AudioParametersVariable.setObjectName("AudioParametersVariable")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.AudioParametersVariable)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.AudioParametersVariable)
        self.label_8.setMinimumSize(QtCore.QSize(85, 0))
        self.label_8.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_8.setStyleSheet("border: 0;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.filter_length = QtWidgets.QSpinBox(self.AudioParametersVariable)
        self.filter_length.setMinimum(743)
        self.filter_length.setMaximum(1111111111)
        self.filter_length.setProperty("value", 1024)
        self.filter_length.setObjectName("filter_length")
        self.horizontalLayout_9.addWidget(self.filter_length)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.AudioParametersVariable)
        self.label_7.setMinimumSize(QtCore.QSize(85, 0))
        self.label_7.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_7.setStyleSheet("border: 0;")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.sampling_rate = QtWidgets.QSpinBox(self.AudioParametersVariable)
        self.sampling_rate.setMinimum(16000)
        self.sampling_rate.setMaximum(48000)
        self.sampling_rate.setSingleStep(50)
        self.sampling_rate.setProperty("value", 22050)
        self.sampling_rate.setObjectName("sampling_rate")
        self.horizontalLayout_8.addWidget(self.sampling_rate)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.AudioParametersVariable)
        self.label_9.setMinimumSize(QtCore.QSize(85, 0))
        self.label_9.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_9.setStyleSheet("border: 0;")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.hop_length = QtWidgets.QSpinBox(self.AudioParametersVariable)
        self.hop_length.setMinimum(186)
        self.hop_length.setMaximum(256)
        self.hop_length.setProperty("value", 256)
        self.hop_length.setObjectName("hop_length")
        self.horizontalLayout_10.addWidget(self.hop_length)
        self.gridLayout_4.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.AudioParametersVariable)
        self.label_10.setMinimumSize(QtCore.QSize(85, 0))
        self.label_10.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_10.setStyleSheet("border: 0;")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.win_length = QtWidgets.QSpinBox(self.AudioParametersVariable)
        self.win_length.setMinimum(743)
        self.win_length.setMaximum(2048)
        self.win_length.setProperty("value", 1024)
        self.win_length.setObjectName("win_length")
        self.horizontalLayout_11.addWidget(self.win_length)
        self.gridLayout_4.addLayout(self.horizontalLayout_11, 5, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.AudioParametersVariable)
        self.label_11.setMinimumSize(QtCore.QSize(85, 0))
        self.label_11.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_11.setStyleSheet("border: 0;")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        self.n_mel_channels = QtWidgets.QSpinBox(self.AudioParametersVariable)
        self.n_mel_channels.setProperty("value", 80)
        self.n_mel_channels.setObjectName("n_mel_channels")
        self.horizontalLayout_12.addWidget(self.n_mel_channels)
        self.gridLayout_4.addLayout(self.horizontalLayout_12, 6, 0, 1, 1)
        self.AudioParametersBox = QtWidgets.QComboBox(self.AudioParametersVariable)
        self.AudioParametersBox.setObjectName("AudioParametersBox")
        self.AudioParametersBox.addItem("")
        self.AudioParametersBox.addItem("")
        self.AudioParametersBox.addItem("")
        self.gridLayout_4.addWidget(self.AudioParametersBox, 0, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_13 = QtWidgets.QLabel(self.AudioParametersVariable)
        self.label_13.setMinimumSize(QtCore.QSize(85, 0))
        self.label_13.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_13.setStyleSheet("border: 0;")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_14.addWidget(self.label_13)
        self.mel_fmax = QtWidgets.QDoubleSpinBox(self.AudioParametersVariable)
        self.mel_fmax.setMaximum(8000.0)
        self.mel_fmax.setProperty("value", 8000.0)
        self.mel_fmax.setObjectName("mel_fmax")
        self.horizontalLayout_14.addWidget(self.mel_fmax)
        self.gridLayout_4.addLayout(self.horizontalLayout_14, 8, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.AudioParametersVariable)
        self.label_12.setMinimumSize(QtCore.QSize(85, 0))
        self.label_12.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_12.setStyleSheet("border: 0;")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.mel_fmin = QtWidgets.QDoubleSpinBox(self.AudioParametersVariable)
        self.mel_fmin.setObjectName("mel_fmin")
        self.horizontalLayout_13.addWidget(self.mel_fmin)
        self.gridLayout_4.addLayout(self.horizontalLayout_13, 7, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.AudioParametersVariable)
        self.label_6.setMinimumSize(QtCore.QSize(85, 0))
        self.label_6.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_6.setStyleSheet("border: 0;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.max_wav_value = QtWidgets.QDoubleSpinBox(self.AudioParametersVariable)
        self.max_wav_value.setMaximum(999999999999999.0)
        self.max_wav_value.setProperty("value", 32768.0)
        self.max_wav_value.setObjectName("max_wav_value")
        self.horizontalLayout_7.addWidget(self.max_wav_value)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.gridLayout_12.addWidget(self.AudioParametersVariable, 0, 0, 3, 1)
        self.EncoderDecoderVariable = QtWidgets.QGroupBox(self.tab_2)
        self.EncoderDecoderVariable.setStyleSheet("border: 1px solid black;")
        self.EncoderDecoderVariable.setObjectName("EncoderDecoderVariable")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.EncoderDecoderVariable)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_17 = QtWidgets.QLabel(self.EncoderDecoderVariable)
        self.label_17.setMinimumSize(QtCore.QSize(150, 0))
        self.label_17.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_17.setStyleSheet("border: 0;")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_20.addWidget(self.label_17)
        self.encoder_kernel_size = QtWidgets.QSpinBox(self.EncoderDecoderVariable)
        self.encoder_kernel_size.setMinimum(1)
        self.encoder_kernel_size.setMaximum(10)
        self.encoder_kernel_size.setSingleStep(1)
        self.encoder_kernel_size.setProperty("value", 5)
        self.encoder_kernel_size.setObjectName("encoder_kernel_size")
        self.horizontalLayout_20.addWidget(self.encoder_kernel_size)
        self.gridLayout_7.addLayout(self.horizontalLayout_20, 0, 0, 1, 1)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_23 = QtWidgets.QLabel(self.EncoderDecoderVariable)
        self.label_23.setMinimumSize(QtCore.QSize(150, 0))
        self.label_23.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_23.setStyleSheet("border: 0;")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_26.addWidget(self.label_23)
        self.max_decoder_steps = QtWidgets.QSpinBox(self.EncoderDecoderVariable)
        self.max_decoder_steps.setMinimum(500)
        self.max_decoder_steps.setMaximum(2000)
        self.max_decoder_steps.setSingleStep(500)
        self.max_decoder_steps.setProperty("value", 1000)
        self.max_decoder_steps.setObjectName("max_decoder_steps")
        self.horizontalLayout_26.addWidget(self.max_decoder_steps)
        self.gridLayout_7.addLayout(self.horizontalLayout_26, 5, 0, 1, 1)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_24 = QtWidgets.QLabel(self.EncoderDecoderVariable)
        self.label_24.setMinimumSize(QtCore.QSize(150, 0))
        self.label_24.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_24.setStyleSheet("border: 0;")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_27.addWidget(self.label_24)
        self.gate_threshold = QtWidgets.QDoubleSpinBox(self.EncoderDecoderVariable)
        self.gate_threshold.setMinimum(0.1)
        self.gate_threshold.setMaximum(1.0)
        self.gate_threshold.setSingleStep(0.1)
        self.gate_threshold.setProperty("value", 0.5)
        self.gate_threshold.setObjectName("gate_threshold")
        self.horizontalLayout_27.addWidget(self.gate_threshold)
        self.gridLayout_7.addLayout(self.horizontalLayout_27, 6, 0, 1, 1)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_25 = QtWidgets.QLabel(self.EncoderDecoderVariable)
        self.label_25.setMinimumSize(QtCore.QSize(150, 0))
        self.label_25.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_25.setStyleSheet("border: 0;")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_28.addWidget(self.label_25)
        self.p_attention_dropout = QtWidgets.QDoubleSpinBox(self.EncoderDecoderVariable)
        self.p_attention_dropout.setMinimum(0.1)
        self.p_attention_dropout.setMaximum(1.0)
        self.p_attention_dropout.setSingleStep(0.1)
        self.p_attention_dropout.setProperty("value", 0.1)
        self.p_attention_dropout.setObjectName("p_attention_dropout")
        self.horizontalLayout_28.addWidget(self.p_attention_dropout)
        self.gridLayout_7.addLayout(self.horizontalLayout_28, 7, 0, 1, 1)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_18 = QtWidgets.QLabel(self.EncoderDecoderVariable)
        self.label_18.setMinimumSize(QtCore.QSize(150, 0))
        self.label_18.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_18.setStyleSheet("border: 0;")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_21.addWidget(self.label_18)
        self.encoder_n_convolutions = QtWidgets.QSpinBox(self.EncoderDecoderVariable)
        self.encoder_n_convolutions.setMinimum(1)
        self.encoder_n_convolutions.setMaximum(10)
        self.encoder_n_convolutions.setSingleStep(1)
        self.encoder_n_convolutions.setProperty("value", 3)
        self.encoder_n_convolutions.setObjectName("encoder_n_convolutions")
        self.horizontalLayout_21.addWidget(self.encoder_n_convolutions)
        self.gridLayout_7.addLayout(self.horizontalLayout_21, 1, 0, 1, 1)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_26 = QtWidgets.QLabel(self.EncoderDecoderVariable)
        self.label_26.setMinimumSize(QtCore.QSize(150, 0))
        self.label_26.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_26.setStyleSheet("border: 0;")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_29.addWidget(self.label_26)
        self.p_decoder_dropout = QtWidgets.QDoubleSpinBox(self.EncoderDecoderVariable)
        self.p_decoder_dropout.setMinimum(0.1)
        self.p_decoder_dropout.setMaximum(1.0)
        self.p_decoder_dropout.setSingleStep(0.1)
        self.p_decoder_dropout.setProperty("value", 0.1)
        self.p_decoder_dropout.setObjectName("p_decoder_dropout")
        self.horizontalLayout_29.addWidget(self.p_decoder_dropout)
        self.gridLayout_7.addLayout(self.horizontalLayout_29, 8, 0, 1, 1)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_19 = QtWidgets.QLabel(self.EncoderDecoderVariable)
        self.label_19.setMinimumSize(QtCore.QSize(150, 0))
        self.label_19.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_19.setStyleSheet("border: 0;")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_22.addWidget(self.label_19)
        self.encoder_embedding_dim = QtWidgets.QSpinBox(self.EncoderDecoderVariable)
        self.encoder_embedding_dim.setMinimum(128)
        self.encoder_embedding_dim.setMaximum(2048)
        self.encoder_embedding_dim.setSingleStep(128)
        self.encoder_embedding_dim.setProperty("value", 512)
        self.encoder_embedding_dim.setObjectName("encoder_embedding_dim")
        self.horizontalLayout_22.addWidget(self.encoder_embedding_dim)
        self.gridLayout_7.addLayout(self.horizontalLayout_22, 2, 0, 1, 1)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_21 = QtWidgets.QLabel(self.EncoderDecoderVariable)
        self.label_21.setMinimumSize(QtCore.QSize(150, 0))
        self.label_21.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_21.setStyleSheet("border: 0;")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_24.addWidget(self.label_21)
        self.decoder_rnn_dim = QtWidgets.QSpinBox(self.EncoderDecoderVariable)
        self.decoder_rnn_dim.setMinimum(256)
        self.decoder_rnn_dim.setMaximum(4096)
        self.decoder_rnn_dim.setSingleStep(256)
        self.decoder_rnn_dim.setProperty("value", 1024)
        self.decoder_rnn_dim.setObjectName("decoder_rnn_dim")
        self.horizontalLayout_24.addWidget(self.decoder_rnn_dim)
        self.gridLayout_7.addLayout(self.horizontalLayout_24, 3, 0, 1, 1)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_22 = QtWidgets.QLabel(self.EncoderDecoderVariable)
        self.label_22.setMinimumSize(QtCore.QSize(150, 0))
        self.label_22.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_22.setStyleSheet("border: 0;")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_25.addWidget(self.label_22)
        self.prenet_dim = QtWidgets.QSpinBox(self.EncoderDecoderVariable)
        self.prenet_dim.setMinimum(64)
        self.prenet_dim.setMaximum(1024)
        self.prenet_dim.setSingleStep(64)
        self.prenet_dim.setProperty("value", 256)
        self.prenet_dim.setObjectName("prenet_dim")
        self.horizontalLayout_25.addWidget(self.prenet_dim)
        self.gridLayout_7.addLayout(self.horizontalLayout_25, 4, 0, 1, 1)
        self.gridLayout_12.addWidget(self.EncoderDecoderVariable, 0, 1, 3, 1)
        self.MelPostVariable = QtWidgets.QGroupBox(self.tab_2)
        self.MelPostVariable.setStyleSheet("border: 1px solid black;")
        self.MelPostVariable.setObjectName("MelPostVariable")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.MelPostVariable)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_32 = QtWidgets.QLabel(self.MelPostVariable)
        self.label_32.setMinimumSize(QtCore.QSize(150, 0))
        self.label_32.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_32.setStyleSheet("border: 0;")
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_35.addWidget(self.label_32)
        self.postnet_embedding_dim = QtWidgets.QSpinBox(self.MelPostVariable)
        self.postnet_embedding_dim.setMinimum(256)
        self.postnet_embedding_dim.setMaximum(1024)
        self.postnet_embedding_dim.setSingleStep(256)
        self.postnet_embedding_dim.setProperty("value", 512)
        self.postnet_embedding_dim.setObjectName("postnet_embedding_dim")
        self.horizontalLayout_35.addWidget(self.postnet_embedding_dim)
        self.gridLayout_9.addLayout(self.horizontalLayout_35, 0, 0, 1, 1)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_33 = QtWidgets.QLabel(self.MelPostVariable)
        self.label_33.setMinimumSize(QtCore.QSize(150, 0))
        self.label_33.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_33.setStyleSheet("border: 0;")
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_36.addWidget(self.label_33)
        self.postnet_kernel_size = QtWidgets.QSpinBox(self.MelPostVariable)
        self.postnet_kernel_size.setMinimum(1)
        self.postnet_kernel_size.setMaximum(10)
        self.postnet_kernel_size.setSingleStep(1)
        self.postnet_kernel_size.setProperty("value", 5)
        self.postnet_kernel_size.setObjectName("postnet_kernel_size")
        self.horizontalLayout_36.addWidget(self.postnet_kernel_size)
        self.gridLayout_9.addLayout(self.horizontalLayout_36, 1, 0, 1, 1)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_31 = QtWidgets.QLabel(self.MelPostVariable)
        self.label_31.setMinimumSize(QtCore.QSize(150, 0))
        self.label_31.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_31.setStyleSheet("border: 0;")
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_34.addWidget(self.label_31)
        self.postnet_n_convolutions = QtWidgets.QSpinBox(self.MelPostVariable)
        self.postnet_n_convolutions.setMinimum(1)
        self.postnet_n_convolutions.setMaximum(10)
        self.postnet_n_convolutions.setSingleStep(1)
        self.postnet_n_convolutions.setProperty("value", 5)
        self.postnet_n_convolutions.setObjectName("postnet_n_convolutions")
        self.horizontalLayout_34.addWidget(self.postnet_n_convolutions)
        self.gridLayout_9.addLayout(self.horizontalLayout_34, 2, 0, 1, 1)
        self.gridLayout_12.addWidget(self.MelPostVariable, 0, 2, 1, 1)
        self.AttentionVariable = QtWidgets.QGroupBox(self.tab_2)
        self.AttentionVariable.setStyleSheet("border: 1px solid black;")
        self.AttentionVariable.setObjectName("AttentionVariable")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.AttentionVariable)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_28 = QtWidgets.QLabel(self.AttentionVariable)
        self.label_28.setMinimumSize(QtCore.QSize(150, 0))
        self.label_28.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_28.setStyleSheet("border: 0;")
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_31.addWidget(self.label_28)
        self.attention_rnn_dim = QtWidgets.QSpinBox(self.AttentionVariable)
        self.attention_rnn_dim.setMinimum(512)
        self.attention_rnn_dim.setMaximum(2048)
        self.attention_rnn_dim.setSingleStep(512)
        self.attention_rnn_dim.setProperty("value", 1024)
        self.attention_rnn_dim.setObjectName("attention_rnn_dim")
        self.horizontalLayout_31.addWidget(self.attention_rnn_dim)
        self.gridLayout_8.addLayout(self.horizontalLayout_31, 0, 0, 1, 1)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_30 = QtWidgets.QLabel(self.AttentionVariable)
        self.label_30.setMinimumSize(QtCore.QSize(150, 0))
        self.label_30.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_30.setStyleSheet("border: 0;")
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_33.addWidget(self.label_30)
        self.attention_dim = QtWidgets.QSpinBox(self.AttentionVariable)
        self.attention_dim.setMinimum(64)
        self.attention_dim.setMaximum(512)
        self.attention_dim.setSingleStep(64)
        self.attention_dim.setProperty("value", 128)
        self.attention_dim.setObjectName("attention_dim")
        self.horizontalLayout_33.addWidget(self.attention_dim)
        self.gridLayout_8.addLayout(self.horizontalLayout_33, 1, 0, 1, 1)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_29 = QtWidgets.QLabel(self.AttentionVariable)
        self.label_29.setMinimumSize(QtCore.QSize(150, 0))
        self.label_29.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_29.setStyleSheet("border: 0;")
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_32.addWidget(self.label_29)
        self.attention_location_n_filters = QtWidgets.QSpinBox(self.AttentionVariable)
        self.attention_location_n_filters.setMinimum(1)
        self.attention_location_n_filters.setMaximum(100)
        self.attention_location_n_filters.setSingleStep(1)
        self.attention_location_n_filters.setProperty("value", 32)
        self.attention_location_n_filters.setObjectName("attention_location_n_filters")
        self.horizontalLayout_32.addWidget(self.attention_location_n_filters)
        self.gridLayout_8.addLayout(self.horizontalLayout_32, 2, 0, 1, 1)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_27 = QtWidgets.QLabel(self.AttentionVariable)
        self.label_27.setMinimumSize(QtCore.QSize(150, 0))
        self.label_27.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_27.setStyleSheet("border: 0;")
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_30.addWidget(self.label_27)
        self.attention_location_kernel_size = QtWidgets.QSpinBox(self.AttentionVariable)
        self.attention_location_kernel_size.setMinimum(1)
        self.attention_location_kernel_size.setMaximum(100)
        self.attention_location_kernel_size.setSingleStep(1)
        self.attention_location_kernel_size.setProperty("value", 31)
        self.attention_location_kernel_size.setObjectName("attention_location_kernel_size")
        self.horizontalLayout_30.addWidget(self.attention_location_kernel_size)
        self.gridLayout_8.addLayout(self.horizontalLayout_30, 3, 0, 1, 1)
        self.gridLayout_12.addWidget(self.AttentionVariable, 0, 3, 2, 1)
        self.ExperimentVariable = QtWidgets.QGroupBox(self.tab_2)
        self.ExperimentVariable.setStyleSheet("border: 1px solid black;")
        self.ExperimentVariable.setObjectName("ExperimentVariable")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.ExperimentVariable)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.text_cleaners_box = QtWidgets.QComboBox(self.ExperimentVariable)
        self.text_cleaners_box.setObjectName("text_cleaners_box")
        self.text_cleaners_box.addItem("")
        self.text_cleaners_box.addItem("")
        self.gridLayout_5.addWidget(self.text_cleaners_box, 4, 0, 1, 1)
        self.cudnn_enabled = QtWidgets.QCheckBox(self.ExperimentVariable)
        self.cudnn_enabled.setStyleSheet("border: 0;")
        self.cudnn_enabled.setChecked(True)
        self.cudnn_enabled.setObjectName("cudnn_enabled")
        self.gridLayout_5.addWidget(self.cudnn_enabled, 2, 0, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_16 = QtWidgets.QLabel(self.ExperimentVariable)
        self.label_16.setMinimumSize(QtCore.QSize(85, 0))
        self.label_16.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_16.setStyleSheet("border: 0;")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_19.addWidget(self.label_16)
        self.iters_per_checkpoint = QtWidgets.QSpinBox(self.ExperimentVariable)
        self.iters_per_checkpoint.setMinimum(100)
        self.iters_per_checkpoint.setMaximum(5000)
        self.iters_per_checkpoint.setSingleStep(100)
        self.iters_per_checkpoint.setProperty("value", 1000)
        self.iters_per_checkpoint.setObjectName("iters_per_checkpoint")
        self.horizontalLayout_19.addWidget(self.iters_per_checkpoint)
        self.gridLayout_5.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)
        self.cudnn_benchmark = QtWidgets.QCheckBox(self.ExperimentVariable)
        self.cudnn_benchmark.setStyleSheet("border: 0;")
        self.cudnn_benchmark.setObjectName("cudnn_benchmark")
        self.gridLayout_5.addWidget(self.cudnn_benchmark, 3, 0, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_15 = QtWidgets.QLabel(self.ExperimentVariable)
        self.label_15.setMinimumSize(QtCore.QSize(85, 0))
        self.label_15.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_15.setStyleSheet("border: 0;")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_18.addWidget(self.label_15)
        self.epoch = QtWidgets.QSpinBox(self.ExperimentVariable)
        self.epoch.setMinimum(200)
        self.epoch.setMaximum(20000)
        self.epoch.setSingleStep(25)
        self.epoch.setProperty("value", 500)
        self.epoch.setObjectName("epoch")
        self.horizontalLayout_18.addWidget(self.epoch)
        self.gridLayout_5.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)
        self.load_mel_from_disk = QtWidgets.QCheckBox(self.ExperimentVariable)
        self.load_mel_from_disk.setStyleSheet("border: 0;")
        self.load_mel_from_disk.setObjectName("load_mel_from_disk")
        self.gridLayout_5.addWidget(self.load_mel_from_disk, 5, 0, 1, 1)
        self.gridLayout_12.addWidget(self.ExperimentVariable, 1, 2, 2, 1)
        self.OptimizationVariable = QtWidgets.QGroupBox(self.tab_2)
        self.OptimizationVariable.setStyleSheet("border: 1px solid black;")
        self.OptimizationVariable.setObjectName("OptimizationVariable")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.OptimizationVariable)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.use_saved_learning_rate = QtWidgets.QCheckBox(self.OptimizationVariable)
        self.use_saved_learning_rate.setStyleSheet("border: 0;")
        self.use_saved_learning_rate.setObjectName("use_saved_learning_rate")
        self.gridLayout_11.addWidget(self.use_saved_learning_rate, 0, 0, 1, 1)
        self.mask_padding = QtWidgets.QCheckBox(self.OptimizationVariable)
        self.mask_padding.setStyleSheet("border: 0;")
        self.mask_padding.setChecked(True)
        self.mask_padding.setObjectName("mask_padding")
        self.gridLayout_11.addWidget(self.mask_padding, 1, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_34 = QtWidgets.QLabel(self.OptimizationVariable)
        self.label_34.setMinimumSize(QtCore.QSize(85, 0))
        self.label_34.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_34.setStyleSheet("border: 0;")
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_17.addWidget(self.label_34)
        self.learning_rate = QtWidgets.QSpinBox(self.OptimizationVariable)
        self.learning_rate.setMinimum(1)
        self.learning_rate.setMaximum(10)
        self.learning_rate.setProperty("value", 3)
        self.learning_rate.setObjectName("learning_rate")
        self.horizontalLayout_17.addWidget(self.learning_rate)
        self.gridLayout_11.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_14 = QtWidgets.QLabel(self.OptimizationVariable)
        self.label_14.setMinimumSize(QtCore.QSize(85, 0))
        self.label_14.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_14.setStyleSheet("border: 0;")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_15.addWidget(self.label_14)
        self.weight_decay = QtWidgets.QSpinBox(self.OptimizationVariable)
        self.weight_decay.setMinimum(1)
        self.weight_decay.setMaximum(10)
        self.weight_decay.setProperty("value", 6)
        self.weight_decay.setObjectName("weight_decay")
        self.horizontalLayout_15.addWidget(self.weight_decay)
        self.gridLayout_11.addLayout(self.horizontalLayout_15, 3, 0, 1, 1)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_35 = QtWidgets.QLabel(self.OptimizationVariable)
        self.label_35.setMinimumSize(QtCore.QSize(85, 0))
        self.label_35.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_35.setStyleSheet("border: 0;")
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_37.addWidget(self.label_35)
        self.batch_size = QtWidgets.QSpinBox(self.OptimizationVariable)
        self.batch_size.setMinimum(4)
        self.batch_size.setMaximum(64)
        self.batch_size.setProperty("value", 8)
        self.batch_size.setObjectName("batch_size")
        self.horizontalLayout_37.addWidget(self.batch_size)
        self.gridLayout_11.addLayout(self.horizontalLayout_37, 4, 0, 1, 1)
        self.gridLayout_12.addWidget(self.OptimizationVariable, 2, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_12, 2, 0, 1, 1)
        self.checkpoint_path.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.checkpoint_path, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.checkpoint_path.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.SampleRate.setCurrentIndex(1)
        self.AudioParametersBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TTS"))
        self.Text_to_Speech.setToolTip(_translate("MainWindow", "Поле для ввода текста"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "1"))
        self.Text_to_Speech_2.setToolTip(_translate("MainWindow", "Поле для ввода текста"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "2"))
        self.Text_to_Speech_3.setToolTip(_translate("MainWindow", "Поле для ввода текста"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "3"))
        self.Text_to_Speech_4.setToolTip(_translate("MainWindow", "Поле для ввода текста"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "4"))
        self.ControlBox.setTitle(_translate("MainWindow", "SELECT TYPE OF VOICE"))
        self.SaveAudio.setToolTip(_translate("MainWindow", "Сохранть в файл"))
        self.LoadWaveGlowModel.setToolTip(_translate("MainWindow", "Загрузить модель вокодера"))
        self.LoadWaveGlowModel.setText(_translate("MainWindow", "LoadWaveGlow"))
        self.PlayWav.setToolTip(_translate("MainWindow", "Старт"))
        self.PauseWav.setToolTip(_translate("MainWindow", "Пауза"))
        self.StopWav.setToolTip(_translate("MainWindow", "Стоп"))
        self.VolumeSlider.setToolTip(_translate("MainWindow", "Громкость"))
        self.SampleRate.setToolTip(_translate("MainWindow", "Частота дискретизации"))
        self.SampleRate.setItemText(0, _translate("MainWindow", "16000"))
        self.SampleRate.setItemText(1, _translate("MainWindow", "22050"))
        self.SampleRate.setItemText(2, _translate("MainWindow", "44100"))
        self.SampleRate.setItemText(3, _translate("MainWindow", "48000"))
        self.AddSpeech.setToolTip(_translate("MainWindow", "Добавить речь"))
        self.Syntethis.setToolTip(_translate("MainWindow", "Синтезировать речь"))
        self.WaveGlowModel.setToolTip(_translate("MainWindow", "Путь вокодера"))
        self.checkpoint_path.setTabText(self.checkpoint_path.indexOf(self.tab), _translate("MainWindow", "Synthesis"))
        self.output_directory_label.setText(_translate("MainWindow", "output_directory"))
        self.output_directory_button.setText(_translate("MainWindow", "Open_folder"))
        self.log_directory_label.setText(_translate("MainWindow", "log_directory"))
        self.log_directory_button.setText(_translate("MainWindow", "Open_folder"))
        self.checkpoint_path_Box.setText(_translate("MainWindow", "checkpoint_path"))
        self.path_checkpoint_button.setText(_translate("MainWindow", "Open_folder"))
        self.training_files_label.setText(_translate("MainWindow", "training_files"))
        self.training_files_button.setText(_translate("MainWindow", "Open_folder"))
        self.validation_files_label.setText(_translate("MainWindow", "validation_files"))
        self.validation_files_button.setText(_translate("MainWindow", "Open_folder"))
        self.warm_start.setText(_translate("MainWindow", "warm_start"))
        self.StartTrain.setText(_translate("MainWindow", "Train"))
        self.Stop.setText(_translate("MainWindow", "Stop"))
        self.AudioParametersVariable.setTitle(_translate("MainWindow", "Audio Parameters"))
        self.label_8.setText(_translate("MainWindow", "filter_length"))
        self.label_7.setText(_translate("MainWindow", "sampling_rate"))
        self.label_9.setText(_translate("MainWindow", "hop_length"))
        self.label_10.setText(_translate("MainWindow", "win_length"))
        self.label_11.setText(_translate("MainWindow", "n_mel_channels"))
        self.AudioParametersBox.setItemText(0, _translate("MainWindow", "16kHz"))
        self.AudioParametersBox.setItemText(1, _translate("MainWindow", "22kHz"))
        self.AudioParametersBox.setItemText(2, _translate("MainWindow", "44kHz"))
        self.label_13.setText(_translate("MainWindow", "mel_fmax"))
        self.label_12.setText(_translate("MainWindow", "mel_fmin"))
        self.label_6.setText(_translate("MainWindow", "max_wav_value"))
        self.EncoderDecoderVariable.setTitle(_translate("MainWindow", "Encoder & Decoder parameters"))
        self.label_17.setText(_translate("MainWindow", "encoder_kernel_size"))
        self.label_23.setText(_translate("MainWindow", "max_decoder_steps"))
        self.label_24.setText(_translate("MainWindow", "gate_threshold"))
        self.label_25.setText(_translate("MainWindow", "p_attention_dropout"))
        self.label_18.setText(_translate("MainWindow", "encoder_n_convolutions"))
        self.label_26.setText(_translate("MainWindow", "p_decoder_dropout"))
        self.label_19.setText(_translate("MainWindow", "encoder_embedding_dim"))
        self.label_21.setText(_translate("MainWindow", "decoder_rnn_dim"))
        self.label_22.setText(_translate("MainWindow", "prenet_dim"))
        self.MelPostVariable.setTitle(_translate("MainWindow", "Mel-post processing network parameters"))
        self.label_32.setText(_translate("MainWindow", "postnet_embedding_dim"))
        self.label_33.setText(_translate("MainWindow", "postnet_kernel_size"))
        self.label_31.setText(_translate("MainWindow", "postnet_n_convolutions"))
        self.AttentionVariable.setTitle(_translate("MainWindow", "Attention Location Layer parameters"))
        self.label_28.setText(_translate("MainWindow", "attention_rnn_dim"))
        self.label_30.setText(_translate("MainWindow", "attention_dim"))
        self.label_29.setText(_translate("MainWindow", "attention_location_n_filters"))
        self.label_27.setText(_translate("MainWindow", "attention_location_kernel_size"))
        self.ExperimentVariable.setTitle(_translate("MainWindow", "Experiment & Data Parameters"))
        self.text_cleaners_box.setItemText(0, _translate("MainWindow", "english_cleaners"))
        self.text_cleaners_box.setItemText(1, _translate("MainWindow", "basic_cleaners"))
        self.cudnn_enabled.setText(_translate("MainWindow", "cudnn_enabled"))
        self.label_16.setText(_translate("MainWindow", "iters_per_checkpoint"))
        self.cudnn_benchmark.setText(_translate("MainWindow", "cudnn_benchmark"))
        self.label_15.setText(_translate("MainWindow", "epoch"))
        self.load_mel_from_disk.setText(_translate("MainWindow", "load_mel_from_disk"))
        self.OptimizationVariable.setTitle(_translate("MainWindow", "Optimization Hyperparameters"))
        self.use_saved_learning_rate.setText(_translate("MainWindow", "use_saved_learning_rate"))
        self.mask_padding.setText(_translate("MainWindow", "mask_padding"))
        self.label_34.setText(_translate("MainWindow", "learning_rate"))
        self.label_14.setText(_translate("MainWindow", "weight_decay"))
        self.label_35.setText(_translate("MainWindow", "batch_size"))
        self.checkpoint_path.setTabText(self.checkpoint_path.indexOf(self.tab_2), _translate("MainWindow", "Training"))
import breeze_rc
import icon_pack_rc
