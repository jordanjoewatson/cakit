import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTableView
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex, pyqtSignal
from data.record import Record 

# Custom Table Model
class CakitTableModel(QAbstractTableModel):

    table_record_deleted = pyqtSignal(Record)

    def __init__(self):
        super().__init__()
        # self._data = [Record("", b'')] # TODO: Fix
        self._data = []
        self._headers = [
            "bytes", 
            "source"
        ]

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    # def data(self, index, role=Qt.ItemDataRole.DisplayRole):
    #     if role == Qt.ItemDataRole.DisplayRole:
    #         return self._data[index.row()][index.column()]
    #     return None
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        # if index.isValid() and 0 <= index.row() < len(self._data) and 0 <= index.column() < len(self._headers):
        person = self._data[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return person.to_list()[index.column()]
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._headers[section]
            return None


    def add_record(self, record):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._data.append(record)
        self.endInsertRows()

    # def delete_record(self, selected_index):
    #     if selected_index.isValid():
    #         row = selected_index.row()
    #         record = self.model.get_record(row)
    #         print(f"Delete-ing record {record.get_record_src()}")
    #         self.table_record_deleted.emit(record)
    #         # TODO: Need to remove this row from the data_model as well, not just the table model
    #         self.model.beginRemoveRows(QModelIndex(), row, row)
    #         del self.model._data[row]
    #         self.model.endRemoveRows()

    def get_record(self, row):
        if 0 <= row < len(self._data):
            return self._data[row]
        return None