'''TKinter-based main window of the application.
Author: MagnusKos
2024'''

from tkinter import *
from tkinter import Misc, Variable, font as tkFont
from tkinter.ttk import *
from menuwindowapp import MenuApp
from peerctls import PeerListCtl, peerListTest

class WindowApp():
    def __init__(self, tkInst) -> None:
        self.varStatus = StringVar(value="Doing nothing.")
        self.tkInst = tkInst
        self.tkInst.title("tincui")
        self.tkInst.option_add('*tearOff', FALSE)   # disable deattaching, this is ugly
        self.tkInst.minsize(250, 150)
        self.tkInst.maxsize(250, 400)
        #self.tkInst.attributes("-toolwindow", True)
        self.tkInst.resizable(False, True)

        self.style = Style(self.tkInst)
        self.style.configure("TButton", font=(18))

        self._initVars()
        self._initWidgets()
        pass

    def _initVars(self):
        self.varStatus = StringVar(value="Doing nothing.")
        self.varAddrLoc = StringVar(value="Local:\taaa.bbb.ccc.ddd")
        self.varAddrGlo = StringVar(value="Global:\taaa.bbb.ccc.ddd")
        pass

    def _initWidgets(self):
        # create
        self.menu = MenuApp(self.tkInst)
        self.frameStatus = Frame(self.tkInst, relief=GROOVE, height=32)
        self.frameConnection = Frame(self.tkInst, relief=GROOVE)
        self.butLog = Button(self.frameStatus, text="📜", width=3)
        self.butConnect = Button(self.frameConnection, text="🔌", width=3)
        self.labelStatus = Label(self.frameStatus, textvariable=self.varStatus, anchor="w")
        self.labelAddrGlo = Label(self.frameConnection, textvariable=self.varAddrGlo, anchor="w")
        self.labelAddrLoc = Label(self.frameConnection, textvariable=self.varAddrLoc, anchor="w")

        self.peerList = PeerListCtl(self.tkInst)

        # pack
        self.frameConnection.pack(side=TOP, fill=X, padx=2)
        self.butConnect.pack(side=LEFT, pady=2, padx=2)
        self.labelAddrGlo.pack(side=TOP, pady=2, padx=2)
        self.labelAddrLoc.pack(side=BOTTOM, pady=2, padx=2)

        self.peerList.pack(side=TOP, fill=BOTH, padx=2, pady=2)

        self.frameStatus.pack(side=BOTTOM, fill=X, padx=2)
        self.frameStatus.pack_propagate(0)
        self.labelStatus.pack(side=LEFT, expand=1, fill=X, padx=2)
        self.butLog.pack(side=RIGHT, padx=2)


class ToggleButton(Button):
    def __init__(self, master):
        super().__init__(master, command=self._toggle)

    def _toggle(self):
        if self.instate(['pressed']):
            self.state(['!pressed'])
        else:
            self.state(['pressed'])


if __name__ == "__main__":          # just for the test purposes: there is no entry point in this file
    tkInst = Tk()
    windowAppInst = WindowApp(tkInst)
    peerListTest(windowAppInst.peerList)
    tkInst.mainloop()
    pass