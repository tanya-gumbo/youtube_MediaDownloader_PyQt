from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QFrame, QHBoxLayout, QPushButton, QLabel, QFormLayout, QMessageBox
from User_Interface.Frontend.Settings import JSON_file_methods as jsn

class UserLoggedIn(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User profile")
        self.setGeometry(100, 100, 350, 250)
        self.define_ui()

    def define_ui(self):
        num_of_tokens = 3
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 50, 30, 50)

        label_layout = QFormLayout()
        label_layout.setSpacing(10)

        layout_title = QLabel()
        layout_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_title.setText("User Profile")
        layout_title.setStyleSheet("""QLabel{
                                            font-family: Times New Roman;
                                             font-size: 25px;
                                             font-style: bold;
                                             margin-bottom: 20px;
                                             background-position: center;
                                             }
        """)

        username_box = QHBoxLayout()
        username_box.setSpacing(50)
        user_name_label = QLabel()
        user_name_label.setText("Username")
        user_name = QLabel()
        user_name.setText("tanya123")
        username_box.addWidget(user_name_label)
        username_box.addWidget(user_name)

        password_box= QHBoxLayout()
        password_box.setSpacing(20)
        change_pass_button = QPushButton("Change password")
        change_pass_button.setMaximumSize(140, 50)
        password_label = QLabel("Password")
        password_box.addWidget(password_label)
        password_box.addWidget(change_pass_button)
        password_info = QLabel("Change password to login to your account.")

        divider = self.create_divider()
        divider1 = self.create_divider()
        divider2 = self.create_divider()
        divider3 = self.create_divider()

        label_layout.addWidget(layout_title)
        label_layout.addRow(divider)
        label_layout.addItem(username_box)
        label_layout.addRow(divider1)
        label_layout.addItem(password_box)
        label_layout.addWidget(password_info)
        label_layout.addRow(divider2)
        # Expand the info text to take available space

        log_out_button = QPushButton("Log out")
        log_out_button.clicked.connect(self.logout_button_clicked)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.cancel_button_clicked)
        button_box = QHBoxLayout()
        button_box.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        button_box.setSpacing(40)
        button_box.addWidget(log_out_button)
        button_box.addWidget(cancel_button)

        main_layout.addLayout(label_layout)
        main_layout.addLayout(button_box)
        self.setLayout(main_layout)

    def create_divider(self):
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setFrameShadow(QFrame.Shadow.Sunken)
        divider.setLineWidth(1)
        divider.setMidLineWidth(1)
        divider.setStyleSheet("color: gray;")
        return divider

    def logout_button_clicked(self):
        jsn.update_json_status("logged out")
        QMessageBox.information(
            self,
            "Logging out message",
            "User logged out successfully"
        )
        self.close()

    def cancel_button_clicked(self):
        self.close()