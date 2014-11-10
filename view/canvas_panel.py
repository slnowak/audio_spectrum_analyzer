from Tkconstants import RIDGE, TOP, X
from Tkinter import Frame, Canvas

__author__ = 'novy'

BACKGROUND = "black"
BORDER_WIDTH = 5
RELIEF = RIDGE

# todo: fix it somehow
GRID_WIDTH = 800                  # Width of the grid
GRID_HEIGHT = 400                  # Height of the grid
X0L = 20                    # Left top X value of grid
Y0T = 25                    # Left top Y value of grid
CANVAS_WIDTH = GRID_WIDTH + 2 * X0L
CANVAS_HEIGHT = GRID_HEIGHT + 80
CANVAS_BACKGROUND = "#000000"


class CanvasPanel(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        Frame.__init__(self, master, cnf,
                       background=BACKGROUND,
                       borderwidth=BORDER_WIDTH,
                       relief=RELIEF)

        self.pack(side=TOP, expand=1, fill=X)

        self.canvas = self.__init_canvas()

    def __init_canvas(self):
        canvas = Canvas(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background=CANVAS_BACKGROUND)
        canvas.pack(side=TOP)
        return canvas