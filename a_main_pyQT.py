from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QAction, QMenuBar, QMenu

import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.init_UI()
        self.create_menu_bar()

    def init_UI(self):
        self.setWindowTitle("Виджеты")
        self.setGeometry(300, 250, 250, 200)
        self.setWindowIcon(QIcon('icons/mainIcon.ico'))

        self.btn1 = QPushButton("1", self)
        self.btn1.move(10, 30)
        #self.btn1.clicked.connect(lambda: self.addNumberButton(int(self.btn1.text())))
        self.btn1.clicked.connect(self.addNumberButton)
        self.btn1.clicked.connect(self.setColorBtn)

        self.btn2 = QPushButton("2", self)
        self.btn2.move(10, 80)
        #self.btn2.clicked.connect(lambda: self.addNumberButton(int(self.btn2.text())))
        self.btn2.clicked.connect(self.addNumberButton)
        self.btn2.clicked.connect(self.setColorBtn)

        self.label1 = QLabel(self)
        self.label1.move(10, 110)
        self.label1.setText("0")

    def create_menu_bar(self):
        self.mainMenu = self.menuBar()

        self.fileMenu = self.mainMenu.addMenu('&Файл')

        self.exitAction = QAction(QIcon('icons/mainIcon.ico'), "Выход", self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.triggered.connect(quit)

        self.fileMenu.addAction(self.exitAction)

        self.styleMenu = self.mainMenu.addMenu('&Стили')

        self.colors_background_menu = self.styleMenu.addMenu("&Цвет фона")
        self.colors_text_menu = self.styleMenu.addMenu("&Цвет шрифта")

        self.color_red = QAction("Красный", self)
        self.color_red.setShortcut("Ctrl+1")
        self.color_red.triggered.connect(lambda: self.setStyleColor("red"))

        self.color_blue = QAction("Синий", self)
        self.color_blue.setShortcut("Ctrl+2")
        self.color_blue.triggered.connect(lambda: self.setStyleColor("blue"))

        self.color_green = QAction("Зеленый", self)
        self.color_green.setShortcut("Ctrl+3")
        self.color_green.triggered.connect(lambda: self.setStyleColor("green"))

        self.colors_text_menu.addAction(self.color_red)
        self.colors_text_menu.addAction(self.color_blue)
        self.colors_text_menu.addAction(self.color_green)

    def setStyleColor(self, name_color):
        self.setStyleSheet(f"color: {name_color}")

    def addNumberButton(self, numberButton: int) -> None:
        #self.label1.setText(str(int(self.label1.text()) + numberButton))
        self.label1.setText(str(int(self.label1.text()) + int(self.sender().text())))

    def setColorBtn(self, checked):
        if not checked:
            self.sender().setStyleSheet("background-color: #4CAF50; color: white")
            self.sender().setCheckable(True)
        else:
            self.sender().setCheckable(False)
            self.sender().setStyleSheet("background-color: #4CAF50; color: red")


def application():
    app = QApplication(sys.argv)  # sys.argv - хранит настройки, связанный с компьютером для запуска
    myWindow = MyWindow()  # Создаем окно

    myWindow.show()  # Показ окна
    sys.exit(app.exec_())  # Корректные параметры выхода из приложения


if __name__ == "__main__":  # Запуск приложения
    application()
