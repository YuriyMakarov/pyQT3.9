from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QLabel, QWidget, QLineEdit, \
    QTextEdit, QGridLayout

import sys


class QtWidget:
    pass


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("Приложуха")
        self.setWindowIcon(QIcon('icons/mainIcon.ico'))

        btn0 = QtWidgets.QPushButton('1')
        btn1 = QtWidgets.QPushButton('2')
        btn2 = QtWidgets.QPushButton('3')
        btn3 = QtWidgets.QPushButton('4')
        btn4 = QtWidgets.QPushButton('5')

        grid = QGridLayout()
        # grid.setSpacing(20)

        grid.addWidget(btn0, 0, 0)
        grid.addWidget(btn1, 1, 0, 1, 3)
        grid.addWidget(btn2, 2, 0)
        grid.addWidget(btn3, 0, 1)
        grid.addWidget(btn4, 0, 2)

        container = QWidget()
        container.setLayout(grid)

        self.setCentralWidget(container)


def application():
    app = QApplication(sys.argv)
    window = MyWindow()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()