import os
import yt_dlp
from PyQt6.QtCore import QDir, QThread, pyqtSignal


class VideoDownloader(QThread):
    progress_updated = pyqtSignal(int)
    download_finished = pyqtSignal(str)

    def __init__(self, link, media_format, parent=None):
        super().__init__(parent)
        self.download_link = link
        self.default_download_folder_path = None
        self.media_format = media_format


