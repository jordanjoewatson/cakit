from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox

class EvaluatorWidget(QWidget):

    def __init__(self, data_model, parent=None):
        super().__init__(parent)
        self.data_model = data_model

        # self.model = DecryptTableModel()
        # self.table_view = DecryptTableView(self.model)

        # self.table_view.setModel(self.model)
        # self.table_view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        # self.table_view.verticalHeader().setVisible(False)

        evs = [ evaluator["name"] for evaluator in data_model.model["evaluators"] ]

        # Layout
        layout = QVBoxLayout(self)

        title = QLabel("Evaluator")
        self.evaluator_dropdown = QComboBox(self)
        self.evaluator_dropdown.addItems(evs)

        # self.evaluator_dropdown.currentIndexChanged.connect(self.on_selector_dropdown_change)

        layout.addWidget(title)
        layout.addWidget(self.evaluator_dropdown)

    def get_selected_evaluator(self):
        return self.evaluator_dropdown.currentText()