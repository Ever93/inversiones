from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal


class CapitalInicialWindow(QtWidgets.QMainWindow):
    closed = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conecta el botón para cerrar la ventana con el método de cierre personalizado
        self.ui.ButtonDelet.clicked.connect(self.cerrar_ventana)
    def closeEvent(self, event):
        # Emite la señal cuando la ventana se cierra
        self.closed.emit()

    def cerrar_ventana(self):
        self.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 295)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.textMonto = QtWidgets.QTextEdit(self.centralwidget)
        self.textFecha = QtWidgets.QTextEdit(self.centralwidget)
        self.labelMonto = QtWidgets.QLabel(self.centralwidget)
        self.labelFecha = QtWidgets.QLabel(self.centralwidget)
        self.ButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonEdit = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDelet = QtWidgets.QPushButton(self.centralwidget)

        self.label.setGeometry(QtCore.QRect(200, 20, 221, 31))
        self.textMonto.setGeometry(QtCore.QRect(170, 60, 251, 31))
        self.textFecha.setGeometry(QtCore.QRect(170, 100, 251, 31))
        self.labelMonto.setGeometry(QtCore.QRect(100, 60, 61, 31))
        self.labelFecha.setGeometry(QtCore.QRect(100, 100, 61, 31))
        self.ButtonSave.setGeometry(QtCore.QRect(170, 140, 75, 23))
        self.ButtonEdit.setGeometry(QtCore.QRect(260, 140, 75, 23))
        self.ButtonDelet.setGeometry(QtCore.QRect(350, 140, 75, 23))
        
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        
        font.setPointSize(12)
        self.labelMonto.setFont(font)
        self.labelFecha.setFont(font)
        
        self.label.setObjectName("label")
        self.textMonto.setObjectName("textMonto")
        self.textFecha.setObjectName("textFecha")
        self.labelMonto.setObjectName("labelMonto")
        self.labelFecha.setObjectName("labelFecha")
        self.ButtonSave.setObjectName("ButtonSave")
        self.ButtonEdit.setObjectName("ButtonEdit")
        self.ButtonDelet.setObjectName("ButtonDelet")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cargar Capital Inicial"))
        self.labelMonto.setText(_translate("MainWindow", "Monto:"))
        self.labelFecha.setText(_translate("MainWindow", "Fecha:"))
        self.ButtonSave.setText(_translate("MainWindow", "Guardar"))
        self.ButtonEdit.setText(_translate("MainWindow", "Editar"))
        self.ButtonDelet.setText(_translate("MainWindow", "Eliminar"))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.capital_inicial_window = None  # Para mantener un seguimiento de la ventana de capital inicial

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())