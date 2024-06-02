from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog


import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Редактор")
        self.setGeometry(300, 250, 250, 200)
        self.setWindowIcon(QIcon('icons/mainIcon.ico'))

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.create_menu_bar()

    def create_menu_bar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        #open_file = fileMenu.addMenu("&Открыть")    # Добавляет пункт меню
        #save_menu = fileMenu.addMenu("&Сохранить")  # Добавляет пункт меню

        fileMenu.addAction("Открыть", self.action_clicked)
        fileMenu.addAction("Сохранить", self.action_clicked)


    @QtCore.pyqtSlot()                #аннотации для обработки нажатий пунктов меню
    def action_clicked(self):
        action = self.sender()
        fname = QFileDialog.getOpenFileName(self)[0]
        if action.text() == 'Открыть':
            try:
                with open(fname, "r", encoding="UTF-8") as f:
                    data = f.read()
                    self.text_edit.setText(data)
            except FileNotFoundError:
                print("Файл не найден")

        elif action.text() == "Сохранить":
            try:
                with open(fname, "w", encoding="UTF-8") as f:
                    text = self.text_edit.toPlainText()
                    f.write(text)
            except FileNotFoundError:
                print("Файл не найден")



def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()

