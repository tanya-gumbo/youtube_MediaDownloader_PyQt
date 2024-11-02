from PyQt6.QtCore import Qt, QDir
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QListWidget, QMainWindow, QDockWidget, QSpacerItem, QSizePolicy
from User_Interface.Frontend.DependecyManager import container_manager as cnt_mnger


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        dependency_manager = cnt_mnger.register_dependencies_in_container()
        self.main_layout = dependency_manager.resolve('main_layout')
        self.side_bar = dependency_manager.resolve('side_bar')
        self.media_format = "NOTHING"
        self.status_menu = QListWidget()
        self.video_title = ""
        self.define_main_window()

    def define_main_window(self):
        """Defines the main window which will be displayed to the user"""
        self.setWindowTitle("Youtube Downloader")
        self.setWindowIcon(QIcon("User_Interface/Frontend/MainApplication/download_icon.png"))
        self.setGeometry(100, 100, 400, 300)

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

    def showEvent(self, event):
        """Creates the download folder for the videos/audios when the window is loaded"""
        super().showEvent(event)
        #if not event.spontaneous():
            # folder_creator = Settings()
            # download_path = folder_creator.create_download_folder_on_startup()
            #if download_path is not None:
             #   jsn.update_json_file_path(download_path)