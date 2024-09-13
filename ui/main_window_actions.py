import os 
from PyQt6.QtWidgets import QFileDialog, QDialog
from data.record import Record 
from ui.custom_widgets.load_string_dialog import LoadStringDialog

class MainWindowActions:
    def __init__(self, data_model, parent_window):
        self.data_model = data_model
        self.parent_window = parent_window

    def load_directory(self):
        selected_directory = QFileDialog.getExistingDirectory(self.parent_window, "Select folder")
        files = [ f for f in os.listdir(selected_directory) if os.path.isfile(os.path.join(selected_directory,f))]
        for f in files:
            fpath = os.path.join(selected_directory, f)
            with open(fpath, 'rb') as fh:
                record_byte_array = fh.read()
                r = Record(
                    fpath,
                    record_byte_array
                )

                self.data_model.add_record(r)

    def load_string(self):
        dialog = LoadStringDialog(self.data_model)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            name, data, data_type, encoding = dialog.get_data()
            print(f"Name: {name}, Data: {data}, Type: {data_type}, Encoding: {encoding}")