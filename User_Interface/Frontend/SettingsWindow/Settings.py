import os

from PyQt6.QtCore import Qt, QSize, QDir
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy


class SideBar(QWidget):
    """Class that contains the sidebar to be added to the main Application window"""
    def __init__(self):
        super().__init__()
        self.side_menu_layout = QVBoxLayout()
        self.side_menu_layout.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)

        # Set spacing between buttons to 0
        self.side_menu_layout.setSpacing(0)
        self.settings_button = QPushButton()

        self.settings_button.setIcon(QIcon("User_Interface/Frontend/SettingsWindow/settings_icon.png"))
        self.settings_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.settings_button.setStyleSheet("background-color: transparent;border: none; padding: 0px;")
        self.settings_button.setIconSize(QSize(32, 19))  # Set the size of the icon
        self.settings_button.setFixedSize(35, 20)

        self.file_explorer_button = QPushButton()
        self.file_explorer_button.setIcon(QIcon("User_Interface/Frontend/SettingsWindow/file_explorer_icon.png"))
        self.file_explorer_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.file_explorer_button.setStyleSheet(
            "background-color: transparent; border: none; padding: 0px;"
        )
        self.file_explorer_button.setIconSize(QSize(32, 19))  # Set the size of the icon
        self.file_explorer_button.setFixedSize(35, 20)

        self.side_menu_layout.addWidget(self.file_explorer_button)
        self.side_menu_layout.addWidget(self.settings_button)
        self.setLayout(self.side_menu_layout)


class Settings:
    def __init__(self):
        self.download_path = ""


    def create_download_folder_on_startup(self):
        """Creates the download folder on startup if it already doesn't exist"""
        try:
            desktop_path = os.path.join(QDir.homePath(), "Desktop")
            download_folder_name = "VidDownloader1"
            folder_path = os.path.join(desktop_path, download_folder_name)
            default_download_folder_path = os.path.abspath(folder_path)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            return default_download_folder_path
        except Exception as e:
            print("Exception is", e)

    def settings_button_clicked(self):
        """Opens the settings window"""

    def file_explorer_button_clicked(self):
        """Opens the file location where the videos/audios are being downloaded"""