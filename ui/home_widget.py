from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from ui.custom_widgets.cakit_list_widget import CakitListWidget
from ui.custom_widgets.cakit_table_widget import CakitTableWidget
from PyQt6.QtCore import Qt

class HomeWidget(QWidget):
    def __init__(self, data_model):
        super().__init__()
        self.data_model = data_model
        

        # self.list_widget = CakitListWidget(data_model)
        self.table_widget = CakitTableWidget(data_model)


        # self.model.table_record_deleted.connect(self.test)
        # self.table_widget.model.table_record_deleted.connect(self.test)

        # Setup the layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        # Create a QPushButton with a + sign
        # add_button = QPushButton("+", self)
        # add_button.setFixedSize(40, 40)  # Set the size of the button
        # add_button.clicked.connect(self.open_dialog)
        # layout.addWidget(add_button)

        self.setLayout(layout)

    def test(self, r):
        print("test")

    def open_dialog(self):
        print("YAY")