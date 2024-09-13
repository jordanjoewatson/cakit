from PyQt6.QtWidgets import QWidget, QTextEdit, QLineEdit, QVBoxLayout, QLabel, QScrollArea, QPushButton, QHBoxLayout

from ui.decrypt.decrypt_table_widget import DecryptTableWidget
from ui.decrypt.evaluators.evaluator_widget import EvaluatorWidget
from ui.decrypt.decryptor_selector_widget import DecryptorSelectorWidget
from ui.decrypt.xor.xor_decryptor import xor_decryptor

class DecryptTab(QWidget):
    def __init__(self, data_model):
        super().__init__()
        self.data_model = data_model
        
        main_vbox_layout = QVBoxLayout(self)

        self.record_data = QLineEdit(self)
        self.record_data.setText("")
        self.record_data.setReadOnly(True)
        main_vbox_layout.addWidget(QLabel("Record:"))
        main_vbox_layout.addWidget(self.record_data)

        self.button = QPushButton("Execute order 66")
        self.button.clicked.connect(self.on_button_click)

        self.clear_button = QPushButton("Clear table")
        # self.clear_button.clicked.connect(self.clear_table)

        decryptor_panel = QVBoxLayout()
        placeholder = QTextEdit()
        self.evaluator_widget = EvaluatorWidget(data_model)
        self.decryptor_selector_widget = DecryptorSelectorWidget(data_model)
        decryptor_panel.addWidget(self.decryptor_selector_widget)
        decryptor_panel.addWidget(self.evaluator_widget)
        decryptor_panel.addWidget(self.button)
        decryptor_panel.addWidget(self.clear_button)
        
        # decryptor_panel.setSpacing(0)  # No space between widgets
        #decryptor_panel.setContentsMargins(0, 0, 0, 0)

        table_and_decryptor_panel = QHBoxLayout()
        self.table = DecryptTableWidget(data_model)
        self.clear_button.clicked.connect(self.table.clear_table)
        table_and_decryptor_panel.addWidget(self.table, stretch=5)
        table_and_decryptor_panel.addLayout(decryptor_panel, stretch=2)

        main_vbox_layout.addLayout(table_and_decryptor_panel)
        self.setLayout(main_vbox_layout)

    def update_decrypt_record(self, record):
        self.record_data.setText(record.get_record_hexstring())

    # Decrypt function, beeeeicly
    def on_button_click(self):
        if self.data_model.model["decrypt_data"].get("record"):
            record_data = self.data_model.model["decrypt_data"]["record"].get_record_bytes()
            decryptor = self.decryptor_selector_widget.get_selected_decryptor()
            generator = None 
            if decryptor == "xor":
                generator = xor_decryptor(record_data, self.decryptor_selector_widget.get_xor_options())
            else: 
                print("NOT IMPLEMENTED")
                return 

            ev_name = self.evaluator_widget.get_selected_evaluator()
            ev_lambda = self.data_model.get_evaluator_lambda(ev_name)
            next_batch = []
            for (possible_decryption, key) in generator:

                if len(next_batch) == 100:
                    # add batch into model for table
                    self.table.add_batch_to_table(next_batch)
                    next_batch = []

                evaluation = ev_lambda(possible_decryption)
                if evaluation is not None:       

                    score, misc = evaluation
                    hexkey = ''.join([f"{x:02X}" for x in key])
                    next_batch.append([possible_decryption.hex(), score, hexkey, misc])

            # TODO: add the last batch here
            self.table.add_batch_to_table(next_batch)
            next_batch = []
                    
        else:
            print("nothing there dumbass")