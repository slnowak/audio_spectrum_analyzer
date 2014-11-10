from Tkconstants import RIDGE, TOP, X, LEFT, RIGHT
from Tkinter import Frame, Button

__author__ = 'novy'

FRAME_COLOR = "#000080"
BORDER_WIDTH = 5
RELIEF = RIDGE
BUTTON_WIDTH = 8


class BottomPanel(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        Frame.__init__(self, master, cnf,
                       background=FRAME_COLOR,
                       borderwidth=BORDER_WIDTH,
                       relief=RIDGE)

        self.pack(side=TOP, expand=1, fill=X)
        self.__init_buttons()

    def __init_buttons(self):
        self.start_button = self.__init_button(button_caption="Start", button_position=LEFT)
        self.stop_button = self.__init_button(button_caption="Stop", button_position=LEFT)
        self.start_freq_button = self.__init_button(button_caption="Start freq", button_position=RIGHT)
        self.end_freq_button = self.__init_button(button_caption="End freq", button_position=RIGHT)

    def __init_button(self, button_caption, button_position, button_callback=None):
        button = Button(self, text=button_caption, width=BUTTON_WIDTH)
        button.pack(side=button_position, padx=5, pady=5)
        return button
