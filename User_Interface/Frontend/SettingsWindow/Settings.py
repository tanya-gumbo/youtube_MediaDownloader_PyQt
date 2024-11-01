from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class SideBar(QWidget):
    """Class that contains the side bar to be added to the main Application window"""
    def __init__(self):
        super().__init__()
        self.side_menu_layout = QVBoxLayout()
        self.settings_button = QPushButton()
        self.settings_button.setIcon(QIcon("settings icon.png"))
        self.settings_button.setIconSize(self.settings_button.size())
        self.file_explorer_button = QPushButton()
        self.file_explorer_button.setIcon(QIcon("file_explorer_icon.png"))
        self.file_explorer_button.setIconSize(self.file_explorer_button.size())
        self.side_menu_layout.addWidget(self.settings_button)
        self.side_menu_layout.addWidget(self.file_explorer_button)