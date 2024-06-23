from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QLabel, QWidget

import sys


class QtWidget:
    pass


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(400, 400, 500, 300)
        self.setWindowTitle("Приложуха")
        self.setWindowIcon(QIcon('../icons/mainIcon.ico'))

        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/', '4', '5', '6', '*',
                 '1', '2', '3', '-', '0', '.', '=', '+']
        positions = []

        for i in range(5):
            for j in range(4):
                positions.append((i, j))

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QtWidgets.QPushButton(name)
            grid.addWidget(button, *position)

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

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
#
# class MyWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         layout = QHBoxLayout()
#
#         layout.addWidget(QPushButton('Button 1'))
#         layout.addWidget(QPushButton('Button 2'))
#         layout.addWidget(QPushButton('Button 3'))
#
#         self.setLayout(layout)
#
#
# def application():
#     app = QApplication(sys.argv)
#     window = MyWidget()
#
#     window.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     application()
