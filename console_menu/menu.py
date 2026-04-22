import os
import sys
import msvcrt

from .menu_item import *


class Menu:
    class Actions:
        UP      = 1 # Change cursor position up.
        DOWN    = 2 # Change cursor position down.
        ENTER   = 3 # Activation menu option.
        ESC     = 4 # Back/reset action.
        EXIT    = 5 # End of menu execution.
        EMPTY   = 6 # No action.


    def __init__(self, title, parent_menu=None):
        self.title = title
        self.items = []
        self.selected_index = 0
        self.parent = parent_menu


    def run(self):
        running = True

        while running:
            self._display()

            action = self._get_action()

            if action == self.Actions.UP:
                if self.selected_index > 0:
                    self.selected_index -= 1
                elif self.items:
                    self.selected_index = len(self.items) - 1

            elif action == self.Actions.DOWN:
                if self.selected_index < len(self.items) - 1:
                    self.selected_index += 1
                elif self.items:
                    self.selected_index = 0

            elif action == self.Actions.ENTER:
                if self.selected_index < len(self.items):
                    self.items[self.selected_index].execute(self)

            elif action == self.Actions.ESC:
                if self.parent is not None:
                    return
                if self._confirm_exit() == self.Actions.ENTER:
                    running = False
                else:
                    self._display()


    def add_item(self, name, action=None, sub_menu=None):
        if action is not None:
            self.items.append(MenuItem(name, action, None))
        elif sub_menu is not None:
            self.items.append(MenuItem(name, None, sub_menu))
        else:
            self.items.append(MenuItem(name, None, None))


    def add_action_item(self, name, action):
        self.items.append(MenuItem(name, action, None))


    def add_submenu_item(self, name, sub_menu):
        self.items.append(MenuItem(name, None, sub_menu))


    def remove_item(self, name):
        self.items = [item for item in self.items if item.get_name() != name]

        if self.selected_index >= len(self.items) and self.items:
            self.selected_index = len(self.items) - 1


    def set_parent(self, parent_menu):
        self.parent = parent_menu


    def _display(self):
        self._clear_screen()
        print(f"{self.title}:")
        for i, item in enumerate(self.items):
            if i == self.selected_index:
                print(f" > [x] - {item.get_name()}")
            else:
                print(f"   [ ] - {item.get_name()}")
        print("Press Esc to exit.")


    def _clear_screen(self):
        os.system('cls') # Windows only.


    def _confirm_exit(self):
        self._clear_screen()
        print("Are you sure you want to exit?")

        while True:
            action = self._get_action()
            if action == self.Actions.ENTER or action == self.Actions.ESC:
                return action


    def _get_action(self):
        ch = msvcrt.getch()
            
        # Arrows returns 2 bytes: first - 0xE0 or 0x00.
        if ch == b'\xe0' or ch == b'\x00':
            ch2 = msvcrt.getch()
            if ch2 == b'H':  # Up arrow.
                return self.Actions.UP
            elif ch2 == b'P':  # Down arrow.
                return self.Actions.DOWN
            elif ch2 == b'M':  # Right arrow.
                return self.Actions.ENTER
            elif ch2 == b'K':  # Left arrow.
                return self.Actions.ESC
        else:
            ch_char = ch.decode('ascii', errors='ignore').lower()
            if ch_char == 'w':
                return self.Actions.UP
            elif ch_char == 's':
                return self.Actions.DOWN
            elif ch_char in ('\r', ' ', 'd', 'y'):  # Enter, Space, d, y
                return self.Actions.ENTER
            elif ch == b'\x1b' or ch_char in ('a', 'n'):  # Escape, a, n
                return self.Actions.ESC
        
        return self.Actions.EMPTY
