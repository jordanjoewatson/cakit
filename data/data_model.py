from PyQt6.QtCore import pyqtSignal, QObject
from data.record import Record
import os 

class DataModel(QObject):

    model_updated = pyqtSignal()
    # record_added = pyqtSignal(list)
    record_added = pyqtSignal(Record)
    model_changed = pyqtSignal()
    signal_decrypt_data_updated = pyqtSignal(Record)

    def __init__(self):
        super().__init__()

        self.model = {
            "records": [],
            "decrypt_data": {
                "record": None
            }, 
            "evaluators": []
        }

        # Read in evaluators here
        # THIS COULD BE BUGGY IN FUTURE DEPENDING ON HOW ITS RUN
        pwd = os.getcwd()
        evaluator_path = os.path.join(pwd, "ui", "decrypt", "evaluators", "evaluators")
        for files in os.listdir(evaluator_path):
            evaluator_file = os.path.join(evaluator_path, files)

            with open(evaluator_file, 'r') as efh:
                code = efh.read()
            
            # Create a dictionary to hold the context for the exec
            context = {}
            # Execute the code within the context dictionary
            exec(code, globals(), context)

            self.model["evaluators"].append({
                "name": context["name"],
                "function": context["evaluator"]
            })


    def get_evaluator_lambda(self, ev_name):
        for ev in self.model["evaluators"]:
            if ev["name"] == ev_name:
                return ev["function"]

    # def set_data(self, key, value):
    #     self.model[key] = value

    # def get_data(self, key):
    #     return self.model.get(key, None)

    def delete_record(self, record):
        self.model['records'] = [ r for r in self.model['records'] if r.get_id() != record.get_id() ]
        self.model_changed.emit()

    def add_record(self, record):
        self.model["records"].append(record)
        # self.record_added.emit(record.to_list())
        self.record_added.emit(record)
        self.model_changed.emit()

    def update_decrypt_record(self, record):
        self.model["decrypt_data"] = {
            "record": record
        }
        self.signal_decrypt_data_updated.emit(record)