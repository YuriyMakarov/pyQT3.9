import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.move(100, 100)
        self.setFixedSize(300, 150)

        self.layout = QVBoxLayout()

        self.result_display = QLineEdit()
        self.layout.addWidget(self.result_display)

        buttons_layout = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 0
        col = 0
        for text in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.on_button_clicked)
            buttons_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.layout.addLayout(buttons_layout)
        self.setLayout(self.layout)

    def on_button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = str(eval(self.result_display.text()))
                self.result_display.setText(result)
            except Exception as e:
                self.result_display.setText("Error")
        elif text == 'C':
            self.result_display.clear()
        else:
            current_text = self.result_display.text()
            new_text = current_text + text
            self.result_display.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())