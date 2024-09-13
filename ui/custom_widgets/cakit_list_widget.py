from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QMenu, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal 
from ui.custom_widgets.cakit_list_item_widget import CakitListItemWidget
from ui.custom_widgets.record_window import RecordWindow

class CakitListWidget(QListWidget):

    def __init__(self, data_model, parent=None):
        super().__init__(parent)
        self.data_model = data_model
        self.data_model.model_updated.connect(self.update_ui)

    def handleRightClick(self, position):
        item = self.itemAt(position)
        if item:
            menu = QMenu()
            menu.addAction("Send to decrypt", lambda: self.performAction(item, "Send to decrypt"))
            menu.exec(self.mapToGlobal(position))

    def mouseDoubleClickEvent(self, event):
        # Get the item at the mouse position
        item = self.itemAt(event.position().toPoint())
        if item:
            self.open_record_window(item.text())
        super().mouseDoubleClickEvent(event)

    def open_record_window(self, item_text):
        # Custom function to open a new window
        record_window = RecordWindow(item_text, self)
        record_window.show()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.RightButton:
            self.handleRightClick(event.pos())

    def performAction(self, item, action):
        pass 

    def update_ui(self):
        self.clear()
        # self.addItem("a", "b", "c")
        self.addItems([ x.get_record_src() for x in  self.data_model.model["records"]])

    # def addItem(self, column1_text, column2_text, column3_text):
    #     item = QListWidgetItem(self)
    #     widget = CakitListItemWidget(column1_text, column2_text, column3_text)
    #     item.setSizeHint(widget.sizeHint())  # Set size hint for the item
    #     self.addItem(item)  # Add item to the list widget
    #     self.setItemWidget(item, widget) 