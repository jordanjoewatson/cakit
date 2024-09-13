from PyQt6.QtWidgets import QTableView, QHeaderView
from PyQt6.QtCore import Qt, QModelIndex, pyqtSignal
from PyQt6.QtGui import QMouseEvent, QContextMenuEvent, QAction
from PyQt6.QtWidgets import QMenu
from data.record import Record


# I tihnk this can all be added into widget instead of having a view, kind of pointless
class DecryptTableView(QTableView):

    def __init__(self, decrypt_table_model):
        super().__init__()
        self.model = decrypt_table_model
        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.context_menu = QMenu(self)
        # self.setup_context_menu()

    def clear_table(self):
        self.model.removeRows(0, self.model.rowCount()) # clearContents()
        # self.setRowCount(0)

    # def setup_context_menu(self):
    #     # Add actions to the context menu
    #     # self.action_edit = QAction("Edit", self)
    #     self.action_delete = QAction("Delete", self)
    #     # self.context_menu.addAction(self.action_edit)
    #     self.context_menu.addAction(self.action_delete)

    #     # Connect actions to slots
    #     # self.action_edit.triggered.connect(self.edit_row)
    #     self.action_delete.triggered.connect(self.delete_record)

    #     self.action_decrypt = QAction("Decrypt", self)
    #     self.context_menu.addAction(self.action_decrypt)
    #     self.action_decrypt.triggered.connect(self.send_record_to_decrypt)

    # def mousePressEvent(self, event: QMouseEvent):
    #     if event.button() == Qt.MouseButton.RightButton:
    #         index = self.indexAt(event.position().toPoint())
    #         if index.isValid():
    #             self.selected_index = index
    #             self.context_menu.exec(event.globalPosition().toPoint())
    #     super().mousePressEvent(event)

    # def edit_row(self):
    #     if self.selected_index.isValid():
    #         row = self.selected_index.row()
    #         print(f"Edit row {row}")

    # I don't like this here, but it's working for now, ass selected index is easiest to get form here
    # Or maybe i could just sort of proxy this request to the model after the if
    # def delete_record(self):
    #     if self.selected_index.isValid():
    #         row = self.selected_index.row()
    #         record = self.model.get_record(row)
    #         print(f"Deleting record {record.get_record_src()}")
    #         self.table_record_deleted.emit(record)
    #         # TODO: Need to remove this row from the data_model as well, not just the table model
    #         self.model.beginRemoveRows(QModelIndex(), row, row)
    #         del self.model._data[row]
    #         self.model.endRemoveRows()

    # def send_record_to_decrypt(self):
    #     if self.selected_index.isValid():
    #         row = self.selected_index.row()
    #         record = self.model.get_record(row)
    #         self.signal_send_to_decrypt.emit(record)
    