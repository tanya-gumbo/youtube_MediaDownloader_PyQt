from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QListWidgetItem, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, \
    QCheckBox, QButtonGroup


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.youtube_link_entry = QLineEdit()
        self.link_Label = QLabel("Link Entry")
        self.mp3_checkbox = QCheckBox()
        self.mp4_checkbox = QCheckBox()
        self.checkbox_buttons_box = QHBoxLayout()
        self.checkbox_button_group = QButtonGroup()
        self.download_button = QPushButton("Download")
        self.media_format = ""
        self.define_ui()

    def define_ui(self):
        """Defines the core UI which will be displayed to the user"""
        self.setWindowTitle("Youtube Downloader")
        self.setWindowIcon(QIcon("User_Interface/Frontend/download_icon.png"))
        self.setGeometry(100, 100, 400, 300)
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Add entry label and entry point for Youtube link to main layout
        user_entry_items_container = QHBoxLayout()
        user_entry_items_container.addWidget(self.link_Label)
        user_entry_items_container.addWidget(self.youtube_link_entry)
        main_layout.addWidget(user_entry_items_container)

        # Add checkboxes to button group then the horizontal layout
        self.mp3_checkbox.setText("mp3")
        self.mp4_checkbox.setText("mp4")
        self.checkbox_button_group.addButton(self.mp3_checkbox)
        self.checkbox_button_group.addButton(self.mp4_checkbox)
        self.checkbox_buttons_box.addWidget(self.checkbox_button_group)


    def checkbox_clicked(self, button):
        """Ensures the checkboxes remain exclusive and updates the media_format variable"""
        if button is self.mp3_checkbox:
            self.mp4_checkbox.setChecked(False)
            self.medai_format = "mp3"
        elif button is self.mp4_checkbox:
            self.mp3_checkbox.setChecked(False)
            self.media_format = "mp4"


    def download_button_clicked(self):
        """Executes the download thread when the download button is clicked"""
        pass

    def add_status_menu_items(self):
        """Adds the media name and the progress bar to the status menu(QListWidget) in the main window"""
        pass

    def update_progress_bar(self):
        """Updates the progress bar of the download"""
        pass

    def add_status_menu(self):
        """Adds the status menu and its components to the main window"""

class CustomStatusMenuItems(QListWidgetItem):
    def __init__(self):
        super().__init__()

