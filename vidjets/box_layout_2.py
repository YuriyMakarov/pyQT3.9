import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QTextEdit, \
    QCheckBox, QWidget


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(600, 600, 700, 700)

        hbox_layout = QHBoxLayout()
        hbox_layout.addStretch(1)
        hbox_layout.addWidget(QPushButton("1"))
        hbox_layout.addWidget(QPushButton("2"))
        hbox_layout.addWidget(QPushButton("3"))


        vbox_layout = QVBoxLayout()
        vbox_layout.addStretch(1)
        vbox_layout.addLayout(hbox_layout)

        central_widget = QWidget()
        central_widget.setLayout(vbox_layout)

        self.setCentralWidget(central_widget)


def application():
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()

# vbox_layout = QVBoxLayout()
# vbox_layout.addWidget(QLineEdit())
# vbox_layout.addWidget(QTextEdit())
# vbox_layout.addWidget(QCheckBox())

# container = QWidget()
# container.setLayout(hbox_layout)
# container.setLayout(vbox_layout)

# self.setCentralWidget(container)