# Example from https://www.techwithtim.net/tutorials/python-module-walk-throughs/pyqt5-tutorial/buttons-and-events
# Small adaptions

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.label = None
        self.button = None
        self.init_ui()

    def button_clicked(self):
        self.update()

    def init_ui(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("First PyQt Example")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World!")
        self.label.move(10, 50)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Click me!")
        self.button.clicked.connect(self.button_clicked)

    def update(self):
        # Changing the background color and font size of text
        self.setStyleSheet("background-color: yellow;")
        self.label.setFont(QFont('Arial', 12))
        self.label.setText("Hello World!")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
