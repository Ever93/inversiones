# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingreso.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 264)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labeltitulo = QtWidgets.QLabel(self.centralwidget)
        self.labeltitulo.setGeometry(QtCore.QRect(250, 0, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labeltitulo.setFont(font)
        self.labeltitulo.setObjectName("labeltitulo")
        self.lineEditFecha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFecha.setGeometry(QtCore.QRect(70, 60, 113, 20))
        self.lineEditFecha.setObjectName("lineEditFecha")
        self.lineEditDetalle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDetalle.setGeometry(QtCore.QRect(80, 90, 571, 61))
        self.lineEditDetalle.setObjectName("lineEditDetalle")
        self.lineEditMonto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMonto.setGeometry(QtCore.QRect(70, 160, 113, 21))
        self.lineEditMonto.setObjectName("lineEditMonto")
        self.labelFecha = QtWidgets.QLabel(self.centralwidget)
        self.labelFecha.setGeometry(QtCore.QRect(10, 60, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelFecha.setFont(font)
        self.labelFecha.setObjectName("labelFecha")
        self.labelDetalle = QtWidgets.QLabel(self.centralwidget)
        self.labelDetalle.setGeometry(QtCore.QRect(10, 100, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelDetalle.setFont(font)
        self.labelDetalle.setObjectName("labelDetalle")
        self.labelMonto = QtWidgets.QLabel(self.centralwidget)
        self.labelMonto.setGeometry(QtCore.QRect(10, 160, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelMonto.setFont(font)
        self.labelMonto.setObjectName("labelMonto")
        self.ButtonRegis = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonRegis.setGeometry(QtCore.QRect(70, 200, 75, 23))
        self.ButtonRegis.setObjectName("ButtonRegis")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 200, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labeltitulo.setText(_translate("MainWindow", "Registre Ingreso"))
        self.labelFecha.setText(_translate("MainWindow", "Fecha:"))
        self.labelDetalle.setText(_translate("MainWindow", "Detalle:"))
        self.labelMonto.setText(_translate("MainWindow", "Monto:"))
        self.ButtonRegis.setText(_translate("MainWindow", "Registrar"))
        self.pushButton_2.setText(_translate("MainWindow", "Editar"))
