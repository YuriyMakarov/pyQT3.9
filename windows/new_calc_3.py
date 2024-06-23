from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QLabel, QStackedWidget, QAction, \
    QWidget

import sys


class BarWindow(QMainWindow):
    def __init__(self):
        super(BarWindow, self).__init__()

        self.move(700, 500)
        self.setWindowTitle("Приложуха")
        self.setWindowIcon(QIcon('../icons/mainIcon.ico'))
        self.create_menu_bar()

    def create_menu_bar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        self.fileMenu = QMenu("&Режимы", self)
        self.colorMenu = QMenu("&Тема", self)
        self.menuBar.addMenu(self.fileMenu)
        self.menuBar.addMenu(self.colorMenu)

        self.black_color = QAction("Темная", self)
        self.black_color.triggered.connect(self.set_color)
        self.light_color = QAction("Светлая", self)
        self.light_color.triggered.connect(self.set_color)


        self.calc = QAction("Калькулятор", self)
        self.calc.triggered.connect(lambda: self.open_widget(CalcWidget))
        self.clicker = QAction("Кликер", self)
        self.clicker.triggered.connect(lambda: self.open_widget(ClickerWidget))

        self.fileMenu.addAction(self.calc)
        self.fileMenu.addAction(self.clicker)

        self.colorMenu.addAction(self.black_color)
        self.colorMenu.addAction(self.light_color)

    def set_color(self):
        sender = self.sender()
        if sender.text() == "Темная":
            self.setStyleSheet("background-color: black; color: orange;")
        elif sender.text() == "Светлая":
            self.setStyleSheet("background-color: none; color: none; }")

    def open_widget(self, widget):
        self.calc_widget = widget()
        self.setCentralWidget(self.calc_widget)


class CalcWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout()

        self.monitor1 = QtWidgets.QLabel(self)
        self.monitor1.setText("0")
        layout.addWidget(self.monitor1)

        buttons = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            "0", "=", "*", "/",
            "+", "-"
        ]

        for button_text in buttons:
            button = QtWidgets.QPushButton(button_text, self)
            button.clicked.connect(lambda _, text=button_text: self.add_digit(text))
            layout.addWidget(button)

        self.setLayout(layout)

    def add_digit(self, num):
        text = self.monitor1.text()
        if text == "0":
            self.monitor1.setText(num)
        else:
            self.monitor1.setText(text + num)

    def add_sign(self, sign):
        text = self.monitor1.text()
        if "+" not in text and "-" not in text and "*" not in text and "/" not in text:
            self.monitor1.setText(text + sign)

    def calc(self):
        text = self.monitor1.text()
        if "+" in text:
            numbers = text.split("+")
            num1 = float(numbers[0])
            num2 = float(numbers[1])
            self.monitor1.setText(str(num1+num2))
        elif "-" in text:
            numbers = text.split("-")
            num1 = float(numbers[0])
            num2 = float(numbers[1])
            self.monitor1.setText(str(num1-num2))
        elif "*" in text:
            numbers = text.split("*")
            num1 = float(numbers[0])
            num2 = float(numbers[1])
            self.monitor1.setText(str(num1*num2))
        elif "/" in text:
            numbers = text.split("/")
            num1 = float(numbers[0])
            num2 = float(numbers[1])
            self.monitor1.setText(str(num1/num2))

    def clear(self):
        self.monitor1.setText("0")


class ClickerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Click in this window")
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            # handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            # handle the middle-button press in here.
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            # handle the right-button press in here.
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")

def application():
    app = QApplication(sys.argv)
    window = BarWindow()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()

