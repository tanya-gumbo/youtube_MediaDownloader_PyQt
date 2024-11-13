from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QListWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QStackedLayout, QPushButton, \
    QWidget


class DashboardWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setWindowIcon(QIcon("User_Interface/Frontend/Settings/window_dash_icon.png"))
        self.setGeometry(100, 100, 600, 500)
        self.options_list = QListWidget()
        self.content_layout = QStackedLayout()
        self.define_ui()

    def define_ui(self):
        try:
            self.options_list.addItem("User profile")
            self.options_list.addItem("Stats on music")
            self.options_list.addItem("Music recommendation")
            self.options_list.setMaximumWidth(150)
            self.options_list.currentRowChanged.connect(self.select_content_layout)

            user_profile = self.create_user_profile()
            stats_on_music = self.create_stats_on_music()
            music_recommendations = self.create_music_recommendations()

            self.content_layout.addWidget(user_profile)
            self.content_layout.addWidget(stats_on_music)
            self.content_layout.addWidget(music_recommendations)

            window_layout = QHBoxLayout()
            window_layout.addWidget(self.options_list)
            window_layout.addLayout(self.content_layout)
            main_layout = QVBoxLayout()
            main_layout.addLayout(window_layout)
            self.setLayout(main_layout)
        except Exception as e:
            traceback = e.__traceback__
            # Get the line number where the exception occurred
            line_number = traceback.tb_lineno
            print("The Dashboard error is", e, "and the line number is ", line_number)

    def create_user_profile(self):
        """Create the user account content pane"""
        widget = QWidget()
        example_layout = QVBoxLayout()
        one = QPushButton("User layout")
        example_layout.addWidget(one)
        widget.setLayout(example_layout)
        return widget

    def create_stats_on_music(self):
        """Create the statistics on music pane"""
        widget = QWidget()
        example_layout = QVBoxLayout()
        one = QPushButton("Music stats")
        example_layout.addWidget(one)
        widget.setLayout(example_layout)
        return widget

    def create_music_recommendations(self):
        """Create the music recommendations pane"""
        widget = QWidget()
        example_layout = QVBoxLayout()
        one = QPushButton("Music Recs")
        example_layout.addWidget(one)
        widget.setLayout(example_layout)
        return widget

    def select_content_layout(self, index):
        count = self.content_layout.count()
        print('The index is', index, "and the number of children is", count)
        if index == 0:
            self.content_layout.setCurrentIndex(index)
        elif index == 1:
            self.content_layout.setCurrentIndex(index)
        elif index == 2:
            self.content_layout.setCurrentIndex(index)
