from Tkconstants import RIDGE, TOP, X, RIGHT, LEFT
from Tkinter import Frame, Canvas, Button
from view.bottom_panel import BUTTON_WIDTH

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
        self._init_buttons()

    def _init_canvas(self):
        canvas = Canvas(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background=CANVAS_BACKGROUND)
        canvas.pack(side=TOP)
        return canvas

    def draw_text(self, sample_size):
        info = "FFT samples: " + sample_size
        return self.canvas.create_text(CANVAS_WIDTH / 2, LEFT_TOP_GRID_Y_POSITION / 2, text=info, fill=GRID_COLOR)

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
            for i, line in zip(xrange(COLUMNS + 1), lines)
        ]

        self._draw_descriptions(descriptions)
        self._draw_lines(lines)

    def _draw_lines(self, lines):
        for line in lines:
            self.canvas.create_line(line, fill=GRID_COLOR)

    def draw_spectrum(self, sample_size, db_range, freq_range, spectrum):
        self.clear_canvas()
        self.draw_text(sample_size)
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

    def _init_buttons(self):
        self.start_button = self.__init_button(button_caption="Start", button_position=LEFT,
                                                     button_callback=self.presenter.start_sweep)
        self.stop_button = self.__init_button(button_caption="Stop", button_position=LEFT,
                                                     button_callback=self.presenter.stop_sweep)
        self.start_freq_button = self.__init_button(button_caption="Start freq", button_position=LEFT,
                                                    button_callback=self.presenter.read_start_freq)
        self.end_freq_button = self.__init_button(button_caption="End freq", button_position=LEFT,
                                                  button_callback=self.presenter.read_stop_freq)
        self.dec_samples_button = self.__init_button(button_caption="-Samples", button_position=LEFT,
                                                     button_callback=self.presenter.get_sound_reader().dec_samples)
        self.inc_samples_button = self.__init_button(button_caption="+Samples", button_position=LEFT,
                                                     button_callback=self.presenter.get_sound_reader().inc_samples)
        self.db_div_up_button = self.__init_button(button_caption="+db/div", button_position=LEFT,
                                                     button_callback=self.presenter.inc_decibel_div)
        self.db_div_down_button = self.__init_button(button_caption="-db/div", button_position=LEFT,
                                                     button_callback=self.presenter.dec_decibel_div)
        self.db_level_up_button = self.__init_button(button_caption="+db level", button_position=LEFT,
                                                     button_callback=self.presenter.inc_db_level)
        self.db_level_down_button = self.__init_button(button_caption="-db level", button_position=LEFT,
                                                     button_callback=self.presenter.dec_db_level)

    def __init_button(self, button_caption, button_position, button_callback=None):
        button = Button(self, text=button_caption, width=BUTTON_WIDTH, command=button_callback)
        button.pack(side=button_position, padx=5, pady=5)
        return button