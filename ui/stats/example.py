from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QTextEdit
import math
from collections import Counter
from PyQt6.QtGui import QPainter
import pyqtgraph as pg
import random 

class GraphWidget(QWidget):
    def __init__(self):
        super().__init__()
        # This is a placeholder for the graph
        self.setMinimumSize(400, 150)
        self.setStyleSheet("background-color: black;") 

class ExampleWidget(QWidget):
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
        title_label = QLabel("Example something", self)
        title_label.setStyleSheet("font-weight: bold; font-size: 16px;")  # Example styling for title

        # Create and add a QTextEdit for multi-line text
        self.body_text_edit = QTextEdit(self)
        self.body_text_edit.setPlainText("Something else: ")
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
        self.random_val = random.randint(0,50)

    def rewrite_plot(self):
        self.plot_widget.clear()
        x = list([ random.randint(0,10) for i in range(0,100)])
        y = list([ random.randint(0,10) for i in range(0,100)])
        self.plot_widget.plot(x, y, pen=None, symbol='o')

    def update_tab(self):
        self.entropy = self.calculate_statistics()
        self.body_text_edit.setPlainText("Example something: {}".format(self.random_val))
        # self.chart_view = self.create_chart()
        # Generate random data points
        self.rewrite_plot()