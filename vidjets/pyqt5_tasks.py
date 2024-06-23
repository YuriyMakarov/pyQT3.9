import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color, text):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        self.monitor1 = QtWidgets.QLabel(self)
        self.monitor1.setText(text)  # 2

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()

        buttons_text = (("1", "2", "3","+"),
                        ("4", "5", "6", "-"),
                        ("7", "8", "9", ":"))

        for i in range(len(buttons_text)):
            for j in range(len(buttons_text[i])):
                layout.addWidget(Color('red', buttons_text[i][j]), i, j)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()