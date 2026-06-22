from path_processor import collect_file_paths
from console_menu.menu import Menu

import os


def create_file_menu(menu_title: str, 
                     action,
                     path: str, 
                     file_types, 
                     recursive: bool = False):
    files = collect_file_paths(path, file_types, recursive)
    files = [os.path.relpath(file, path) for file in files]

    menu = Menu(title=menu_title, close_mode=True)
    for file in files:
        menu.add_action_item(file, action(file))
    return menu
