from PyQt6.QtWidgets import QDialog


class UserProfile(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Profile")
        self.setGeometry(100, 100, 400, 300)

    def define_ui(self):
        pass