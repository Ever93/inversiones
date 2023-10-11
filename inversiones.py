import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QVBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from db import conectar
import sqlite3
from capitalinicial import Ui_MainWindow as Ui_CapitalInicial, CapitalInicialWindow
from egreso import MyMainWindow
from PyQt5.QtCore import QTimer
import threading
import time
from PyQt5.QtCore import QObject, pyqtSignal

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

class CapitalInicialWindow(QtWidgets.QMainWindow):
    closed = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_CapitalInicial()
        self.ui.setupUi(self)

        # Conecta el botón para cerrar la ventana con el método de cierre personalizado
        self.ui.ButtonDelet.clicked.connect(self.cerrar_ventana)
    def closeEvent(self, event):
        # Emite la señal cuando la ventana se cierra
        self.closed.emit()

    def cerrar_ventana(self):
        self.close()
        
class MainWindow(QtWidgets.QMainWindow):
    saldo_actualizado = QtCore.pyqtSignal(float, str)
    def __init__(self):
        super().__init__()
        self.capital_inicial_window = None  # Para mantener un seguimiento de la ventana de capital inicial
        self.egreso_window = None
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
        self.cargaCI.clicked.connect(self.abrir_capital_inicial)
        
        self.ingreso = QtWidgets.QPushButton(self.centralwidget)
        self.ingreso.setGeometry(QtCore.QRect(150, 160, 75, 23))
        self.ingreso.setObjectName("ingreso")
        
        self.egreso = QtWidgets.QPushButton(self.centralwidget)
        self.egreso.setGeometry(QtCore.QRect(610, 160, 75, 23))
        self.egreso.setObjectName("egreso")
        self.egreso.clicked.connect(self.abrir_egreso)
        
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
        self.cargar_datos_egreso()
    def cargar_datos_egreso(self):
        try:
            conexion, cursor = conectar()
            cursor.execute("SELECT fecha, detalle, monto FROM egreso")
            data = cursor.fetchall()

            for row in data:
                fecha, detalle, monto = row
                item_fecha = QtGui.QStandardItem(fecha)
                item_detalle = QtGui.QStandardItem(detalle)
                item_monto = QtGui.QStandardItem(str(monto))
                self.modelEgreso.appendRow([item_fecha, item_detalle, item_monto])

            conexion.close()
        except sqlite3.Error as error:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error al cargar datos desde la base de datos: {error}")

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
        # Crear y empezar un hilo para actualizar el saldo periódicamente
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_saldo_periodicamente)
        self.timer.start(1000)  # Actualiza cada 10 segundos
    def abrir_egreso(self):
        if self.egreso_window is None:
            self.egreso_window = MyMainWindow()
            self.egreso_window.destroyed.connect(self.activar_ventana_principal)

        self.egreso_window.show()

    def activar_ventana_egreso(self):
        self.setEnabled(True)
        self.egreso_window = None 
    def abrir_capital_inicial(self):
        if self.capital_inicial_window is None:
        # Crea una instancia de la ventana de capital inicial
            self.capital_inicial_window = CapitalInicialWindow()
        # Deshabilita la ventana principal
            self.setEnabled(False)
        # Conecta la señal de cierre de la ventana de capital inicial
            self.capital_inicial_window.closed.connect(self.activar_ventana_principal)
        # Muestra la ventana de capital inicial
            self.capital_inicial_window.show()
    def activar_ventana_principal(self):
        # Habilita nuevamente la ventana principal
        self.setEnabled(True)
        self.capital_inicial_window = None
            
    def cargar_saldo_desde_db(self):
        try:
        #Usar la función conectar del archivo conexion_db.py
            conn, cursor = conectar()
        # Realizar una consulta SQL para obtener el saldo
            cursor.execute("SELECT monto, fecha FROM saldo ORDER BY id DESC LIMIT 1")
            resultado = cursor.fetchone()
        # Si se encontró un resultado, mostrarlo en el QTextBrowser
            if resultado:
                monto, fecha = resultado
                self.textSaldo.setPlainText(str(monto))
                self.textFechaSaldo.setPlainText(str(fecha))
                font = QtGui.QFont()
                font.setPointSize(12)  # Tamaño de fuente deseado
                self.textSaldo.setFont(font)
                self.textFechaSaldo.setFont(font)
        # Cerrar la conexión a la base de datos
            conn.close()
        except sqlite3.Error as e:
            print("Error al acceder a la base de datos:", e)
    def actualizar_saldo_periodicamente(self):
        try:
            conn, cursor = conectar()
            cursor.execute("SELECT monto, fecha FROM saldo WHERE id = 1")
            resultado = cursor.fetchone()

            if resultado:
                saldo_actual, fecha_actual = resultado

            # Actualiza la interfaz de usuario con el saldo
                self.textSaldo.setPlainText(str(saldo_actual))
                self.textFechaSaldo.setPlainText(fecha_actual)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.textSaldo.setFont(font)

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