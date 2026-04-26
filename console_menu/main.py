from menu import Menu

# Example function.
def action1():
    print("Execute option 1")

def test_menu():
    # Create main menu.
    main_menu = Menu("Main menu")

    # Create submenus.
    settings_menu = Menu("Settings", main_menu)
    info_menu = Menu("Information", main_menu)

    # Add main menu suboptions.
    main_menu.add_action_item("Option 1", action1)
    main_menu.add_action_item("Option 2", lambda: print("Execute option 2"))

    main_menu.add_submenu_item("Settings", settings_menu)
    main_menu.add_submenu_item("Information", info_menu)

    # Add settings suboprions.
    settings_menu.add_action_item("Change parameter 1", lambda: print("Changing parameter 1..."))
    settings_menu.add_action_item("Change parameter 2", lambda: print("Changing parameter 2..."))
    settings_menu.add_action_item("Reset settnigs", lambda: print("Reset settings..."))
    settings_menu.add_action_item("Close settings menu", lambda: settings_menu.stop())

    # Add information suboptions.
    info_menu.add_action_item("About", lambda: print("Console menu v1.0"))
    info_menu.add_action_item("Help", lambda: print("Controls:\n"
        "Arrow Up/Down or W/S - navigation\n"
        "Enter or Space - choose menu option\n"
        "Esc - back/exit"))

    # Delete menu option demonstration (uncomment for testing).
    # main_menu.remove_item("Option 1")

    # Start main menu.
    main_menu.run()


if __name__ == "__main__":
    test_menu()
