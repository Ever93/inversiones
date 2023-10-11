from PyQt5 import QtCore, QtGui, QtWidgets
from db import conectar
import sqlite3
import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(310, 0, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
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
        self.fechaSaldo = QtWidgets.QLabel(self.centralwidget)
        self.fechaSaldo.setGeometry(QtCore.QRect(520, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fechaSaldo.setFont(font)
        self.fechaSaldo.setObjectName("fechaSaldo")
        self.cargaCI = QtWidgets.QPushButton(self.centralwidget)
        self.cargaCI.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.cargaCI.setObjectName("cargaCI")
        self.cargaCI.clicked.connect(self.abrir_ventana_carga_CI)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Método para abrir la ventana modal de carga de Capital Inicial
    def abrir_ventana_carga_CI(self):
        self.ventana_carga_CI = QtWidgets.QDialog()
        self.ventana_carga_CI.setWindowTitle("Carga de Capital Inicial")

        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Ingrese el Capital Inicial:")
        layout.addWidget(label)

        self.textEditCI = QtWidgets.QLineEdit()
        self.textEditCI.setValidator(QtGui.QDoubleValidator())  # Asegura que solo se ingresen números
        layout.addWidget(self.textEditCI)

        button_ok = QtWidgets.QPushButton("OK")
        button_ok.clicked.connect(self.guardar_CI)
        layout.addWidget(button_ok)

        self.ventana_carga_CI.setLayout(layout)
        self.ventana_carga_CI.exec_()

    # Método para guardar el Capital Inicial
    def guardar_CI(self):
        ci_text = self.textEditCI.text()
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn, c = conectar()

        try:
            ci = float(ci_text)  # Intenta convertir el texto a un número
        except ValueError:
            QtWidgets.QMessageBox.critical(None, "Error", "El dato debe ser un número")
            return

        try:
            # Verificar si ya existe un registro con id 1 en 'capitalinicial'
            c.execute("SELECT COUNT(*) FROM capitalinicial WHERE id = 1")
            count = c.fetchone()[0]

            if count > 0:
                # Actualizar el registro existente
                c.execute("UPDATE capitalinicial SET fecha = ?, monto = ? WHERE id = 1", (fecha, ci))
            else:
                # Insertar un nuevo registro
                c.execute("INSERT INTO capitalinicial (id, fecha, monto) VALUES (?, ?, ?)", (1, fecha, ci))

            # Actualizar el registro con id 1 en 'saldo'
            c.execute("UPDATE saldo SET fecha = ?, monto = ? WHERE id = 1", (fecha, ci))

            conn.commit()
            conn.close()

            self.ventana_carga_CI.accept()

            QtWidgets.QMessageBox.information(None, "Éxito", "Guardado con éxito")
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"Error al guardar: {str(e)}")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo.setText(_translate("MainWindow", "Control de Inversiones"))
        self.capinicial.setText(_translate("MainWindow", "Capital Inicial:"))
        self.saldo.setText(_translate("MainWindow", "Saldo:"))
        self.fechaCI.setText(_translate("MainWindow", "Fecha:"))
        self.fechaSaldo.setText(_translate("MainWindow", "Fecha:"))
        self.cargaCI.setText(_translate("MainWindow", "Cargar"))
        self.ingreso.setText(_translate("MainWindow", "Ingreso"))
        self.egreso.setText(_translate("MainWindow", "Egreso"))
        self.deletEgreso.setText(_translate("MainWindow", "Eliminar"))
        self.deletIngreso.setText(_translate("MainWindow", "Eliminar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
