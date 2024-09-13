import sys
from PyQt6.QtWidgets import QLabel, QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTableView
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex, pyqtSignal
from data.record import Record 

from PyQt6.QtWidgets import QStyledItemDelegate, QStyle, QStyleOptionProgressBar
from PyQt6.QtGui import QPainter

# Custom Table Model
class DecryptTableModel(QAbstractTableModel):

    table_record_deleted = pyqtSignal(Record)

    def __init__(self):
        super().__init__()
        # self._data = [Record("", b'')] # TODO: Fix
        self._data = []
        self._headers = [
            "decryption",
            "score",
            "key",
            "misc"
        ]

    def sort(self, column, order):
        # self.layoutAboutToBeChanged.emit()
        self._data.sort(key=lambda row: row[column], reverse=(order == Qt.SortOrder.DescendingOrder))
        # self.layoutChanged.emit()

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        # # if index.isValid() and 0 <= index.row() < len(self._data) and 0 <= index.column() < len(self._headers):
        decrypted_record = self._data[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return decrypted_record[index.column()]
        return None


    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._headers[section]
            return None


    # def add_record(self, record):
    #     self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
    #     self._data.append(record)
    #     self.endInsertRows()

    def get_record(self, row):
        if 0 <= row < len(self._data):
            return self._data[row]
        return None
    
    def add_batch_to_table(self, batch):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount() + len(batch) - 1)
        self._data.extend(batch)
        # End the batch update
        self.endInsertRows()
        self.sort(1, Qt.SortOrder.DescendingOrder)

    # def clear_table(self):
    #     self.clearContents()
    #     self.setRowCount(0)

    def clear_table(self, parent=QModelIndex()):
        print("HERE")
        self.beginRemoveRows(parent, 0, self.rowCount()-1)
        del self._data[0:self.rowCount()]
        self.endRemoveRows()