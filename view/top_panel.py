from Tkconstants import RIDGE, TOP, X, RIGHT
from Tkinter import Frame, Button

__author__ = 'novy'

FRAME_COLOR = "#000080"
BORDER_WIDTH = 5
RELIEF = RIDGE
BUTTON_WIDTH = 12


class TopPanel(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        Frame.__init__(self, master, cnf,
                       background=FRAME_COLOR,
                       borderwidth=BORDER_WIDTH,
                       relief=RIDGE)

        self.pack(side=TOP, expand=1, fill=X)

    def add_buttons(self, callback):
        self.setup_button = Button(self, text="Sample rate", width=BUTTON_WIDTH, command=callback)
        self.setup_button.pack(side=RIGHT, padx=5, pady=5)


