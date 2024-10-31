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
        self.create_download_folder()


    def run(self):
        """Download the video as a mp4"""
        file_path = self.default_download_folder_path

        ydl_opts = {
            'outtmpl': f'{file_path}/%(title)s.%(ext)s',
            'format': 'best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.media_format,
                'preferredquality': '0',
            }],
            'progress_hooks': [self.download_progress_hook],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(self.download_link, download=True)
                video_title = info.get('title', 'Unknown')
                self.download_finished.emit(video_title)
            except Exception as e:
                self.download_finished.emit(f"Error: {e}")

    def download_progress_hook(self, d):
        if d['status'] == 'downloading':
            try:
                percent = int(float(d['_percent_str'].strip('%')))
                self.progress_updated.emit(percent)
            except (ValueError, KeyError):
                pass


    def create_download_folder(self):
        try:
            desktop_path = os.path.join(QDir.homePath(), "Desktop")
            download_folder_name = "VidDownloader"
            folder_path = os.path.join(desktop_path, download_folder_name)
            self.default_download_folder_path = os.path.abspath(folder_path)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        except Exception as e:
            print("Exception is", e)
