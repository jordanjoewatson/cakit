from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QTextEdit
import math
from collections import Counter
from PyQt6.QtGui import QPainter
import pyqtgraph as pg
import random 

class CharacterAnalysisWidget(QWidget):
    def __init__(self, data_model):
        super().__init__()

        self.bytes_dct = { b: 0 for b in range(0x0, 0xFF+1) }
        self.data_model = data_model 
        self.data_model.model_changed.connect(self.update_tab)

        # Create a QHBoxLayout for the left and right sides
        main_layout = QHBoxLayout(self)

        # Create a QVBoxLayout for the left side (title and text)
        left_v_layout = QVBoxLayout()
        
        # Create and add a title QLabel
        title_label = QLabel("Byte Distribution", self)
        title_label.setStyleSheet("font-weight: bold; font-size: 16px;")  # Example styling for title

        # Create and add a QTextEdit for multi-line text
        self.body_text_edit = QTextEdit(self)
        self.body_text_edit.setPlainText("Entropy: \nCoverage:")
        self.body_text_edit.setReadOnly(True)  # Make the text read-only

        # Add the title and text edit to the vertical layout
        left_v_layout.addWidget(title_label)
        left_v_layout.addWidget(self.body_text_edit)

        # Add the vertical layout to the left side of the horizontal layout
        main_layout.addLayout(left_v_layout)

        self.chart_view = self.create_chart()
        main_layout.addWidget(self.chart_view)
        self.setLayout(main_layout)

    def create_chart(self):
        """Create a scatter plot chart with random data."""
        # Create a scatter series
        self.plot_widget = pg.PlotWidget()

        # Generate random data points
        x = list(self.bytes_dct.keys())
        y = list(self.bytes_dct.values())

        # Plot the data
        self.plot_widget.plot(x, y, pen=None, symbol='o')  # 'o' for circular markers

        return self.plot_widget


    def calculate_statistics(self):
        records = self.data_model.model["records"]
        self.bytes_dct = { b: 0 for b in range(0x0, 0xFF+1) }
        for r in records:
            bs = r.get_record_bytes()
            for b in bs:
                self.bytes_dct[b] += 1

        value_counts = Counter(self.bytes_dct.values())
        total_values = sum(value_counts.values())
        probabilities = [count / total_values for count in value_counts.values()]
        entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
        return entropy

    def rewrite_plot(self):
        self.plot_widget.clear()
        x = list(self.bytes_dct.keys())
        y = list(self.bytes_dct.values())

        # Plot the data
        self.plot_widget.plot(x, y, pen=None, symbol='o')
        self.plot_widget.setXRange(0, 255) 

    def update_tab(self):
        self.entropy = self.calculate_statistics()
        self.body_text_edit.setPlainText("""Entropy: {}
Coverage: {}  
        """.format(
            self.entropy,
            len(list({ k for k in self.bytes_dct.keys() if self.bytes_dct[k] > 0 })) / 255
        ))
        
        # self.chart_view = self.create_chart()
        # Generate random data points
        self.rewrite_plot()