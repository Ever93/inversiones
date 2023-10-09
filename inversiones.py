import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.resize(833, 640)
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(320, 20, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        
        self.capinicial = QtWidgets.QLabel(self.centralwidget)
        self.capinicial.setGeometry(QtCore.QRect(20, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.capinicial.setFont(font)
        self.capinicial.setTextFormat(QtCore.Qt.PlainText)
        self.capinicial.setObjectName("capinicial")
        
        self.saldo = QtWidgets.QLabel(self.centralwidget)
        self.saldo.setGeometry(QtCore.QRect(20, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.saldo.setFont(font)
        self.saldo.setObjectName("saldo")
        
        self.fechaCI = QtWidgets.QLabel(self.centralwidget)
        self.fechaCI.setGeometry(QtCore.QRect(520, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fechaCI.setFont(font)
        self.fechaCI.setObjectName("fechaCI")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.cargaCI = QtWidgets.QPushButton(self.centralwidget)
        self.cargaCI.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.cargaCI.setObjectName("cargaCI")
        
        self.ingreso = QtWidgets.QPushButton(self.centralwidget)
        self.ingreso.setGeometry(QtCore.QRect(150, 160, 75, 23))
        self.ingreso.setObjectName("ingreso")
        
        self.egreso = QtWidgets.QPushButton(self.centralwidget)
        self.egreso.setGeometry(QtCore.QRect(610, 160, 75, 23))
        self.egreso.setObjectName("egreso")
        
        self.treeViewIngreso = QtWidgets.QTreeView(self.centralwidget)
        self.treeViewIngreso.setGeometry(QtCore.QRect(10, 200, 391, 391))
        self.treeViewIngreso.setObjectName("treeViewIngreso")
        
        self.treeViewEgreso = QtWidgets.QTreeView(self.centralwidget)
        self.treeViewEgreso.setGeometry(QtCore.QRect(430, 200, 391, 391))
        self.treeViewEgreso.setObjectName("treeViewEgreso")
        
        self.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo.setText(_translate("MainWindow", "Control de Inversiones"))
        self.capinicial.setText(_translate("MainWindow", "Capital Inicial:"))
        self.saldo.setText(_translate("MainWindow", "Saldo:"))
        self.fechaCI.setText(_translate("MainWindow", "Fecha:"))
        self.label_4.setText(_translate("MainWindow", "Fecha:"))
        self.cargaCI.setText(_translate("MainWindow", "Cargar"))
        self.ingreso.setText(_translate("MainWindow", "Ingreso"))
        self.egreso.setText(_translate("MainWindow", "Egreso"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
