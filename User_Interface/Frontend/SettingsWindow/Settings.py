from PyQt6.QtCore import Qt
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

        self.settings_button.setIcon(QIcon("img.png"))
        self.settings_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.settings_button.setStyleSheet("background-color: transparent;")

        self.file_explorer_button = QPushButton()
        self.file_explorer_button.setIcon(QIcon("file_explorer_icon.png"))
        self.file_explorer_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.file_explorer_button.setStyleSheet("background-color: transparent;")

        self.side_menu_layout.addWidget(self.file_explorer_button)
        self.side_menu_layout.addWidget(self.settings_button)
        self.setLayout(self.side_menu_layout)