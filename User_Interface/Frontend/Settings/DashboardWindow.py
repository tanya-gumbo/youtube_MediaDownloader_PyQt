from PyQt6.QtWidgets import QDialog, QListWidget


class DashboardWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.options_list = QListWidget()


    def define_ui(self):
        man = 11

