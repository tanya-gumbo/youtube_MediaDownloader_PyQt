import os
import User_Interface.Frontend.Settings.JSON_file_methods as jsn
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QMessageBox
from User_Interface.Frontend.Settings.DashboardWindow import DashboardWindow
from User_Interface.Frontend.Settings.SettingsWindow import SettingsWindow
from User_Interface.Frontend.Settings.UserProfile import UserProfile
from User_Interface.Frontend.Settings.user_logged_in_window import UserLoggedIn


class SideBar(QWidget):
    """Class that contains the sidebar to be added to the QDocketWidget in the main Application window"""
    def __init__(self):
        super().__init__()
        self.side_menu_layout = QVBoxLayout()
        self.side_menu_layout.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)

        # Set spacing between buttons to 0
        self.side_menu_layout.setSpacing(0)

        self.settings_button = QPushButton()
        self.settings_button.clicked.connect(self.settings_button_clicked)
        self.settings_button.setIcon(QIcon("User_Interface/Frontend/Settings/images/settings_icon.png"))
        self.settings_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.settings_button.setStyleSheet("background-color: transparent;border: none; padding: 0px;")
        self.settings_button.setIconSize(QSize(32, 19))  # Set the size of the icon
        self.settings_button.setFixedSize(35, 20)


        self.file_explorer_button = QPushButton()
        file_expl_tool_tip_text = "Opens folder which contains downloads"
        self.file_explorer_button.setToolTip(file_expl_tool_tip_text)
        self.file_explorer_button.clicked.connect(self.file_explorer_button_clicked)
        self.file_explorer_button.setIcon(QIcon("User_Interface/Frontend/Settings/images/file_explorer_icon.png"))
        self.file_explorer_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.file_explorer_button.setStyleSheet(
            "background-color: transparent; border: none; padding: 0px;"
        )
        self.file_explorer_button.setIconSize(QSize(32, 19))  # Set the size of the icon
        self.file_explorer_button.setFixedSize(35, 20)

        self.dashboard_button = QPushButton()
        dashboard_tool_tip = "Opens the user dashboard"
        self.dashboard_button.setToolTip(dashboard_tool_tip)
        self.dashboard_button.clicked.connect(self.dashboard_button_clicked)
        self.dashboard_button.setIcon(QIcon("User_Interface/Frontend/Settings/images/dashboard.png"))
        self.dashboard_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.dashboard_button.setStyleSheet(
            "background-color: transparent; border: none; padding: 0px;"
        )
        self.dashboard_button.setIconSize(QSize(32, 19))  # Set the size of the icon
        self.dashboard_button.setFixedSize(35, 20)

        self.user_profile_button = QPushButton()
        user_profile_tool_tip = "Opens the user profile for sign in or sign out"
        self.user_profile_button.setToolTip(user_profile_tool_tip)
        self.user_profile_button.clicked.connect(self.user_profile_button_clicked)
        self.user_profile_button.setIcon(QIcon("User_Interface/Frontend/Settings/images/user_profile.png"))
        self.user_profile_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.user_profile_button.setStyleSheet(
            "background-color: transparent; border: none; padding: 0px;"
        )
        self.user_profile_button.setIconSize(QSize(32, 19))  # Set the size of the icon
        self.user_profile_button.setFixedSize(35, 20)

        self.side_menu_layout.addWidget(self.dashboard_button)
        self.side_menu_layout.addWidget(self.file_explorer_button)
        self.side_menu_layout.addWidget(self.settings_button)
        self.side_menu_layout.addWidget(self.user_profile_button)
        self.setLayout(self.side_menu_layout)

    def settings_button_clicked(self):
        """Opens the settings window"""
        settings_window = SettingsWindow()
        settings_window.exec()

    def file_explorer_button_clicked(self):
        """Opens the file location where the videos/audios are being downloaded"""
        file_path = jsn.read_json_file_path()
        os.startfile(file_path)

    def dashboard_button_clicked(self):
        try:
            user_status = jsn.read_json_status()
            if user_status == "logged in":
                dashboard_window = DashboardWindow()
                dashboard_window.exec()
            else:
                QMessageBox().information(
                    self,
                    "Error",
                    "You cannot access the dashboard if you aren't logged in. \nNavigate to the user profile to log in"
                )
        except Exception as e:
            print("The exception in dash", e)

    def user_profile_button_clicked(self):
        user_status = jsn.read_json_status()
        if user_status == "logged out":
            user_profile = UserProfile()
            user_profile.exec()
        else:
            logged_in_window = UserLoggedIn()
            logged_in_window.exec()
