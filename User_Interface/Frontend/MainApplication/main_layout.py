from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QLabel, QVBoxLayout, QCheckBox, QButtonGroup, QPushButton

from User_Interface.Frontend.MainApplication.download_functionality import VideoDownloader


class MainLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.youtube_link_entry = QLineEdit()
        self.link_label = QLabel("Link Entry")
        self.download_button = QPushButton()
        self.main_layout = QVBoxLayout()
        self.mp3_checkbox = QCheckBox()
        self.mp4_checkbox = QCheckBox()
        self.checkbox_button_group = QButtonGroup()
        self.checkbox_buttons_box = QHBoxLayout()
        self.define_ui()

    def define_ui(self):
        # Add entry label and entry point for Youtube link to main layout
        self.youtube_link_entry.resize(30, 60)
        user_entry_items_container = QHBoxLayout()
        user_entry_items_container.addWidget(self.link_label)
        user_entry_items_container.addWidget(self.youtube_link_entry)
        self.main_layout.addLayout(user_entry_items_container)

        # Add checkboxes to button group
        self.mp3_checkbox.setText("mp3")
        # self.mp3_checkbox.clicked.connect(self.checkbox_clicked)
        self.mp4_checkbox.setText("mp4")
        # self.mp4_checkbox.clicked.connect(self.checkbox_clicked)
        self.checkbox_button_group.addButton(self.mp3_checkbox)
        self.checkbox_button_group.addButton(self.mp4_checkbox)

        # add checkboxes and download button to main layout
        self.checkbox_buttons_box.addWidget(self.mp3_checkbox)
        self.checkbox_buttons_box.addWidget(self.mp4_checkbox)
        # self.download_button.clicked.connect(self.download_button_clicked)
        self.download_button.setText("Download")
        self.checkbox_buttons_box.addWidget(self.download_button)
        self.main_layout.addLayout(self.checkbox_buttons_box)

        self.setLayout(self.main_layout)
