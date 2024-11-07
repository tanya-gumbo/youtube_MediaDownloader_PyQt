from PyQt6.QtCore import Qt, QDir, QThread
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QListWidget, QMainWindow, QDockWidget, QSpacerItem, QSizePolicy
from User_Interface.Frontend.MainApplication.main_layout import MainLayout
from User_Interface.Frontend.Settings import JSON_file_methods as jsn
from User_Interface.Frontend.Settings.Settings import SideBar, Settings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.side_bar = None
        self.main_layout = None
        self.media_format = "NOTHING"
        self.status_menu = QListWidget()
        self.video_title = ""
        self.define_main_window()

    def define_main_window(self):
        """Defines the main window which will be displayed to the user"""
        self.setWindowTitle("Youtube Downloader")
        self.setWindowIcon(QIcon("User_Interface/Frontend/MainApplication/download_icon.png"))
        self.setGeometry(100, 100, 400, 300)
        try:
            self.main_layout = MainLayout()
            self.side_bar = SideBar()

            central_widget = self.main_layout
            self.setCentralWidget(central_widget)

            #Add settings Dock to container sidebar
            dock_widget = QDockWidget(self)
            dock_widget.setTitleBarWidget(QWidget())  # Remove the title bar
            dock_widget.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)  # Disable features
            dock_widget.setFixedWidth(35)
            dock_widget.setWidget(self.side_bar)

            # Add settings sidebar to the window
            self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock_widget)

            #Add dock to the right side to offset left side
            right_side_spacer = QDockWidget()
            right_side_spacer.setTitleBarWidget(QWidget())
            right_side_spacer.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
            right_side_spacer.setFixedWidth(35)
            self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, right_side_spacer)
        except Exception as main_window_ex:
            print("error in main_window",main_window_ex)

    def showEvent(self, event):
        """Creates the download folder for the videos/audios when the window is loaded"""
        super().showEvent(event)
        if not event.spontaneous():
            folder_creator = Settings()
            download_path = folder_creator.create_download_folder_on_startup()
            if download_path is not None:
                jsn.update_json_file_path(download_path)