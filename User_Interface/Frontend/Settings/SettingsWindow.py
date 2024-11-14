from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QDialog, QStackedWidget, QListWidget, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, \
    QLabel, QFormLayout, QLineEdit
from User_Interface.Frontend.Settings import JSON_file_methods as jsn

class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, False)
        self.contents_pane = QStackedWidget()
        self.define_ui()

    def define_ui(self):
        """Defines elements of the UI"""
        try:
            settings_pane = QListWidget()
            settings_pane.setMaximumWidth(100)
            settings_pane.addItem("Downloads")
            settings_pane.currentRowChanged.connect(self.display_pane)

            pane_box = QHBoxLayout()
            pane_box.addWidget(settings_pane)

            download_pane = self.create_downloads_pane()
            self.contents_pane.addWidget(download_pane)
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
        except Exception as e:
            print("The exception is", e)



    def create_downloads_pane(self):
        """Creates the downloads contents pane to be added to the content pane"""
        download_path_text = jsn.read_json_file_path()
        main_layout = QWidget()

        download_label = QLabel()
        download_label.setText("Download folder:")
        download_path = QLabel()
        download_path.setText(download_path_text)
        change_path_button = QPushButton("Change download folder")
        change_path_tool_tip = "Changes the default download folder"
        change_path_button.setToolTip(change_path_tool_tip)

        layout = QFormLayout()
        layout.addWidget(download_label)
        layout.addWidget(download_path)
        layout.addWidget(change_path_button)
        main_layout.setLayout(layout)
        return main_layout


    def display_pane(self, index):
        """Display the pane in the QStackWidget according to the index passed"""
        if index == 0:
            self.contents_pane.setCurrentIndex(index)
        elif index == 1:
            self.contents_pane.setCurrentIndex(index)

    def update_button_clicked(self):
        """Saves any changes made when the update button is clicked"""

    def cancel_button_clicked(self):
        """Closes the window"""

    def change_download_folder(self):
        """Changes the download folder where downloads are placed"""
