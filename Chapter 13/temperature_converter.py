import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QRadioButton


class TemperatureConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties (title and initial size)
        self.setWindowTitle("Temperature Converter")
        # (x, y, width, height)
        self.setGeometry(100, 100, 300, 200)

        # Create a central widget for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create radio buttons for unit selection
        self.celsius_radio = QRadioButton("Celsius")
        self.fahrenheit_radio = QRadioButton("Fahrenheit")

        # Create labels and input fields for temperature input and result
        input_label = QLabel("Enter Temperature:")
        self.input_field = QLineEdit()
        result_label = QLabel("Result:")
        self.result_field = QLineEdit()
        self.result_field.setReadOnly(True)

        # Create a convert button
        convert_button = QPushButton("Convert")
        convert_button.clicked.connect(self.convert_temperature)

        # Create layout for unit selection
        unit_layout = QVBoxLayout()
        unit_layout.addWidget(self.celsius_radio)
        unit_layout.addWidget(self.fahrenheit_radio)

        # Create layout for temperature input and result
        input_layout = QVBoxLayout()
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(result_label)
        input_layout.addWidget(self.result_field)
        input_layout.addWidget(convert_button)

        # Create layout for central widget
        layout = QVBoxLayout()
        layout.addLayout(unit_layout)
        layout.addLayout(input_layout)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

        # Set default unit to Celsius
        self.celsius_radio.setChecked(True)
        self.fahrenheit_radio.setChecked(False)

    def convert_temperature(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = TemperatureConverterApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
