from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox
from ui.decrypt.xor.xor_widget import XorWidget 

class DecryptorSelectorWidget(QWidget):

    def __init__(self, data_model, parent=None):
        super().__init__(parent)
        self.data_model = data_model

        # self.model = DecryptTableModel()
        # self.table_view = DecryptTableView(self.model)

        # self.table_view.setModel(self.model)
        # self.table_view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        # self.table_view.verticalHeader().setVisible(False)

        # Layout
        layout = QVBoxLayout(self)
        title = QLabel("Decryptor")

        self.selector_dropdown = QComboBox(self)
        self.selector_dropdown.addItems(["xor", "NOT IMPLEMENTED"])
        self.selector_dropdown.currentIndexChanged.connect(self.on_selector_dropdown_change)

        self.xor_widget = XorWidget()

        layout.addWidget(title)
        layout.addWidget(self.selector_dropdown)
        layout.addWidget(self.xor_widget)

    def on_selector_dropdown_change(self, index):
        # Show or hide the second dropdown based on the selection
        if self.selector_dropdown.currentText() == "xor":
            self.xor_widget.show()
        else:
            self.xor_widget.hide()

    def get_selected_decryptor(self):
        return self.selector_dropdown.currentText()

    def get_xor_options(self):
        return self.xor_widget.get_selected_options()