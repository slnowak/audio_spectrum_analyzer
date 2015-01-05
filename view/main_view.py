from presenter.canvas_presenter import CanvasPresenter
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
        self.main_window.title(MAIN_WINDOW_CAPTION)

        self.top_panel = TopPanel(self.main_window)
        # todo: fix
        canvas_presenter = CanvasPresenter()
        self.top_panel.add_buttons(canvas_presenter.set_sample_rate)
        self.canvas_panel = CanvasPanel(self.main_window, presenter=canvas_presenter)
        canvas_presenter.canvas_view = self.canvas_panel
        canvas_presenter.drawing_loop()
