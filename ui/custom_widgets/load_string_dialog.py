from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QMessageBox, QWidget, QLineEdit, QDialog,
    QLabel, QTextEdit, QComboBox, QDialogButtonBox
)
from data.record import Record

class LoadStringDialog(QDialog):
    def __init__(self, data_model):
        super().__init__()
        self.data_model = data_model

        self.setWindowTitle("Load String")

        # Layout for the dialog
        layout = QVBoxLayout()


        self.text_area_name = QLineEdit(self)
        layout.addWidget(QLabel("Enter Source/Name:"))
        layout.addWidget(self.text_area_name)

        # Text area
        self.text_area_string = QTextEdit(self)
        layout.addWidget(QLabel("Enter String:"))
        layout.addWidget(self.text_area_string)

        # Dropdown menu
        self.dropdown = QComboBox(self)
        self.dropdown.addItems(["Hex string", "String"])
        self.dropdown.currentIndexChanged.connect(self.on_first_dropdown_change)
        layout.addWidget(QLabel("Select Data Type:"))
        layout.addWidget(self.dropdown)

        self.second_dropdown = QComboBox(self)
        self.second_dropdown.addItems(["utf-8", "utf-16", "utf-16le", "ascii", "latin-1"])
        self.second_dropdown_title = QLabel("Encoding:")
        layout.addWidget(self.second_dropdown_title)
        layout.addWidget(self.second_dropdown)
        self.second_dropdown.hide()  
        self.second_dropdown_title.hide()

        # Buttons for the dialog
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.validate_and_accept)  # Connect OK button to accept
        button_box.rejected.connect(self.reject)  # Connect Cancel button to reject
        layout.addWidget(button_box)

        self.setLayout(layout)
        self.resize(500,300)

    def is_hex_string(self, s):
        hex_digits = set("0123456789abcdefABCDEF")
        return all(char in hex_digits for char in s)

    def validate_and_accept(self):
        name = self.text_area_name.text()
        data = self.text_area_string.toPlainText()
        data_type = self.dropdown.currentText()
        encoding = self.second_dropdown.currentText()
        # Check if both fields have text
        if not name or not data:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
        elif data_type == "Hex string" and not self.is_hex_string(data):
            QMessageBox.warning(self, "Input Error", "Hex string only allows valid hex string data.")
        else:
            self.accept()
            data_bytes = None
            if data_type == "String":
                data_bytes = data.encode(encoding)
            elif data_type == "Hex string":
                data_bytes = bytes.fromhex(data)
            r = Record(name, data_bytes)
            self.data_model.add_record(r)

    def get_data(self):
        # Return the text and selected option
        return self.text_area_name.text(), self.text_area_string.toPlainText(), self.dropdown.currentText(), self.second_dropdown.currentText()

    def on_first_dropdown_change(self, index):
        # Show or hide the second dropdown based on the selection
        if self.dropdown.currentText() == "String":
            self.second_dropdown.show()
            self.second_dropdown_title.show()
        else:
            self.second_dropdown.hide()
            self.second_dropdown_title.hide()