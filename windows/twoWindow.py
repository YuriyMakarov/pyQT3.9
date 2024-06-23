import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction, QWidget, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QStackedWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Переключение")
        self.setGeometry(500, 500, 300, 50)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        self.calculator_widget = QWidget()
        self.calculator_layout = QVBoxLayout(self.calculator_widget)
        self.calculator_layout.addWidget(QLabel("Калькулятор"))
        self.calculator_layout.addWidget(QPushButton("Вычисляем"))
        self.stacked_widget.addWidget(self.calculator_widget)

        self.settings_widget = QWidget()
        self.settings_layout = QVBoxLayout(self.settings_widget)
        self.settings_layout.addWidget(QLabel("Найстройки виджета"))
        self.settings_layout.addWidget(QLineEdit())
        self.stacked_widget.addWidget(self.settings_widget)

        menu_bar = QMenuBar()
        calculator_action = QAction("Калькулятор", self)
        calculator_action.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        settings_action = QAction("Настройки", self)
        settings_action.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        menu_bar.addAction(calculator_action)
        menu_bar.addAction(settings_action)
        self.setMenuBar(menu_bar)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
