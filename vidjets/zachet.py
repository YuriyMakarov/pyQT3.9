from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget

import sys

from PyQt5.uic.properties import QtCore


class MyWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.setWindowTitle("Зачет")  # Заголовок программы

        self.btn_light = QtWidgets.QPushButton('Темная')
        self.btn_light.clicked.connect(self.tema_dark)

        self.btn_dark = QtWidgets.QPushButton('Светлая')
        self.btn_dark.clicked.connect(self.tema_light)

        self.text_write_1 = QtWidgets.QLineEdit()
        self.text_write_2 = QtWidgets.QLineEdit()

        self.btn_plus = QtWidgets.QPushButton("+")
        self.btn_minus = QtWidgets.QPushButton("-")
        self.btn_umnoch = QtWidgets.QPushButton("*")
        self.btn_delete = QtWidgets.QPushButton("/")

        self.btn_plus.clicked.connect(self.plus)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_umnoch.clicked.connect(self.umnoch)
        self.btn_delete.clicked.connect(self.delete)

        self.text_read = QtWidgets.QLabel("Результат")

        grid = QGridLayout()

        grid.addWidget(self.btn_light, 0, 0, 1, 2)
        grid.addWidget(self.btn_dark, 0, 2, 1, 2)
        grid.addWidget(self.text_write_1, 1, 0, 1, 2)
        grid.addWidget(self.text_write_2, 1, 2, 1, 2)
        grid.addWidget(self.btn_plus, 2, 0)
        grid.addWidget(self.btn_minus, 2, 1)
        grid.addWidget(self.btn_umnoch, 2, 2)
        grid.addWidget(self.btn_delete, 2, 3)
        grid.addWidget(self.text_read, 3, 0)

        container = QWidget()
        container.setLayout(grid)

        self.setCentralWidget(container)

    def tema_dark(self):
        self.setStyleSheet("background-color: black; color: orange;")

    def tema_light(self):
        self.setStyleSheet("background-color: none; color: none; }")

    def plus(self):
        number1 = float(self.text_write_1.text())
        number2 = float(self.text_write_2.text())
        self.text_read.setText(str(number1 + number2))

    def minus(self):
        number1 = float(self.text_write_1.text())
        number2 = float(self.text_write_2.text())
        self.text_read.setText(str(number1 - number2))

    def umnoch(self):
        number1 = float(self.text_write_1.text())
        number2 = float(self.text_write_2.text())
        self.text_read.setText(str(number1 * number2))

    def delete(self):
        number1 = float(self.text_write_1.text())
        number2 = float(self.text_write_2.text())
        self.text_read.setText(str(number1 / number2))


def application():
    app = QApplication(sys.argv)
    window = MyWindow()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()

