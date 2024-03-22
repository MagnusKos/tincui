'''TKinter-based classes (controls) for visualisation of peers of the network.
Author: MagnusKos
2024'''

from tkinter import *
from tkinter import Misc
from tkinter.ttk import *


class PeerListCtl(LabelFrame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.master = master
        self.configure(text="Peers",relief=RIDGE, height=32)

        self._initVars()
        self._initWidgets()

    def _initVars(self):
        self.peerCtls = {}  # {peerId : PeerCtl}
        pass

    def _initWidgets(self):
        pass

    def addPeerCtl(self, peerId, peerInfo):
        if peerId not in self.peerCtls:
            newPeerCtl = PeerCtl(master=self, peerInfo=peerInfo)
            newPeerCtl.pack(side=TOP, fill=X, pady=1, padx=1)
            self.peerCtls[peerId] = newPeerCtl
        pass

    def remPeerCtl(self, peerId):
        if peerId in self.peerCtls:
            self.peerCtls[peerId].destroy()
            self.peerCtls.pop(peerId)
        pass

    def updatePeerCtl(self, peerId, peerInfo):
        if peerId in self.peerCtls:
            self.peerCtls[peerId].update(peerInfo)
        pass


class PeerCtl(Frame):
    def __init__(self, peerInfo, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.master = master
        self.configure(relief=RAISED)

        self._initVars()
        self._initWidgets()
        self.update(peerInfo)

    def _initVars(self):
        self.peerInfo = {}  # {'hostname': String, 'ip': String, 'ping': Int, 'state': Bool}
        self.varPing = IntVar(value=-1)
        self.varPeer = StringVar(value="Vasya_Pupkin")
        pass

    def _initWidgets(self):
        self.labelPing = Label(self, textvariable=self.varPing, anchor="e")
        self.separator = Separator(self, orient='vertical')
        self.labelPeer = Label(self, textvariable=self.varPeer, anchor="w")

        self.labelPing.pack(side=LEFT, padx=2, pady=2)
        self.separator.pack(side=LEFT, padx=2, pady=2)
        self.labelPeer.pack(side=RIGHT, padx=2, pady=2)
        pass

    def update(self, peerInfo):
        self.peerInfo = peerInfo
        self.varPing.set(self.peerInfo['ping'])
        self.varPeer.set(self.peerInfo['hostname'])
        pass


def peerListTest(peerListCtl: PeerListCtl):
    peerListCtl.pack(fill=X, padx=2, pady=2)
    peerInfo1 = {'ping': 42, 'hostname': "dude"}
    peerInfo2 = {'ping': 1337, 'hostname': "undude"}
    peerListCtl.addPeerCtl(peerId=1, peerInfo=peerInfo1)
    peerListCtl.addPeerCtl(peerId=2, peerInfo=peerInfo2)
    pass


if __name__ == "__main__":
    tkInst = Tk()
    peerListCtl = PeerListCtl(tkInst)
    peerListTest(peerListCtl)
    tkInst.mainloop()