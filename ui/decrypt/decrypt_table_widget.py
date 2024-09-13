from PyQt6.QtWidgets import QVBoxLayout, QWidget, QTableView, QListWidget, QListWidgetItem, QMenu, QMessageBox
from ui.decrypt.decrypt_table_model import DecryptTableModel
from ui.decrypt.decrypt_table_view import DecryptTableView
# from PyQt6.QtCore import Qt, pyqtSignal 
# from ui.custom_widgets.cakit_list_item_widget import CakitListItemWidget
# from ui.custom_widgets.record_window import RecordWindow
from ui.decrypt.progress_bar_delegate import ProgressBarDelegate

class DecryptTableWidget(QWidget):

    def __init__(self, data_model, parent=None):
        super().__init__(parent)
        self.data_model = data_model

        self.model = DecryptTableModel()
        self.table_view = DecryptTableView(self.model)

        self.table_view.setModel(self.model)
        self.table_view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.table_view.verticalHeader().setVisible(False)

        # delegate = ProgressBarDelegate(self.table_view)
        # self.table_view.setItemDelegateForColumn(2, delegate)

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.table_view)

    def add_batch_to_table(self, batch):
        self.model.add_batch_to_table(batch)

    def clear_table(self):
        self.model.clear_table()