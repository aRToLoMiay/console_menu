from menu import Menu
from file_menu import create_file_menu

import msvcrt


def action1():
    print("Execute option 1")
    msvcrt.getch()


def setting_action1():
    print("Changing parameter 1...")
    msvcrt.getch()


def test_menu():
    # Create main menu.
    main_menu = Menu("Main menu")

    # Create submenus.
    settings_menu = Menu("Settings", main_menu, close_mode=True)
    info_menu = Menu("Information", main_menu)

    # Add main menu suboptions.
    main_menu.add_action_item("Option 1", action1)
    main_menu.add_action_item("Option 2", lambda: print("Execute option 2"))

    main_menu.add_submenu_item("Settings", settings_menu)
    main_menu.add_submenu_item("Information", info_menu)

    # Add settings suboprions.
    settings_menu.add_action_item("Change parameter 1", setting_action1)
    settings_menu.add_action_item("Change parameter 2", lambda: print("Changing parameter 2..."))
    settings_menu.add_action_item("Reset settnigs", lambda: print("Reset settings..."))
    settings_menu.add_action_item("Close settings menu", lambda: settings_menu.stop())

    # Add information suboptions.
    info_menu.add_action_item("About", lambda: print("Console menu v1.0"))
    info_menu.add_action_item("Help", lambda: print("Controls:\n"
        "Arrow Up/Down or W/S - navigation\n"
        "Enter or Space - choose menu option\n"
        "Esc - back/exit"))

    # Start main menu.
    main_menu.run()


selected_file = None
def test_file_menu():
    # Collect files information.
    from path_processor import get_app_path
    path = get_app_path()
    file_types = ('.py')

    # Create function for text extraction from menu.
    def file_action(text):
        def handler():
            global selected_file
            selected_file = text
        return handler
    action = file_action

    # Get and run menu.
    menu = create_file_menu(menu_title="py-files",
                            action=action,
                            path=path,
                            file_types=file_types)
    menu.run()
    print(f"Choosed option: {selected_file}")


if __name__ == "__main__":
    test_file_menu()
