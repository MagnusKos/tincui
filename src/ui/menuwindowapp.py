'''TKinter-based menu of the main window.
Author: MagnusKos
2024'''

from tkinter import *
from tkinter.ttk import *


class MenuApp:
    def __init__(self, win_inst) -> None:
        self.win_inst = win_inst
        self.menubar = Menu(self.win_inst)
        self.win_inst['menu'] = self.menubar
        self._menu_config()
        self._menu_net()
        self._menu_help()
        pass

    def _menu_config(self):
        self.menu_config = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_config, label="Setup")

    def _menu_net(self):
        self.menu_net = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_net, label="Network")

    def _menu_help(self):
        self.menu_help = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_help, label="Help")