from venv import create

import httpx
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QLabel, QHBoxLayout, QPushButton, \
    QStackedLayout, QWidget, QMessageBox
from qasync import asyncSlot
from sqlalchemy import except_


# from User_Interface.Frontend.Settings.user_profile_button_utilities import register_button_clicked


class UserProfile(QDialog):
    """Class for user to register and login"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Profile")
        self.setGeometry(100, 100, 350, 250)
        self.username_entry = QLineEdit()
        self.password_entry = QLineEdit()
        self.user_profile_stacked = QStackedLayout()
        self.toggle_action = QAction()
        self.define_ui()

    def define_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 50, 20, 50)

        login_register_layout = self.create_user_login_and_register()
        self.user_profile_stacked.addWidget(login_register_layout)

        main_layout.addLayout(self.user_profile_stacked)
        self.setLayout(main_layout)


    def create_user_login_and_register(self):
        create_user_login_widget = QWidget()
        login_register_layout = QVBoxLayout()
        data_entry_form = QFormLayout()

        # Username and password entry
        username_label = QLabel()
        username_label.setText("Username: ")
        self.username_entry.setPlaceholderText('Enter your username')
        self.username_entry.setMaximumSize(200, 30)
        self.password_entry.setPlaceholderText("Enter your password")
        self.password_entry.setMaximumSize(200, 30)
        self.password_entry.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        password_label = QLabel()
        password_label.setText("Password: ")
        data_entry_form.addRow(username_label, self.username_entry)
        data_entry_form.addRow(password_label, self.password_entry)

        # Replace with path to your "eye open" icon
        self.toggle_action = QAction(self)
        self.toggle_action.setIcon(
            QIcon("User_Interface/Frontend/Settings/images/open_eye.png"))  # Make sure to set the icon immediately
        self.toggle_action.setToolTip("Show password")
        self.toggle_action.triggered.connect(self.toggle_password_visibility)

        # Add the eye action to the password input
        self.password_entry.addAction(self.toggle_action, QLineEdit.ActionPosition.TrailingPosition)

        # Login and register buttons
        button_box = QHBoxLayout()
        register_button = QPushButton("Sign up")
        register_button.setMaximumSize(100, 30)

        register_button.clicked.connect(self.register_button_clicked)
        login_button = QPushButton("Login")
        login_button.setMaximumSize(100, 30)
        login_button.clicked.connect(self.login_button_clicked)
        button_box.addWidget(register_button)
        button_box.addWidget(login_button)

        # Forgot password and need help buttons
        forgot_and_help_but_box = self.create_help_reset_pass_buttons()

        login_register_layout.addLayout(data_entry_form)
        login_register_layout.addLayout(button_box)
        login_register_layout.addLayout(forgot_and_help_but_box)

        create_user_login_widget.setLayout(login_register_layout)
        return create_user_login_widget

    def toggle_password_visibility(self):
        if self.password_entry.echoMode() == QLineEdit.EchoMode.Password:
            # Show password as plain text
            self.password_entry.setEchoMode(QLineEdit.EchoMode.Normal)
            self.toggle_action.setIcon(QIcon("User_Interface/Frontend/Settings/images/open_eye.png"))  # Change to "eye closed" icon
        else:
            # Hide password (set it to password mode)
            self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
            self.toggle_action.setIcon(QIcon("User_Interface/Frontend/Settings/images/img.png"))

    def create_help_reset_pass_buttons(self):
        button_box = QHBoxLayout()
        button_box.setSpacing(100)
        forgot_pass_button = QPushButton("Forgot password")
        forgot_pass_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;  /* Transparent background */
                border: none;                  /* No border */
                color: #ffffff;                /* Text color */
                font-size: 14px;               /* Font size */
            }
            QPushButton:hover {
                color: #a0a0a0;                /* Text color on hover */
            }
        """)

        help_button = QPushButton("Need Help?")
        help_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;  /* Transparent background */
                border: none;                  /* No border */
                color: #ffffff;                /* Text color */
                font-size: 14px;               /* Font size */
            }
            QPushButton:hover {
                color: #a0a0a0;                /* Text color on hover */
            }
        """)
        button_box.addWidget(forgot_pass_button)
        button_box.addWidget(help_button)
        return button_box


    @asyncSlot()
    async def register_button_clicked(self):
        print("In method")
        username = self.username_entry.text()
        password = self.username_entry.text()

        if not username and not password:
            print("Enter both username and password")
            return

        if not username or not password:
            print("All fields are mandatory")
            return

        try:
            async with httpx.AsyncClient(timeout=55) as client:
                response = await client.post(
                    "http://127.0.0.1:8000/register",
                    json={"user_name": username, "password": password}
                )
                if response.status_code == 200:
                    message = response.json()['message']
                    print("The message is", message)
                    QMessageBox().information(
                        self,
                        "Information",
                        message
                    )
                else:
                    return response.json()['message']
        except httpx.TimeoutException:
            print("Timeout exception")
        except httpx.RequestError:
            print("Server error")

    @asyncSlot()
    async def login_button_clicked(self):
        username = self.username_entry.text()
        password = self.username_entry.text()

        if not username and not password:
            print("Enter both username and password")
            return

        if not username or not password:
            print("All fields are mandatory")
            return

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://127.0.0.1:8000/login",
                    json={"user_name": username, "password": password}
                )
                if response.status_code == 200:
                    message = response.json()['message']
                    print("The message is", message)
                else:
                    print("The message is", response.json()['message'])
        except httpx.TimeoutException:
            print("Timeout exception")
        except httpx.RequestError:
            print("Server error")