import sys
from PyQt6.QtWidgets import QApplication
from User_Interface.Frontend.MainApplication.UI import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    # create the default download folder when the app starts
    app.aboutToQuit.connect(MainWindow.create_download_folder_on_startup)
    sys.exit(app.exec())
