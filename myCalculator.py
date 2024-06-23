from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("Заголовок программы")  # Заголовок программы
        #self.setGeometry(700, 500, 180, 270)  # Смещение по x, y \ ширина и высота
        self.move(700, 500)
        self.setFixedSize(216, 270)

        self.monitor1 = QtWidgets.QLabel(self)
        self.monitor1.setText("0")  # 2
        self.monitor1.setGeometry(10, 0, 170, 30)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setGeometry(0, 150, 60, 60)
        self.btn1.setText("1")
        self.btn1.clicked.connect(lambda: self.add_digit(self.btn1.text()))

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setGeometry(60, 150, 60, 60)
        self.btn2.setText("2")
        self.btn2.clicked.connect(lambda: self.add_digit(self.btn2.text()))

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setGeometry(120, 150, 60, 60)
        self.btn3.setText("3")
        self.btn3.clicked.connect(lambda: self.add_digit(self.btn3.text()))

        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.setGeometry(0, 90, 60, 60)
        self.btn4.setText("4")
        self.btn4.clicked.connect(lambda: self.add_digit(self.btn4.text()))

        self.btn5 = QtWidgets.QPushButton(self)
        self.btn5.setGeometry(60, 90, 60, 60)
        self.btn5.setText("5")
        self.btn5.clicked.connect(lambda: self.add_digit(self.btn5.text()))

        self.btn6 = QtWidgets.QPushButton(self)
        self.btn6.setGeometry(120, 90, 60, 60)
        self.btn6.setText("6")
        self.btn6.clicked.connect(lambda: self.add_digit(self.btn6.text()))

        self.btn7 = QtWidgets.QPushButton(self)
        self.btn7.setGeometry(0, 30, 60, 60)
        self.btn7.setText("7")
        self.btn7.clicked.connect(lambda: self.add_digit(self.btn7.text()))

        self.btn8 = QtWidgets.QPushButton(self)
        self.btn8.setGeometry(60, 30, 60, 60)
        self.btn8.setText("8")
        self.btn8.clicked.connect(lambda: self.add_digit(self.btn8.text()))

        self.btn9 = QtWidgets.QPushButton(self)
        self.btn9.setGeometry(120, 30, 60, 60)
        self.btn9.setText("9")
        self.btn9.clicked.connect(lambda: self.add_digit(self.btn9.text()))

        self.btn0 = QtWidgets.QPushButton(self)
        self.btn0.setGeometry(0, 210, 108, 60)
        self.btn0.setText("0")
        self.btn0.clicked.connect(lambda: self.add_digit(self.btn0.text()))

        self.btnP = QtWidgets.QPushButton(self)
        self.btnP.setGeometry(108, 210, 108, 60)
        self.btnP.setText("=")
        self.btnP.clicked.connect(self.calc)

        self.btnMul = QtWidgets.QPushButton(self)
        self.btnMul.setGeometry(180, 102, 36, 36)
        self.btnMul.setText("*")
        self.btnMul.clicked.connect(lambda: self.add_sign(self.btnMul.text()))

        self.btnDiv = QtWidgets.QPushButton(self)
        self.btnDiv.setGeometry(180, 66, 36, 36)
        self.btnDiv.setText("/")
        self.btnDiv.clicked.connect(lambda: self.add_sign(self.btnDiv.text()))

        self.btnPlus = QtWidgets.QPushButton(self)
        self.btnPlus.setGeometry(180, 174, 36, 36)
        self.btnPlus.setText("+")
        self.btnPlus.clicked.connect(lambda: self.add_sign(self.btnPlus.text()))

        self.btnMinus = QtWidgets.QPushButton(self)
        self.btnMinus.setGeometry(180, 138, 36, 36)
        self.btnMinus.setText("-")
        self.btnMinus.clicked.connect(lambda: self.add_sign(self.btnMinus.text()))

        self.btnDel = QtWidgets.QPushButton(self)
        self.btnDel.setGeometry(180, 30, 36, 36)
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




def application():
    app = QApplication(sys.argv)  #sys.argv - хранит настройки, связанный с компьютером для запуска
    myWindow = MyWindow()        #Создаем окно

    myWindow.show()               #Показ окна
    sys.exit(app.exec_())         #Корректные параметры выхода из приложения


if __name__ == "__main__":        #Запуск приложения
    application()

