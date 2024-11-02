from PyQt6.QtWidgets import QProgressBar, QListWidgetItem, QLabel, QVBoxLayout, QWidget


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
