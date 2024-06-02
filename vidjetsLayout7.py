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

        title_label = QtWidgets.QLabel("Title")
        author_label = QtWidgets.QLabel("Author")
        review_label = QtWidgets.QLabel("Review")

        title_line = QtWidgets.QLineEdit()
        author_line = QtWidgets.QLineEdit()
        review_line = QtWidgets.QLineEdit()

        grid = QGridLayout()

        grid.addWidget(title_label, 0, 0)
        grid.addWidget(author_label, 1, 0)
        grid.addWidget(review_label, 2, 0)
        grid.addWidget(title_line, 0, 1)
        grid.addWidget(author_line, 1, 1)
        grid.addWidget(review_line, 2, 1)

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