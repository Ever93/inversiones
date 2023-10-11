import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from db import conectar
import sqlite3
from PyQt5.QtCore import QDate
import datetime

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal
        self.setObjectName("MainWindow")
        self.resize(667, 264)

        # Crear el widget central
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        # Crear widgets
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
        self.ButtonRegis.clicked.connect(self.insertar_datos)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 200, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        # Configurar menú y barra de estado
        self.menubar = self.menuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 21))
        self.menubar.setObjectName("menubar")

        self.statusbar = self.statusBar()
        self.statusbar.setObjectName("statusbar")

        # Llamar a la función para configurar traducciones
        self.retranslateUi()
    def insertar_datos(self):
        fecha = self.lineEditFecha.text()  # Obtenemos la fecha en formato de texto
        detalle = self.lineEditDetalle.text()
        monto_egreso = float(self.lineEditMonto.text())

        if fecha and detalle and monto_egreso:
            try:
                conexion, cursor = conectar()  # Utiliza la función conectar

                # Sentencia SQL para insertar datos en la tabla "egreso"
                cursor.execute("INSERT INTO egreso (fecha, detalle, monto) VALUES (?, ?, ?)", (fecha, detalle, monto_egreso))
                # Obtener el saldo actual desde la tabla "saldo"
                cursor.execute("SELECT monto FROM saldo WHERE id=1")
                saldo_actual = cursor.fetchone()
                if saldo_actual:
                    saldo_monto = saldo_actual[0]
                # Calcular el nuevo saldo restando el monto del egreso
                    nuevo_saldo = saldo_monto - monto_egreso
                # Actualizar el saldo en la tabla "saldo"
                    
                    cursor.execute("UPDATE saldo SET fecha = ?, monto = ? WHERE id = 1", (fecha, nuevo_saldo))
                
                    conexion.commit()  # Confirmar la transacción
                    conexion.close()   # Cerrar la conexión

                # Limpia los campos después de la inserción
                    self.lineEditFecha.clear()
                    self.lineEditDetalle.clear()
                    self.lineEditMonto.clear()
                # Mostrar un mensaje de confirmación
                    QtWidgets.QMessageBox.information(self, "Éxito", "Los datos han sido registrados correctamente.")
                else:
                    QtWidgets.QMessageBox.warning(self, "Advertencia", "No se encontró un registro de saldo.")
            except sqlite3.Error as error:
                QtWidgets.QMessageBox.critical(self, "Error", f"Error al insertar en la base de datos: {error}")
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Todos los campos son obligatorios.")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labeltitulo.setText(_translate("MainWindow", "Registre Egreso"))
        self.labelFecha.setText(_translate("MainWindow", "Fecha:"))
        self.labelDetalle.setText(_translate("MainWindow", "Detalle:"))
        self.labelMonto.setText(_translate("MainWindow", "Monto:"))
        self.ButtonRegis.setText(_translate("MainWindow", "Registrar"))
        self.pushButton_2.setText(_translate("MainWindow", "Editar"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())