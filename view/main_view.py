from view.bottom_panel import BottomPanel
from view.canvas_panel import CanvasPanel
from view.top_panel import TopPanel

MAIN_WINDOW_CAPTION = "Audio spectrum analyzer"

__author__ = 'novy'

from Tkinter import *


class MainWindow(object):

    def __init__(self, presenter=None):
        self.presenter = presenter
        self.initialize_view()
        self.main_window.mainloop()

    def initialize_view(self):
        self.main_window = Tk()
        self.main_window .title(MAIN_WINDOW_CAPTION)

        top_panel = TopPanel(self.main_window)
        canvas_panel = CanvasPanel(self.main_window)
        bottom_panel = BottomPanel(self.main_window)