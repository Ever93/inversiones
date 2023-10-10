import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QVBoxLayout
import sqlite3

class MontoInputDialog(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.monto_label = QtWidgets.QLabel("Monto:")
        self.monto_input = QtWidgets.QLineEdit()
        self.ok_button = QtWidgets.QPushButton("OK")

        layout.addWidget(self.monto_label)
        layout.addWidget(self.monto_input)
        layout.addWidget(self.ok_button)

        self.ok_button.clicked.connect(self.accept)

        self.setLayout(layout)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setObjectName("MainWindow")
        self.resize(833, 654)
        
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
        self.label_4.setObjectName("fechaSaldo")
        
        self.cargaCI = QtWidgets.QPushButton(self.centralwidget)
        self.cargaCI.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.cargaCI.setObjectName("cargaCI")
        self.cargaCI.clicked.connect(self.abrir_dialogo)
        
        self.ingreso = QtWidgets.QPushButton(self.centralwidget)
        self.ingreso.setGeometry(QtCore.QRect(150, 160, 75, 23))
        self.ingreso.setObjectName("ingreso")
        
        self.egreso = QtWidgets.QPushButton(self.centralwidget)
        self.egreso.setGeometry(QtCore.QRect(610, 160, 75, 23))
        self.egreso.setObjectName("egreso")
        
        self.treeViewIngreso = QtWidgets.QTreeView(self.centralwidget)
        self.treeViewIngreso.setGeometry(QtCore.QRect(10, 200, 391, 391))
        self.treeViewIngreso.setObjectName("treeViewIngreso")
        
        # Crear el modelo de datos para el QTreeView
        self.modelIngreso = QtGui.QStandardItemModel()
        self.treeViewIngreso.setModel(self.modelIngreso)
        # Agregar encabezados de columna
        self.modelIngreso.setHorizontalHeaderLabels(["Fecha", "Detalle", "Monto"])
        self.treeViewIngreso.setColumnWidth(1, 200)
        
        self.treeViewEgreso = QtWidgets.QTreeView(self.centralwidget)
        self.treeViewEgreso.setGeometry(QtCore.QRect(430, 200, 391, 391))
        self.treeViewEgreso.setObjectName("treeViewEgreso")
        # Crear el modelo de datos para el QTreeView
        self.modelEgreso = QtGui.QStandardItemModel()
        self.treeViewEgreso.setModel(self.modelEgreso)
        # Agregar encabezados de columna
        self.modelEgreso.setHorizontalHeaderLabels(["Fecha", "Detalle", "Monto"])
        self.treeViewEgreso.setColumnWidth(1, 200)
        self.textCI = QtWidgets.QTextBrowser(self.centralwidget)
        self.textCI.setGeometry(QtCore.QRect(140, 50, 211, 31))
        self.textCI.setObjectName("textCI")
        self.textSaldo = QtWidgets.QTextBrowser(self.centralwidget)
        self.textSaldo.setGeometry(QtCore.QRect(70, 110, 211, 31))
        self.textSaldo.setObjectName("textSaldo")
        self.textFechaCI = QtWidgets.QTextBrowser(self.centralwidget)
        self.textFechaCI.setGeometry(QtCore.QRect(580, 50, 211, 31))
        self.textFechaCI.setObjectName("textFechaCI")
        self.textFechaSaldo = QtWidgets.QTextBrowser(self.centralwidget)
        self.textFechaSaldo.setGeometry(QtCore.QRect(580, 110, 211, 31))
        self.textFechaSaldo.setObjectName("textFechaSaldo")
        self.deletEgreso = QtWidgets.QPushButton(self.centralwidget)
        self.deletEgreso.setGeometry(QtCore.QRect(750, 600, 75, 23))
        self.deletEgreso.setObjectName("deletEgreso")
        self.deletIngreso = QtWidgets.QPushButton(self.centralwidget)
        self.deletIngreso.setGeometry(QtCore.QRect(330, 600, 75, 23))
        self.deletIngreso.setObjectName("deletIngreso")
        self.editIngreso = QtWidgets.QPushButton(self.centralwidget)
        self.editIngreso.setGeometry(QtCore.QRect(10, 600, 75, 23))
        self.editIngreso.setObjectName("editIngreso")
        self.editEgreso = QtWidgets.QPushButton(self.centralwidget)
        self.editEgreso.setGeometry(QtCore.QRect(430, 600, 75, 23))
        self.editEgreso.setObjectName("editEgreso")
        
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
        # Llamar al método para cargar el saldo desde la base de datos
        self.cargar_saldo_desde_db()
    def abrir_dialogo(self):
        dialogo = MontoInputDialog()
        if dialogo.exec_() == QDialog.Accepted:
            monto = dialogo.monto_input.text()
            # Actualiza el texto de self.capinicial con el monto ingresado
            self.textCI.setPlainText(monto)
            font = QtGui.QFont()
            font.setPointSize(12)  # Tamaño de fuente deseado
            self.textCI.setFont(font)
            
    def cargar_saldo_desde_db(self):
        try:
        # Conectarse a la base de datos
            conn = sqlite3.connect("inversiones.db")
            cursor = conn.cursor()

        # Realizar una consulta SQL para obtener el saldo
            cursor.execute("SELECT monto FROM saldo ORDER BY id DESC LIMIT 1")
            resultado = cursor.fetchone()

        # Si se encontró un resultado, mostrarlo en el QTextBrowser
            if resultado:
                monto = resultado[0]
                self.textSaldo.setPlainText(str(monto))
                font = QtGui.QFont()
                font.setPointSize(12)  # Tamaño de fuente deseado
                self.textSaldo.setFont(font)

        # Cerrar la conexión a la base de datos
            conn.close()
        except sqlite3.Error as e:
            print("Error al acceder a la base de datos:", e)
    
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
        self.deletEgreso.setText(_translate("MainWindow", "Eliminar"))
        self.deletIngreso.setText(_translate("MainWindow", "Eliminar"))
        self.editIngreso.setText(_translate("MainWindow", "Editar"))
        self.editEgreso.setText(_translate("MainWindow", "Editar"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())