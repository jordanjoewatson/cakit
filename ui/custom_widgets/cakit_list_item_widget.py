from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout

class CakitListItemWidget(QWidget):
    def __init__(self, column1_text, column2_text, column3_text, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        
        self.column1_label = QLabel(column1_text, self)
        self.column2_label = QLabel(column2_text, self)
        self.column3_label = QLabel(column3_text, self)

        layout.addWidget(self.column1_label)
        layout.addWidget(self.column2_label)
        layout.addWidget(self.column3_label)
        
        layout.addStretch()  # Optional: Push widgets to the left
        self.setLayout(layout)
