import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("Кнопочки")
        self.setWindowIcon(QIcon("icons/mainIcon.ico"))
        self.setFixedSize(300, 200)
        #self.resize(100, 200)
        self.move(1200, 300)

        self.btn_1 = QPushButton(self)
        #self.btn_1.move(100, 100)
        #self.btn_1.setFixedSize(100, 100)
        self.btn_1.setGeometry(10, 10, 70, 50)
        self.btn_1.setText("Кнопка 1")
        self.btn_1.clicked.connect(lambda: self.buttonPluse(self.btn_1, 1))

        self.btn_2 = QPushButton(self)
        self.btn_2.setGeometry(80, 10, 70, 50)
        self.btn_2.setText("Кнопка 2")
        self.btn_2.clicked.connect(lambda: self.buttonPluse(self.btn_2, 5))

        self.btn_3 = QPushButton(self)
        self.btn_3.setGeometry(150, 10, 70, 50)
        self.btn_3.setText("Кнопка 3")
        self.btn_3.clicked.connect(lambda: self.buttonPluse(self.btn_3, 20))

        self.btn_4 = QPushButton(self)
        self.btn_4.setGeometry(220, 10, 70, 50)
        self.btn_4.setText("Кнопка 4")
        self.btn_4.clicked.connect(self.labelPluse)

        self.label_1 = QLabel(self)
        self.label_1.setText("1")
        self.label_1.setGeometry(30, 50, 70, 50)

        self.line_1 = QLineEdit(self)
        self.line_1.setGeometry(10, 100, 70, 50)


    def labelPluse(self):
        btn_int = int(self.label_1.text())
        self.label_1.setText(str(btn_int + 1))


    def buttonPluse(self, btn, lv):
        btn_text = btn.text().split()
        btn_int = int(btn_text[-1]) + lv
        btn.setText(btn_text[0] + " " + str(btn_int))


    def printText(self, btn):
        print(btn.text())


def application():
    app = QApplication(sys.argv)  #sys.argv - хранит настройки, связанный с компьютером для запуска

    myWindow = MyWindow()        #Создаем окно
    myWindow.show()               #Показ окна

    sys.exit(app.exec_())         #Корректные параметры выхода из приложения


if __name__ == "__main__":        #Запуск приложения
    application()
