import sys
from PyQt6.QtGui import QFontDatabase, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout
from ui.main_window import MainWindow
from data.data_model import DataModel

def main():
    # Initialize the Qt application
    app = QApplication(sys.argv)
    
    # font_id = QFontDatabase.addApplicationFont('./resources/fonts/JetBrainsMono-Regular.ttf')
    # font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    # custom_font = QFont(font_family)
    # custom_font.setPointSize(10)
    # app.setFont(custom_font)

    # Create a shared data model
    data_model = DataModel()

    # Create the main application window
    main_window = MainWindow(data_model)
    main_window.show()

    # Start the application's event loop
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
