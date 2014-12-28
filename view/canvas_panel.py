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
ROWS = 8
COLUMNS = 10
GRID_COLOR = "#808080"
SPECTRUM_COLOR = "#00ff00"

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

        self.canvas = self._init_canvas()

    def _init_canvas(self):
        canvas = Canvas(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background=CANVAS_BACKGROUND)
        canvas.pack(side=TOP)
        return canvas

    def draw_grid(self, freq_range, db_range):
        self._draw_horizontal_lines(db_range)
        self._draw_vertical_lines(freq_range)

    def _draw_horizontal_lines(self, db_range):
        top_left_x = LEFT_TOP_GRID_X_POSITION
        top_right_x = CANVAS_WIDTH - LEFT_TOP_GRID_X_POSITION
        cell_height = GRID_HEIGHT / ROWS

        db_per_row = (db_range['max'] - db_range['min']) / ROWS

        lines = [
            (top_left_x, y, top_right_x, y) for y in
            [LEFT_TOP_GRID_Y_POSITION + cell_number * cell_height for cell_number in xrange(ROWS + 1)]
        ]

        descriptions = [
            (line[0] - 10, line[1], str(db_range['max'] - i * db_per_row))
            for i, line in zip(xrange(ROWS + 1), lines)[:-1]
        ]

        self._draw_descriptions(descriptions)
        self._draw_lines(lines)

    def _draw_vertical_lines(self, freq_range):
        left_top_y = LEFT_TOP_GRID_Y_POSITION
        left_bottom_y = CANVAS_HEIGHT - LEFT_TOP_GRID_Y_POSITION
        cell_width = GRID_WIDTH / COLUMNS

        freq_per_column = (freq_range['max'] - freq_range['min']) / COLUMNS

        lines = [
            (x, left_top_y, x, left_bottom_y) for x in
            [LEFT_TOP_GRID_X_POSITION + cell_number * cell_width for cell_number in xrange(COLUMNS + 1)]
        ]

        descriptions = [
            (line[0], line[3] + 10, str(freq_range['min'] + i * freq_per_column))
            for i, line in zip(xrange(COLUMNS + 1), lines)[1:]
        ]

        self._draw_descriptions(descriptions)
        self._draw_lines(lines)

    def _draw_lines(self, lines):
        for line in lines:
            self.canvas.create_line(line, fill=GRID_COLOR)

    def draw_spectrum(self, db_range, freq_range, spectrum):
        self.clear_canvas()
        self.draw_grid(freq_range, db_range)
        self.canvas.create_line(spectrum, fill=SPECTRUM_COLOR)

    def clear_canvas(self):
        self.canvas.delete('all')

    def do_after(self, delay, function):
        self.canvas.after(delay, function)

    def _draw_descriptions(self, descriptions):
        for description in descriptions:
            self.canvas.create_text(
                description[0], description[1],
                text=description[2], fill=GRID_COLOR
            )
