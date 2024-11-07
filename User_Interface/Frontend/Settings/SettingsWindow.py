from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QStackedWidget, QListWidget, QHBoxLayout, QVBoxLayout, QPushButton


class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, False)
        self.contents_pane = QStackedWidget()
        self.define_ui()

    def define_ui(self):
        """Defines elements of the UI"""
        settings_pane = QListWidget()
        settings_pane.setMaximumWidth(100)

        pane_box = QHBoxLayout()
        pane_box.addWidget(settings_pane)
        pane_box.addWidget(self.contents_pane)

        update_and_cancel_button_box = QHBoxLayout()
        update_button = QPushButton("Update")
        cancel_button = QPushButton("Cancel")
        update_and_cancel_button_box.addWidget(update_button)
        update_and_cancel_button_box.addWidget(cancel_button)

        settings_window_layout = QVBoxLayout()
        settings_window_layout.addLayout(pane_box)
        settings_window_layout.addLayout(update_and_cancel_button_box)
        self.setLayout(settings_window_layout)

        self.setFixedSize(400, 300)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)


    def create_downloads_pane(self):
        """Creates the downloads pane to be added to the content pane"""

    def create_user_profile_pane(self):
        """Creates the user profile pane to be added to the content pane"""

    def display_pane(self, index):
        """Display the pane in the QStackWidget according to the index passed"""

    def update_button_clicked(self):
        """Saves any changes made when the update button is clicked"""

    def cancel_button_clicked(self):
        """Closes the window"""

    def change_download_folder(self):
        """Changes the download folder where downloads are placed"""
