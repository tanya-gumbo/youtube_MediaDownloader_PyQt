import sys
from PyQt6.QtCore import Qt
from PyQt6.QtTest import QTest
from PyQt6.QtWidgets import QApplication

from User_Interface.Frontend.UI import MainWindow
def test_define_ui():
    """tests if the main ui method is adding the label, entry field, download button, check boxes and status menu to
    the window"""

def test_add_status_menu():
    """tests if the status menu method is being added to the main window"""


def test_checkbox_clicked():
    """Tests to see if the media_format variable is updated"""
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window2 = MainWindow()

    QTest.mouseClick(main_window.mp4_checkbox, Qt.MouseButton.RightButton)
    main_window.checkbox_clicked(main_window.mp4_checkbox)
    assert main_window.media_format == "mp4"

    # Clean up
    app.quit()

