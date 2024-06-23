from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Мое приложение")

        self.label = QLabel()   #создаем виджет поле вывода

        self.input = QLineEdit() #создаем виджет поле ввода
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()                #Создаем макет
        layout.addWidget(self.input)          #добавляем виджет поле ввода в макет
        layout.addWidget(self.label)          #добавляем виджет поле вывода в макет

        container = QWidget()                #создаем виджет-контейнер
        container.setLayout(layout)          #помещаем наш макет в виджет

        self.setCentralWidget(container)



def application():
    app = QApplication(sys.argv)  #sys.argv - хранит настройки, связанный с компьютером для запуска
    myWindow = MainWindow()        #Создаем окно

    myWindow.show()               #Показ окна
    sys.exit(app.exec_())         #Корректные параметры выхода из приложения


if __name__ == "__main__":        #Запуск приложения
    application()
