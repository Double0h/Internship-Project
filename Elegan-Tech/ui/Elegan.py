# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Elegan.ui',
# licensing of 'Elegan.ui' applies.
#
# Created: Wed Aug  7 11:03:48 2019
#      by: pyside2-uic  running on PySide2 5.11.4a1.dev1546291887
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 669)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 669))
        MainWindow.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(125, 9, 9);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(555, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(750, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        self.comboBox_Port = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Port.setMinimumSize(QtCore.QSize(120, 34))
        self.comboBox_Port.setObjectName("comboBox_Port")
        self.horizontalLayout_11.addWidget(self.comboBox_Port)
        self.pushButton_Connect = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Connect.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_Connect.setStyleSheet("")
        self.pushButton_Connect.setObjectName("pushButton_Connect")
        self.horizontalLayout_11.addWidget(self.pushButton_Connect)
        self.pushButton_Disconnect = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Disconnect.setEnabled(True)
        self.pushButton_Disconnect.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_Disconnect.setObjectName("pushButton_Disconnect")
        self.horizontalLayout_11.addWidget(self.pushButton_Disconnect)
        self.horizontalLayout_12.addWidget(self.groupBox)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_start.setMaximumSize(QtCore.QSize(139, 55))
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_12.addWidget(self.pushButton_start)
        self.pushButton_disable_motors = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_disable_motors.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_disable_motors.setMaximumSize(QtCore.QSize(139, 55))
        self.pushButton_disable_motors.setObjectName("pushButton_disable_motors")
        self.horizontalLayout_12.addWidget(self.pushButton_disable_motors)
        self.pushButton_Reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Reset.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_Reset.setMaximumSize(QtCore.QSize(139, 55))
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.horizontalLayout_12.addWidget(self.pushButton_Reset)
        self.pushButton_Stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Stop.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_Stop.setMaximumSize(QtCore.QSize(139, 55))
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.horizontalLayout_12.addWidget(self.pushButton_Stop)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(325, 330))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setMinimumSize(QtCore.QSize(120, 30))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox_Yayma_hizi = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_Yayma_hizi.setMinimumSize(QtCore.QSize(120, 30))
        self.spinBox_Yayma_hizi.setObjectName("spinBox_Yayma_hizi")
        self.horizontalLayout.addWidget(self.spinBox_Yayma_hizi)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setMinimumSize(QtCore.QSize(120, 30))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.spinBox_Aci = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_Aci.setMinimumSize(QtCore.QSize(120, 30))
        self.spinBox_Aci.setObjectName("spinBox_Aci")
        self.horizontalLayout_3.addWidget(self.spinBox_Aci)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setMinimumSize(QtCore.QSize(120, 30))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.spinBox_Rampa = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_Rampa.setMinimumSize(QtCore.QSize(120, 30))
        self.spinBox_Rampa.setObjectName("spinBox_Rampa")
        self.horizontalLayout_2.addWidget(self.spinBox_Rampa)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.checkBox_Yayma = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_Yayma.setObjectName("checkBox_Yayma")
        self.verticalLayout_7.addWidget(self.checkBox_Yayma)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setMinimumSize(QtCore.QSize(120, 30))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setMinimumSize(QtCore.QSize(120, 30))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_13.addWidget(self.label_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox_Miktar = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_Miktar.setMinimumSize(QtCore.QSize(120, 34))
        self.comboBox_Miktar.setObjectName("comboBox_Miktar")
        self.horizontalLayout_4.addWidget(self.comboBox_Miktar)
        self.comboBox_Tup = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_Tup.setMinimumSize(QtCore.QSize(120, 34))
        self.comboBox_Tup.setStyleSheet("")
        self.comboBox_Tup.setObjectName("comboBox_Tup")
        self.horizontalLayout_4.addWidget(self.comboBox_Tup)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.pushButton_Yayma = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(75)
        sizePolicy.setVerticalStretch(23)
        sizePolicy.setHeightForWidth(self.pushButton_Yayma.sizePolicy().hasHeightForWidth())
        self.pushButton_Yayma.setSizePolicy(sizePolicy)
        self.pushButton_Yayma.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_Yayma.setStyleSheet("")
        self.pushButton_Yayma.setObjectName("pushButton_Yayma")
        self.verticalLayout_7.addWidget(self.pushButton_Yayma)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(325, 175))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.doubleSpinBox_Lam = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_Lam.setMinimumSize(QtCore.QSize(81, 31))
        self.doubleSpinBox_Lam.setObjectName("doubleSpinBox_Lam")
        self.verticalLayout_3.addWidget(self.doubleSpinBox_Lam)
        self.checkBox_Lam = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_Lam.setObjectName("checkBox_Lam")
        self.verticalLayout_3.addWidget(self.checkBox_Lam)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.comboBox_Lam = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_Lam.setMinimumSize(QtCore.QSize(120, 34))
        self.comboBox_Lam.setObjectName("comboBox_Lam")
        self.horizontalLayout_6.addWidget(self.comboBox_Lam)
        self.pushButton_Lam_Al = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_Lam_Al.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_Lam_Al.setObjectName("pushButton_Lam_Al")
        self.horizontalLayout_6.addWidget(self.pushButton_Lam_Al)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setMaximumSize(QtCore.QSize(325, 125))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comboBox_Pump = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_Pump.setMinimumSize(QtCore.QSize(120, 34))
        self.comboBox_Pump.setObjectName("comboBox_Pump")
        self.horizontalLayout_7.addWidget(self.comboBox_Pump)
        self.pushButton_Yikama = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_Yikama.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_Yikama.setObjectName("pushButton_Yikama")
        self.horizontalLayout_7.addWidget(self.pushButton_Yikama)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_9.addWidget(self.line_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setMaximumSize(QtCore.QSize(330, 630))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_4_Methanol = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_4_Methanol.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_4_Methanol.setObjectName("pushButton_4_Methanol")
        self.horizontalLayout_8.addWidget(self.pushButton_4_Methanol)
        self.pushButton_Kurutma = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_Kurutma.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_Kurutma.setObjectName("pushButton_Kurutma")
        self.horizontalLayout_8.addWidget(self.pushButton_Kurutma)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButton_May_G = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_May_G.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_May_G.setObjectName("pushButton_May_G")
        self.horizontalLayout_16.addWidget(self.pushButton_May_G)
        self.pushButton_Yikama_after_May_G = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_Yikama_after_May_G.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_Yikama_after_May_G.setObjectName("pushButton_Yikama_after_May_G")
        self.horizontalLayout_16.addWidget(self.pushButton_Yikama_after_May_G)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_Birakma = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_Birakma.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_Birakma.setObjectName("pushButton_Birakma")
        self.horizontalLayout_15.addWidget(self.pushButton_Birakma)
        self.pushButton_Igne_Yikama = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_Igne_Yikama.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_Igne_Yikama.setObjectName("pushButton_Igne_Yikama")
        self.horizontalLayout_15.addWidget(self.pushButton_Igne_Yikama)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.pushButton_May_G_Cozelti = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_May_G_Cozelti.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_May_G_Cozelti.setObjectName("pushButton_May_G_Cozelti")
        self.horizontalLayout_20.addWidget(self.pushButton_May_G_Cozelti)
        self.pushButton_Yikama_After_Cozelti = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_Yikama_After_Cozelti.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_Yikama_After_Cozelti.setObjectName("pushButton_Yikama_After_Cozelti")
        self.horizontalLayout_20.addWidget(self.pushButton_Yikama_After_Cozelti)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_Giemsa = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_Giemsa.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_Giemsa.setObjectName("pushButton_Giemsa")
        self.horizontalLayout_14.addWidget(self.pushButton_Giemsa)
        self.pushButton_yikama_after_giemsa = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_yikama_after_giemsa.setMinimumSize(QtCore.QSize(120, 36))
        self.pushButton_yikama_after_giemsa.setObjectName("pushButton_yikama_after_giemsa")
        self.horizontalLayout_14.addWidget(self.pushButton_yikama_after_giemsa)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_9.addWidget(self.groupBox_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_9.addWidget(self.line)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setMaximumSize(QtCore.QSize(650, 630))
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_17.addWidget(self.textBrowser)
        self.horizontalLayout_9.addWidget(self.groupBox_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_4.addWidget(self.line_7)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 30))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Connection", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Port :", None, -1))
        self.pushButton_Connect.setText(QtWidgets.QApplication.translate("MainWindow", "Connect", None, -1))
        self.pushButton_Disconnect.setText(QtWidgets.QApplication.translate("MainWindow", "Disconnect", None, -1))
        self.pushButton_start.setText(QtWidgets.QApplication.translate("MainWindow", "START", None, -1))
        self.pushButton_disable_motors.setText(QtWidgets.QApplication.translate("MainWindow", "Motorları Durdur", None, -1))
        self.pushButton_Reset.setText(QtWidgets.QApplication.translate("MainWindow", "Reset", None, -1))
        self.pushButton_Stop.setText(QtWidgets.QApplication.translate("MainWindow", "ACİL STOP", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Yayma", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Yayma Hızı :", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Yayma Açısı :", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Rampa :", None, -1))
        self.checkBox_Yayma.setText(QtWidgets.QApplication.translate("MainWindow", "Elle girdiyi aktif et", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Miktar :", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Tüp :", None, -1))
        self.pushButton_Yayma.setText(QtWidgets.QApplication.translate("MainWindow", "Kanı Yay", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Lam", None, -1))
        self.checkBox_Lam.setText(QtWidgets.QApplication.translate("MainWindow", "Elle girdiyi aktif et", None, -1))
        self.pushButton_Lam_Al.setText(QtWidgets.QApplication.translate("MainWindow", "Lam Bırak", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Pump Yıkama", None, -1))
        self.pushButton_Yikama.setText(QtWidgets.QApplication.translate("MainWindow", "Yıkama", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "Boyama", None, -1))
        self.pushButton_4_Methanol.setText(QtWidgets.QApplication.translate("MainWindow", "Methanol", None, -1))
        self.pushButton_Kurutma.setText(QtWidgets.QApplication.translate("MainWindow", "Kurutma", None, -1))
        self.pushButton_May_G.setText(QtWidgets.QApplication.translate("MainWindow", "May Grunwald", None, -1))
        self.pushButton_Yikama_after_May_G.setText(QtWidgets.QApplication.translate("MainWindow", "Yıkama 1", None, -1))
        self.pushButton_Birakma.setText(QtWidgets.QApplication.translate("MainWindow", "Bırakma", None, -1))
        self.pushButton_Igne_Yikama.setText(QtWidgets.QApplication.translate("MainWindow", "İğne Yıkama", None, -1))
        self.pushButton_May_G_Cozelti.setText(QtWidgets.QApplication.translate("MainWindow", "May Grunwald\n"
" Çözeltisi", None, -1))
        self.pushButton_Yikama_After_Cozelti.setText(QtWidgets.QApplication.translate("MainWindow", "Yıkama 2", None, -1))
        self.pushButton_Giemsa.setText(QtWidgets.QApplication.translate("MainWindow", "Giemsa", None, -1))
        self.pushButton_yikama_after_giemsa.setText(QtWidgets.QApplication.translate("MainWindow", "Yıkama 3", None, -1))
        self.groupBox_6.setTitle(QtWidgets.QApplication.translate("MainWindow", "Bilgilendirme", None, -1))
        self.actionNew.setText(QtWidgets.QApplication.translate("MainWindow", "New", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))

import resources.resource_rc
