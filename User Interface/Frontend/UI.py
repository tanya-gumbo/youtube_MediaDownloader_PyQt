from PyQt6.QtWidgets import QWidget, QListWidgetItem


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

    def checkbox_clicked(self):
        """Ensures the checkboxes remain exclusive and updates the format variable"""

    def download_button_clicked(self):
        """Executes the download thread when the download button is clicked"""
        pass

    def add_status_menu_items(self):
        """Adds the media name and the progress bar to the QListWidget in the main window"""
        pass

    def update_progress_bar(self):
        """Updates the progress bar of the download"""
        pass

class CustomStatusMenuItems(QListWidgetItem):
    def __init__(self):
        super().__init__()

