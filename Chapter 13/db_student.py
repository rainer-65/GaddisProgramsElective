import sys

import mysql.connector
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget, QApplication, QTableWidgetItem, QLabel, \
    QLineEdit, QSizePolicy, QMessageBox

from secrets import secrets

# Get parameters for connection
my_host = secrets.get('DATABASE_HOST')
my_user = secrets.get('DATABASE_USER')
my_passwd = secrets.get('DATABASE_PWD')
my_db = secrets.get('DATABASE')


class TableDisplay(QWidget):

    def __init__(self):
        super(TableDisplay, self).__init__()
        # Logo for application
        self.setWindowIcon(QtGui.QIcon('student-logo.png'))
        # Create LineEdit
        self.sql_line = QLineEdit()
        self.sql_line.setText("select * from student")
        self.table_widget = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("MySQL Database")

        # Create Vertical Layout
        layout = QVBoxLayout()

        # Create Label
        sql_label = QLabel()
        sql_label.setText('SQL Statement')
        layout.addWidget(sql_label)

        # Add LineEdit
        layout.addWidget(self.sql_line)

        # Create two Buttons
        button_sql = QPushButton("Execute SQL Command")
        button_sql.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        layout.addWidget(button_sql)
        button_sql.clicked.connect(self.display_table)

        button_clear = QPushButton("Delete Input")
        button_clear.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        layout.addWidget(button_clear)
        button_clear.clicked.connect(self.clear_command)

        # Create a Table Widget
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

    def clear_command(self):
        self.sql_line.clear()

    def display_table(self):
        # Delete old table content
        self.table_widget.clear()
        try:
            db = mysql.connector.connect(
                host=my_host,
                user=my_user,
                password=my_passwd,
                database=my_db)
            print("Connection to mySQL database successful")
            try:
                # Execute SQL command
                cursor = db.cursor()
                cursor.execute(self.sql_line.text())
                data = cursor.fetchall()
            except mysql.connector.Error as error:
                self.show_message(error)
                print("Error when executing SQL statement")

            # Get number of rows / columns
            else:
                num_rows = len(data)
                num_cols = len(data[0])
                self.table_widget.setRowCount(num_rows)
                self.table_widget.setColumnCount(num_cols)
                # Fill table with data
                for i, row in enumerate(data):
                    for j, value in enumerate(row):
                        item = QTableWidgetItem(str(value))
                        self.table_widget.setItem(i, j, item)
                print("SQL Statement successfully executed")
        except mysql.connector.Error as error:
            self.show_message(error)
            print("Error when connecting to mySQL database")
        # Close database
        finally:
            cursor.close()
            db.close()

    def show_message(self, error):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setWindowTitle("Error message")
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableDisplay()
    window.resize(600, 600)
    window.show()
    show_program_info()
    sys.exit(app.exec_())
