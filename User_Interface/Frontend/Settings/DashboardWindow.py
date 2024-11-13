from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QListWidget, QStackedWidget, QVBoxLayout, QHBoxLayout


class DashboardWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setWindowIcon(QIcon("User_Interface/Frontend/Settings/window_dash_icon.png"))
        self.setGeometry(100, 100, 600, 500)
        self.options_list = QListWidget()
        self.content_layout = QStackedWidget()
        self.define_ui()

    def define_ui(self):
        self.options_list.addItem("User profile")
        self.options_list.addItem("Stats on music")
        self.options_list.addItem("Music recommendation")
        self.options_list.setMaximumWidth(150)
        self.options_list.currentRowChanged(self.select_content_layout)

        window_layout = QHBoxLayout()
        window_layout.addWidget(self.options_list)
        window_layout.addWidget(self.content_layout)

        main_layout = QVBoxLayout()
        main_layout.addLayout(window_layout)
        self.setLayout(main_layout)

    def create_user_profile(self):
        """Create the user account content pane"""
        pass

    def create_stats_on_music(self):
        """Create the statistics on music pane"""
        pass

    def create_music_recommendations(self):
        """Create the music recommendations pane"""
        pass

    def select_content_layout(self, index):
        if index == 0:
            self.content_layout.setCurrentIndex(index)
        elif index == 1:
            self.content_layout.setCurrentIndex(index)
        elif index == 2:
            self.content_layout.setCurrentIndex(index)
