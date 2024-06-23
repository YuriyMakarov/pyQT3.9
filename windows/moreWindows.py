from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Главное окно')

        self.button = QtWidgets.QPushButton('Открыть окно 2')
        self.button.clicked.connect(self.open_window2)
        self.setCentralWidget(self.button)

    def open_window2(self):
        self.hide()
        self.window2 = Window2()
        self.window2.show()

class Window2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Окно 2')

        self.button = QtWidgets.QPushButton('Вернуться в главное окно')
        self.button.clicked.connect(self.open_main_window)
        self.setCentralWidget(self.button)

    def open_main_window(self):
        self.hide()
        self.main_window = MainWindow()
        self.main_window.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()