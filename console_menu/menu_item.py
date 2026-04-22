import msvcrt


class MenuItem:
    def __init__(self, name, action=None, sub_menu=None):
        self.name = name
        self.action = action
        self.sub_menu = sub_menu


    def execute(self, current_menu):
        if self.action:
            self.action()
            print("\nPress any key to continue...")
            self._getch_windows()
        elif self.sub_menu:
            self.sub_menu.run()


    def _getch_windows(self):
        return msvcrt.getch() # Windows only.


    def get_name(self):
        return self.name
