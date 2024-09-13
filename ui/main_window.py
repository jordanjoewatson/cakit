from PyQt6.QtWidgets import QMainWindow, QTabWidget
from PyQt6.QtGui import QAction
from ui.main_window_actions import MainWindowActions

from ui.home_widget import HomeWidget
from ui.stats_widget import StatsTab
from ui.decrypt_tab import DecryptTab

class MainWindow(QMainWindow):
    def __init__(self, data_model):
        super().__init__()
        self.actions = MainWindowActions(data_model, self)

        self.setWindowTitle("cakit")
        self.setGeometry(100, 100, 800, 600)

        self.menu = self.menuBar()
        self.menu.setNativeMenuBar(False)
        file_menu = self.menu.addMenu('File')
        load_directory_action = QAction("Load directory", self)
        load_directory_action.triggered.connect(self.actions.load_directory)
        file_menu.addAction(load_directory_action)

        load_string_action = QAction("Load string", self)
        load_string_action.triggered.connect(self.actions.load_string)
        file_menu.addAction(load_string_action)

        # Initialize the tab widget
        self.tab_widget = QTabWidget()
        
        # Create and add tabs
        # TODO: Rename widget below to tab
        self.home_tab = HomeWidget(data_model)
        self.stats_tab = StatsTab(data_model)
        self.decrypt_tab = DecryptTab(data_model)

        data_model.signal_decrypt_data_updated.connect(self.decrypt_tab.update_decrypt_record)
        
        self.tab_widget.addTab(self.home_tab, "home")
        self.tab_widget.addTab(self.stats_tab, "stats")
        self.tab_widget.addTab(self.decrypt_tab, "decrypt")
        
        # Set the tab widget as the central widget
        self.setCentralWidget(self.tab_widget)
