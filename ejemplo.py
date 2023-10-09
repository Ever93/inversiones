import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QTreeWidget, QTreeWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Scroll en TreeView')
        self.setGeometry(100, 100, 800, 600)

        frame1 = QFrame(self)
        frame1.setGeometry(10, 10, 780, 580)

        tree_label = QLabel('Elementos', frame1)
        tree_label.setGeometry(10, 10, 100, 30)

        self.tree = QTreeWidget(frame1)
        self.tree.setGeometry(10, 40, 760, 530)
        self.tree.setHeaderLabels(['Columna 1', 'Columna 2'])

        # Agregar 50 elementos de ejemplo al árbol
        for i in range(50):
            item = QTreeWidgetItem(self.tree, ['Item {}'.format(i), 'Valor {}'.format(i)])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

