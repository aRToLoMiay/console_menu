class MenuItem:
    def __init__(self, name, action=None, sub_menu=None):
        self.name = name
        self.action = action
        self.sub_menu = sub_menu
        self.type = self._determine_type()


    def _determine_type(self):
        if self.action is not None:
            return "action"
        elif self.sub_menu is not None:
            return "submenu"
        else:
            return "empty"


    def execute(self, current_menu):
        if self.action:
            self.action()
        elif self.sub_menu:
            self.sub_menu.run()


    def get_name(self):
        return self.name


    def get_type(self):
        return self.type
