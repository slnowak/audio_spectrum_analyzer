from Tkconstants import RIDGE, TOP, X
from Tkinter import Frame, Canvas

__author__ = 'novy'

BACKGROUND = "black"
BORDER_WIDTH = 5
RELIEF = RIDGE

# todo: fix it somehow
GRID_WIDTH = 800
GRID_HEIGHT = 400
LEFT_TOP_GRID_X_POSITION = 20
LEFT_TOP_GRID_Y_POSITION = 20
HORIZONTAL_CELLS = 8
VERTICAL_CELLS = 10
GRID_COLOR = "#808080"

CANVAS_WIDTH = GRID_WIDTH + 2 * LEFT_TOP_GRID_X_POSITION
CANVAS_HEIGHT = GRID_HEIGHT + 2 * LEFT_TOP_GRID_Y_POSITION
CANVAS_BACKGROUND = "#000000"


class CanvasPanel(Frame):
    def __init__(self, master=None, cnf={}, presenter=None, **kw):
        Frame.__init__(self, master, cnf,
                       background=BACKGROUND,
                       borderwidth=BORDER_WIDTH,
                       relief=RELIEF)

        self.pack(side=TOP, expand=1, fill=X)

        self.presenter = presenter

        self.canvas = self.__init_canvas()
        self.draw_grid()

    def __init_canvas(self):
        canvas = Canvas(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background=CANVAS_BACKGROUND)
        canvas.pack(side=TOP)
        return canvas

    def draw_grid(self):
        self.__draw_horizontal_lines()
        self.__draw_vertical_lines()

    def __draw_horizontal_lines(self):
        top_left_x = LEFT_TOP_GRID_X_POSITION
        top_right_x = CANVAS_WIDTH - LEFT_TOP_GRID_X_POSITION
        cell_height = GRID_HEIGHT / HORIZONTAL_CELLS

        lines = [
            (top_left_x, y, top_right_x, y) for y in
            [LEFT_TOP_GRID_Y_POSITION + cell_number * cell_height for cell_number in xrange(HORIZONTAL_CELLS + 1)]
        ]

        self.__draw_lines(lines)

    def __draw_vertical_lines(self):
        left_top_y = LEFT_TOP_GRID_Y_POSITION
        left_bottom_y = CANVAS_HEIGHT - LEFT_TOP_GRID_Y_POSITION
        cell_width = GRID_WIDTH / VERTICAL_CELLS

        lines = [
            (x, left_top_y, x, left_bottom_y) for x in
            [LEFT_TOP_GRID_X_POSITION + cell_number * cell_width for cell_number in xrange(VERTICAL_CELLS + 1)]
        ]

        self.__draw_lines(lines)

    def __draw_lines(self, lines):
        for line in lines:
            self.canvas.create_line(line, fill=GRID_COLOR)
