from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QLabel

import sys


class BarWindow(QMainWindow):
    def __init__(self):
        super(BarWindow, self).__init__()

        self.move(700, 500)
        self.setWindowTitle("Приложуха")
        self.setWindowIcon(QIcon('icons/mainIcon.ico'))
        self.create_menu_bar()

    def open_main_window(self, window):
        self.hide()
        self.main_window = window()
        self.main_window.show()

    def create_menu_bar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Режимы", self)
        colorMenu = QMenu("&Тема", self)
        self.menuBar.addMenu(fileMenu)
        self.menuBar.addMenu(colorMenu)

        #open_file = fileMenu.addMenu("&Открыть")    # Добавляет пункт меню
        #save_menu = fileMenu.addMenu("&Сохранить")  # Добавляет пункт меню

        fileMenu.addAction("Калькулятор", self.action_clicked)
        fileMenu.addAction("События мышки", self.action_clicked)

        colorMenu.addAction("Темная", self.action_clicked)
        colorMenu.addAction("Светлая", self.action_clicked)

    @QtCore.pyqtSlot()                #аннотации для обработки нажатий пунктов меню
    def action_clicked(self):
        action = self.sender()
        if action.text() == 'Калькулятор':
            self.open_main_window(CalcWindow)
        elif action.text() == "События мышки":
            self.open_main_window(ClickerWindow)
        elif action.text() == "Темная":
            self.setStyleSheet("background-color: black; color: orange;")
        elif action.text() == "Светлая":
            self.setStyleSheet("background-color: none; color: none; }")


class CalcWindow(BarWindow):
    def __init__(self):
        super(CalcWindow, self).__init__()

        self.setWindowTitle("Заголовок программы")  # Заголовок программы
        #self.setGeometry(700, 500, 180, 270)  # Смещение по x, y \ ширина и высота
        self.setFixedSize(216, 290)

        self.monitor1 = QtWidgets.QLabel(self)
        self.monitor1.setText("0")  # 2
        self.monitor1.setGeometry(10, 20, 170, 50)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setGeometry(0, 170, 60, 60)
        self.btn1.setText("1")
        self.btn1.clicked.connect(lambda: self.add_digit(self.btn1.text()))

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setGeometry(60, 170, 60, 60)
        self.btn2.setText("2")
        self.btn2.clicked.connect(lambda: self.add_digit(self.btn2.text()))

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setGeometry(120, 170, 60, 60)
        self.btn3.setText("3")
        self.btn3.clicked.connect(lambda: self.add_digit(self.btn3.text()))

        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.setGeometry(0, 110, 60, 60)
        self.btn4.setText("4")
        self.btn4.clicked.connect(lambda: self.add_digit(self.btn4.text()))

        self.btn5 = QtWidgets.QPushButton(self)
        self.btn5.setGeometry(60, 110, 60, 60)
        self.btn5.setText("5")
        self.btn5.clicked.connect(lambda: self.add_digit(self.btn5.text()))

        self.btn6 = QtWidgets.QPushButton(self)
        self.btn6.setGeometry(120, 110, 60, 60)
        self.btn6.setText("6")
        self.btn6.clicked.connect(lambda: self.add_digit(self.btn6.text()))

        self.btn7 = QtWidgets.QPushButton(self)
        self.btn7.setGeometry(0, 50, 60, 60)
        self.btn7.setText("7")
        self.btn7.clicked.connect(lambda: self.add_digit(self.btn7.text()))

        self.btn8 = QtWidgets.QPushButton(self)
        self.btn8.setGeometry(60, 50, 60, 60)
        self.btn8.setText("8")
        self.btn8.clicked.connect(lambda: self.add_digit(self.btn8.text()))

        self.btn9 = QtWidgets.QPushButton(self)
        self.btn9.setGeometry(120, 50, 60, 60)
        self.btn9.setText("9")
        self.btn9.clicked.connect(lambda: self.add_digit(self.btn9.text()))

        self.btn0 = QtWidgets.QPushButton(self)
        self.btn0.setGeometry(0, 230, 108, 60)
        self.btn0.setText("0")
        self.btn0.clicked.connect(lambda: self.add_digit(self.btn0.text()))

        self.btnP = QtWidgets.QPushButton(self)
        self.btnP.setGeometry(108, 230, 108, 60)
        self.btnP.setText("=")
        self.btnP.clicked.connect(self.calc)

        self.btnMul = QtWidgets.QPushButton(self)
        self.btnMul.setGeometry(180, 122, 36, 36)
        self.btnMul.setText("*")
        self.btnMul.clicked.connect(lambda: self.add_sign(self.btnMul.text()))

        self.btnDiv = QtWidgets.QPushButton(self)
        self.btnDiv.setGeometry(180, 86, 36, 36)
        self.btnDiv.setText("/")
        self.btnDiv.clicked.connect(lambda: self.add_sign(self.btnDiv.text()))

        self.btnPlus = QtWidgets.QPushButton(self)
        self.btnPlus.setGeometry(180, 194, 36, 36)
        self.btnPlus.setText("+")
        self.btnPlus.clicked.connect(lambda: self.add_sign(self.btnPlus.text()))

        self.btnMinus = QtWidgets.QPushButton(self)
        self.btnMinus.setGeometry(180, 158, 36, 36)
        self.btnMinus.setText("-")
        self.btnMinus.clicked.connect(lambda: self.add_sign(self.btnMinus.text()))

        self.btnDel = QtWidgets.QPushButton(self)
        self.btnDel.setGeometry(180, 50, 36, 36)
        self.btnDel.setText("DEL")
        self.btnDel.clicked.connect(self.clear)

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


class ClickerWindow(BarWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(216, 290)
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

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

