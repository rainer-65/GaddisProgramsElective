import sys

import mysql.connector
from PyQt5 import QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget, QApplication, QTableWidgetItem, QLabel, \
    QLineEdit, QSizePolicy, QMessageBox
from mysql.connector.constants import ClientFlag

import credentials

# Config-File für den Zugriff auf die Google Cloud SQL (mit SSL-Verschlüsselung)
config = {
    'user': credentials.DATABASE_USER,
    'password': credentials.DATABASE_PWD,
    'host': '34.66.98.190',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem'
}


class TableDisplay(QWidget):

    def __init__(self):
        super(TableDisplay, self).__init__()
        # Logo für Anwendung
        self.setWindowIcon(QtGui.QIcon('student-logo.png'))
        # Ein LineEdit erzeugen
        self.sql_line = QLineEdit()
        self.sql_line.setText("select * from studentdb.student")
        self.table_widget = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("MySQL Datenbank")

        # Ein Vertical Layout erzeugen
        layout = QVBoxLayout()

        # Ein Label erzeugen
        sql_label = QLabel()
        sql_label.setText('SQL Statement')
        layout.addWidget(sql_label)

        # Ein LineEdit hinzufügen
        layout.addWidget(self.sql_line)

        # Zwei Buttons erzeugen
        button_sql = QPushButton("SQL Befehl ausführen")
        button_sql.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        layout.addWidget(button_sql)
        button_sql.clicked.connect(self.display_table)

        button_clear = QPushButton("Eingabe löschen")
        button_clear.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        layout.addWidget(button_clear)
        button_clear.clicked.connect(self.clear_command)

        # Ein Table Widget erzeugen
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

    def clear_command(self):
        self.sql_line.clear()

    def display_table(self):
        # Alten Tabelleninhalt löschen
        self.table_widget.clear()
        try:
            # Verbindung zur MySQL Datenbank aufbauen
            db = mysql.connector.connect(**config)
            print("Verbindung zur mySQL Datenbank hergestellt")
            try:
                # SQL Befehl ausführen
                cursor = db.cursor()
                cursor.execute(self.sql_line.text())
                data = cursor.fetchall()
            except mysql.connector.Error:
                print("Error when performing SQL statement")

            # Zahl der Zeilen und Spalten ermitteln
            else:
                num_rows = len(data)
                num_cols = len(data[0])
                self.table_widget.setRowCount(num_rows)
                self.table_widget.setColumnCount(num_cols)
                # Tabelle mit Daten füllen
                for i, row in enumerate(data):
                    for j, value in enumerate(row):
                        item = QTableWidgetItem(str(value))
                        if i % 2 == 0:
                            # Background color "hellgrau"
                            background_color = QColor(240, 240, 240)  # Light gray
                        else:
                            # Background color "weiss"
                            background_color = QColor(255, 255, 255)  # White
                        item.setBackground(background_color)
                        self.table_widget.setItem(i, j, item)
                print("SQL statement successfully performed")
        except mysql.connector.Error:
            print("Error when connecting to MySQL database")
        # Datenbank schliessen
        finally:
            cursor.close()
            db.close()


def show_program_info():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.setWindowTitle("Information")
    msg.setStyleSheet("background-color: rgb(255,255,204);")
    msg.setText("Programs for executing SQL statements")
    msg.setInformativeText("BSc BIT Python Elective, WS 2023/24")
    msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableDisplay()
    window.resize(600, 600)
    window.show()
    show_program_info()
    sys.exit(app.exec_())
