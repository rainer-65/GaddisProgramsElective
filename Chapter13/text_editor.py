# https://www.pythontutorial.net/pyqt/pyqt-qmainwindow/
# some adaptions

import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QStatusBar, QAction, QFileDialog


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Editor')
        self.setGeometry(100, 100, 500, 300)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Create newFile Action
        new_action = QAction('&New', self)
        new_action.setShortcut('Ctrl+N')
        new_action.setStatusTip('New document')
        new_action.triggered.connect(self.new_file)

        # Create openFile Action
        open_action = QAction('&Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open text file')
        open_action.triggered.connect(self.open_file)

        # Create quit app Action
        quit_action = QAction('&Quit', self)
        quit_action.setShortcut('Ctrl+Q')
        quit_action.setStatusTip('Quit application')
        quit_action.triggered.connect(self.quit_action)

        # Setting menu
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('&File')

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(quit_action)

        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('Awesome Editor v1.0')

        self.show()

    def new_file(self):
        self.text_edit.clear()

    def open_file(self):
        # File Dialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Text File", os.path.expanduser("~"),
                                                   "Text Files (*.txt)")

        # Read the txt-File
        with open(file_path) as my_file:
            self.text_edit.append(my_file.read())

    def quit_action(self):
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
