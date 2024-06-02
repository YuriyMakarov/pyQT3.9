from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu


import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Игрули")
        self.setGeometry(300, 250, 250, 200)
        self.setWindowIcon(QIcon('icons/mainIcon.ico'))

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.create_menu_bar()

    def create_menu_bar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Игры", self)
        self.menuBar.addMenu(fileMenu)

        open_file = fileMenu.addMenu("&Кликер")
        save_menu = fileMenu.addMenu("&Сапер")

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()

