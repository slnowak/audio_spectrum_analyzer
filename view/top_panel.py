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

        self.__add_buttons()

    def __add_buttons(self):
        self.setup_button = Button(self, text="Setup", width=BUTTON_WIDTH)
        self.setup_button.pack(side=RIGHT, padx=5, pady=5)

        self.audio_on_off_button = Button(self, text="Audio on/off", width=BUTTON_WIDTH)
        self.audio_on_off_button.pack(side=RIGHT, padx=5, pady=5)


