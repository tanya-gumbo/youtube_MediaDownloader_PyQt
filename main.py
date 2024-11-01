import sys
from PyQt6.QtWidgets import QApplication
from User_Interface.Frontend.MainApplication.UI import MainWindow
from User_Interface.Frontend.SettingsWindow.Settings import Settings

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
