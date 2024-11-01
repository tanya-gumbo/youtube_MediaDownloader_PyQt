from PyQt6.QtCore import Qt, QDir
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QListWidgetItem, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, \
    QCheckBox, QButtonGroup, QListWidget, QProgressBar, QMainWindow, QDockWidget, QSpacerItem, QSizePolicy
from User_Interface.Frontend.MainApplication.download_functionality import VideoDownloader
from User_Interface.Frontend.SettingsWindow.Settings import SideBar, Settings
import User_Interface.Frontend.SettingsWindow.JSON_file_methods as jsn


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout(self)
        self.youtube_link_entry = QLineEdit(self)
        self.link_Label = QLabel("Link Entry")
        self.download_path = ""
        self.mp3_checkbox = QCheckBox(self)
        self.mp4_checkbox = QCheckBox(self)
        self.checkbox_buttons_box = QHBoxLayout(self)
        self.checkbox_button_group = QButtonGroup(self)
        self.download_button = QPushButton("Download")
        self.media_format = "NOTHING"
        self.status_menu = QListWidget()
        self.video_title = ""
        self.define_ui()

    def define_ui(self):
        """Defines the core UI which will be displayed to the user"""
        self.setWindowTitle("Youtube Downloader")
        self.setWindowIcon(QIcon("User_Interface/Frontend/MainApplication/download_icon.png"))
        self.setGeometry(100, 100, 400, 300)

        # Create the central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        # Add entry label and entry point for Youtube link to main layout
        self.youtube_link_entry.resize(30, 60)
        user_entry_items_container = QHBoxLayout()
        user_entry_items_container.addWidget(self.link_Label)
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
        self.download_button.clicked.connect(self.download_button_clicked)
        self.checkbox_buttons_box.addWidget(self.download_button)
        self.main_layout.addLayout(self.checkbox_buttons_box)

        self.add_status_menu()

        #Add settings sidebar to the window
        side_bar = SideBar()
        dock_widget = QDockWidget(self)
        dock_widget.setTitleBarWidget(QWidget())  # Remove the title bar
        dock_widget.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)  # Disable features
        dock_widget.setFixedWidth(35)
        dock_widget.setWidget(side_bar)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock_widget)

        right_side_spacer = QDockWidget()
        right_side_spacer.setTitleBarWidget(QWidget())
        right_side_spacer.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        right_side_spacer.setFixedWidth(35)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, right_side_spacer)

    def showEvent(self, event):
        """Creates the download folder for the videos/audios when the window is loaded"""
        super().showEvent(event)
        if not event.spontaneous():
            folder_creator = Settings()
            self.download_path = folder_creator.create_download_folder_on_startup()
            if self.download_path is not None:
                jsn.update_json_file_path(self.download_path)



    def add_status_menu_items(self):
        """Adds the media name and the progress bar to the status menu(QListWidget) in the main window"""
        status_label = QLabel()
        progress_bar = QProgressBar()
        status_label.setText("Waiting for download...")
        item = CustomStatusMenuItems(progress_bar, status_label)
        self.status_menu.addItem(item)
        self.status_menu.setItemWidget(item, item.widget)
        return item

    def add_status_menu(self):
        """Adds the status menu and its components to the main window"""
        self.main_layout.addWidget(self.status_menu)

    def checkbox_clicked(self):
        """Ensures the checkboxes remain exclusive and updates the media_format variable"""
        if self.mp3_checkbox.isChecked():
            self.media_format = "mp3"
        elif self.mp4_checkbox.isChecked():
            self.media_format = "mp4"
        print("The media format is", self.media_format)


    def download_button_clicked(self):
        """Executes the download thread when the download button is clicked"""
        youtube_link = self.youtube_link_entry.text()
        item = self.add_status_menu_items()
        # print("The media format is", self.media_format)
        self.download_thread = VideoDownloader(youtube_link, self.media_format)
        title = self.download_thread.get_video_title()
        item.set_video_title(title)
        self.download_thread.download_finished.connect(item.handle_download_finished)
        self.download_thread.progress_updated.connect(item.update_progress_bar)
        self.download_thread.start()


class CustomStatusMenuItems(QListWidgetItem):
    def __init__(self, default_progress_bar, default_status_label):
        super().__init__()
        self.progress_bar = default_progress_bar
        self.status_label = default_status_label
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
