from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox

class XorWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.data_model = data_model

        # Layout
        layout = QVBoxLayout(self)

        title = QLabel("XOR")

        self.attack_type_dropdown = QComboBox(self)
        self.attack_type_dropdown.addItems(["Brute force"])

        self.xor_key_length_dropdown = QComboBox(self)
        self.xor_key_length_dropdown.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])

        layout.addWidget(title)
        layout.addWidget(self.attack_type_dropdown)
        layout.addWidget(self.xor_key_length_dropdown)

    def get_selected_options(self):
        return {
            "attack_type": self.attack_type_dropdown.currentText(),
            "key_length": self.xor_key_length_dropdown.currentText()
        }