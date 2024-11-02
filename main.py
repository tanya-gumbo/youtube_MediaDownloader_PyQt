import sys
from PyQt6.QtWidgets import QApplication
from User_Interface.Frontend.MainApplication.main_window import MainWindow
from User_Interface.Frontend.MainApplication.main_layout import MainLayout
from User_Interface.Frontend.MainApplication.download_functionality import VideoDownloader
from User_Interface.Frontend.SettingsWindow.Settings import Settings
from User_Interface.Frontend.container import Container

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = container.resolve('main_window')
    main_window.show()
    sys.exit(app.exec())
