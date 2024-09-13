from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QPushButton, QHBoxLayout
# from ui.stats.stats_widget import StatsWidget
from ui.stats.character_analysis_widget import CharacterAnalysisWidget
from ui.stats.example import ExampleWidget


class StatsTab(QWidget):
    def __init__(self, data_model):
        super().__init__()
        self.data_model = data_model
        
        # Create a QVBoxLayout to hold multiple QHBoxLayouts
        main_vbox_layout = QVBoxLayout(self)

        # Add multiple QHBoxLayouts to the QVBoxLayout
        hbox_item = CharacterAnalysisWidget(data_model)
        main_vbox_layout.addWidget(hbox_item)
        hbox_item2 = ExampleWidget(data_model)
        main_vbox_layout.addWidget(hbox_item2)
        # hbox_item3 = CharacterAnalysisWidget(f"Label3", f"Button")
        # main_vbox_layout.addWidget(hbox_item3)
        # hbox_item4 = CharacterAnalysisWidget(f"Label3", f"Button")
        # main_vbox_layout.addWidget(hbox_item4)

        # Set the layout on the main widget
        self.setLayout(main_vbox_layout)