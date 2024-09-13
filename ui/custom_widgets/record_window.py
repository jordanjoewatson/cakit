from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt

class RecordWindow(QWidget):
    def __init__(self, item_text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Details Window")
        if parent:
            # Make the window cover the main window's client area
            parent_rect = parent.rect()  # Get the client area of the parent
            # parent_rect.adjust(0, parent.menuBar().height(), 0, 0)  # Adjust to exclude the menu bar
            self.setGeometry(parent_rect)  # Set geometry to cover the client area
        else:
            # Default size if no parent is provided
            self.resize(400, 300)

        # Set window flags to keep it on top of the parent
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowStaysOnTopHint)
        
        # self.setStyleSheet("background-color: white;") 
        # Layout and content for the details window
        layout = QVBoxLayout()
        self.label = QLabel(f"Details for: {item_text}", self)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # close_button = QPushButton("Close", self)
        # close_button.clicked.connect(self.close)  # Connect the button click to the close method
        
        # Layout for the button
        # button_layout = QHBoxLayout()
        # button_layout.addStretch()  # Push button to the right
        # button_layout.addWidget(close_button)
        
        # layout.addLayout(button_layout)  # Add button layout to the main layout
        # self.setLayout(layout)