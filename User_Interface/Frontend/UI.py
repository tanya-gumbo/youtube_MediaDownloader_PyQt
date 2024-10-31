from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QListWidgetItem, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, \
    QCheckBox, QButtonGroup, QListWidget, QProgressBar
from click import progressbar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout(self)
        self.youtube_link_entry = QLineEdit(self)
        self.link_Label = QLabel("Link Entry")
        self.mp3_checkbox = QCheckBox(self)
        self.mp4_checkbox = QCheckBox(self)
        self.checkbox_buttons_box = QHBoxLayout(self)
        self.checkbox_button_group = QButtonGroup(self)
        self.download_button = QPushButton("Download")
        self.media_format = ""
        self.status_menu = QListWidget()
        self.video_title = ""
        self.progress_bar = QProgressBar()
        self.status_label = QLabel("Waiting for download...")
        self.define_ui()

    def define_ui(self):
        """Defines the core UI which will be displayed to the user"""
        self.setWindowTitle("Youtube Downloader")
        self.setWindowIcon(QIcon("User_Interface/Frontend/download_icon.png"))
        self.setGeometry(100, 100, 400, 300)
        self.setLayout(self.main_layout)

        # Add entry label and entry point for Youtube link to main layout
        self.youtube_link_entry.resize(30, 60)
        user_entry_items_container = QHBoxLayout()
        user_entry_items_container.addWidget(self.link_Label)
        user_entry_items_container.addWidget(self.youtube_link_entry)
        self.main_layout.addLayout(user_entry_items_container)

        # Add checkboxes to button group
        self.mp3_checkbox.setText("mp3")
        self.mp4_checkbox.setText("mp4")
        self.checkbox_button_group.addButton(self.mp3_checkbox)
        self.checkbox_button_group.addButton(self.mp4_checkbox)

        # add checkboxes and download button to main layout
        self.checkbox_buttons_box.addWidget(self.mp3_checkbox)
        self.checkbox_buttons_box.addWidget(self.mp4_checkbox)
        self.checkbox_buttons_box.addWidget(self.download_button)
        self.main_layout.addLayout(self.checkbox_buttons_box)

        self.add_status_menu()

    def checkbox_clicked(self, button):
        """Ensures the checkboxes remain exclusive and updates the media_format variable"""
        if button is self.mp3_checkbox:
            self.mp4_checkbox.setChecked(False)
            self.media_format = "mp3"
        elif button is self.mp4_checkbox:
            self.mp3_checkbox.setChecked(False)
            self.media_format = "mp4"


    def download_button_clicked(self):
        """Executes the download thread when the download button is clicked"""
        youtube_link = self.youtube_link_entry.text()
        if len(youtube_link) is 0:
            return


    def add_status_menu_items(self):
        """Adds the media name and the progress bar to the status menu(QListWidget) in the main window"""
        item = CustomStatusMenuItems(self.progress_bar)
        self.status_menu.addItem(item)
        self.status_menu.setItemWidget(item, item.widget)

    def update_progress_bar(self):
        """Updates the progress bar of the download"""
        pass

    def add_status_menu(self):
        """Adds the status menu and its components to the main window"""
        self.main_layout.addWidget(self.status_menu)

class CustomStatusMenuItems(QListWidgetItem):
    def __init__(self, progress_bar, status_label):
        super().__init__()
        progress_bar = progress_bar
        status_label = status_label
        self.layout = QVBoxLayout()
        self.layout.addWidget(progress_bar)
        self.layout.addWidget(status_label)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setSizeHint(self.widget.sizeHint())



