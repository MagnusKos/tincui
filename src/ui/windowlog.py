'''TKinter-based log window of the application.
Author: MagnusKos
2024'''

from tkinter import *
from tkinter.ttk import *

class WindowLog():
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("Log")
        self.master.attributes("-toolwindow", True)
        self.master.minsize(200,450)
        self._initVars()
        self._initWidgets()
        pass

    def _initVars(self):
        pass

    def _initWidgets(self):
        self.textLog = TextWithScrolls(self.master)

        self.frameButtons = Frame(self.master, relief=GROOVE, height=32)
        self.butExport = Button(self.frameButtons, text="Export...")
        self.butClear = Button(self.frameButtons, text="Clear")

        self.textLog.pack(side=TOP, padx=2, pady=2)
        self.frameButtons.pack(side=BOTTOM, padx=2, pady=2)
        self.butClear.pack(side=LEFT, padx=2, pady=2)
        self.butExport.pack(side=RIGHT, padx=2, pady=2)
        pass


class TextWithScrolls(Frame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master=master, **kwargs)
        self.master = master
        self._initVars()
        self._initWidgets()

    def _initVars(self):
        pass

    def _initWidgets(self):
        self.text = Text(self, wrap="none")
        self.sbVert = Scrollbar(self, command=self.text.yview, orient="vertical")
        self.sbHori = Scrollbar(self, command=self.text.xview, orient="horizontal")

        self.text.configure(yscrollcommand=self.sbVert.set, xscrollcommand=self.sbHori.set)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.text.grid(row=0, column=0, sticky="nsew")
        self.sbVert.grid(row=0, column=1, sticky="ns")
        self.sbHori.grid(row=1, column=0, sticky="ew")
        pass


if __name__ == "__main__":          # just for the test purposes: there is no entry point in this file
    tkInst = Tk()
    windowLog = WindowLog(tkInst)
    tkInst.mainloop()
    pass