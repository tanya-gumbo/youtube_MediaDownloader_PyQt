from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QStackedWidget, QListWidget


class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 300)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, False)
        self.contents_pane = QStackedWidget()

    def define_ui(self):
        """Defines elements of the UI"""
        settings_pane = QListWidget()
        self.setFixedSize(500, 300)
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
