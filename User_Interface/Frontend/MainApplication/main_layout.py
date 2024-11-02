from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QLabel, QVBoxLayout, QCheckBox, QButtonGroup, QPushButton, \
    QListWidgetItem, QProgressBar, QListWidget
from User_Interface.Frontend.DependecyManager import container_manager as cont_mnger


class MainLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.dependency_manager = cont_mnger.register_dependencies_in_container()
        self.youtube_link_entry = QLineEdit()
        self.link_label = QLabel("Link Entry")
        self.download_button = QPushButton()
        self.main_layout = QVBoxLayout()
        self.mp3_checkbox = QCheckBox()
        self.mp4_checkbox = QCheckBox()
        self.media_format = ""
        self.checkbox_button_group = QButtonGroup()
        self.checkbox_buttons_box = QHBoxLayout()
        self.status_menu = QListWidget()
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
        self.mp3_checkbox.clicked.connect(self.checkbox_clicked)
        self.mp4_checkbox.setText("mp4")
        self.mp4_checkbox.clicked.connect(self.checkbox_clicked)
        self.checkbox_button_group.addButton(self.mp3_checkbox)
        self.checkbox_button_group.addButton(self.mp4_checkbox)

        # add checkboxes and download button to main layout
        self.checkbox_buttons_box.addWidget(self.mp3_checkbox)
        self.checkbox_buttons_box.addWidget(self.mp4_checkbox)
        # self.download_button.clicked.connect(self.download_button_clicked)
        self.download_button.setText("Download")
        self.checkbox_buttons_box.addWidget(self.download_button)
        self.main_layout.addLayout(self.checkbox_buttons_box)

        # Add QListWidget to the layout
        self.main_layout.addWidget(self.status_menu)
        self.setLayout(self.main_layout)

    def checkbox_clicked(self):
        """Updates the media_format variable"""
        if self.mp3_checkbox.isChecked():
            self.media_format = "mp3"
        elif self.mp4_checkbox.isChecked():
            self.media_format = "mp4"

    def add_status_menu_items(self):
        """Adds status menu items once a download is started"""
        status_menu_items = self.dependency_manager.resolve('custom_status_menu_items')
        self.status_menu.addItem(status_menu_items)
        self.status_menu.setItemWidget(status_menu_items, status_menu_items.widget)




class CustomStatusMenuItems(QListWidgetItem):
    def __init__(self):
        super().__init__()
        self.progress_bar = QProgressBar()
        self.status_label = QLabel("Waiting for download to start...")
        self.video_title = QLabel()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.video_title)
        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.status_label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setSizeHint(self.widget.sizeHint())

    def update_progress_bar(self, progress):
        """Updates the progress bar of the download"""
        self.progress_bar.setValue(progress)
        self.status_label.setText(f"Downloading... - {progress}%")

    def handle_download_finished(self, result):
        self.status_label.setText(result)

    def set_video_title(self, title):
        self.video_title.setText(title)
