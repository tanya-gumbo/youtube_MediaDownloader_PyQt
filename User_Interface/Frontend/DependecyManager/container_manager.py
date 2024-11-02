from User_Interface.Frontend.DependecyManager.container import Container
from User_Interface.Frontend.MainApplication.download_functionality import VideoDownloader
from User_Interface.Frontend.MainApplication.main_layout import MainLayout, CustomStatusMenuItems
from User_Interface.Frontend.MainApplication.main_window import MainWindow
from User_Interface.Frontend.SettingsWindow.Settings import Settings

def register_dependencies_in_container():
    container = Container()
    container.register('settings', Settings)
    container.register('vid_downloader', VideoDownloader)
    container.register('custom_status_menu_items', CustomStatusMenuItems)
    # container.register('side_menu', SideMenu, container.resolve('settings'))
    container.register('main_layout', MainLayout)
    container.register('main_window', MainWindow)
    return container