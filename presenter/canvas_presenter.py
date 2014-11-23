from algo.sample_processing import prepare_trace
from presenter.sound_reader import SoundReader
from view.canvas_panel import LEFT_TOP_GRID_X_POSITION, GRID_WIDTH, GRID_HEIGHT, LEFT_TOP_GRID_Y_POSITION, ROWS, \
    DECIBELS_PER_ROW

__author__ = 'novy'

CHUNK_SIZE = 1024


class CanvasPresenter(object):
    def __init__(self, canvas_view, sound_reader=SoundReader()):
        self.canvas_view = canvas_view
        self.sound_reader = sound_reader
        self.drawing_loop()

    def drawing_loop(self):
        audio_sample = self.read_sound_sample(CHUNK_SIZE)
        self.draw_spectrum(audio_sample)
        self.canvas_view.do_after(10, self.drawing_loop)

    def read_sound_sample(self, chunk_size):
        return self.sound_reader.get_sound_sample(chunk_size)

    def draw_spectrum(self, sound_sample):
        frequency, power = prepare_trace(sound_sample, self.sound_reader.rate)
        frequency_scaled = self._scale_frequency_points(frequency)
        power_scaled = self._scale_power_points(power)

        self.canvas_view.draw_spectrum(
            self._make_canvas_input(frequency_scaled, power_scaled)
        )

    def _scale_frequency_points(self, frequency_points):
        pixels_per_frequency_gap = float(GRID_WIDTH) / len(frequency_points)
        return [
            int(i * pixels_per_frequency_gap + LEFT_TOP_GRID_X_POSITION)
            for i in xrange(len(frequency_points))
        ]

    def _scale_power_points(self, power_points):
        # todo this should be probably done in a smarter way...
        with_negative_power_replaced = [
            power if power >= 0 else 0 for power in power_points
        ]

        pixels_per_decibel = float(GRID_HEIGHT) / (ROWS * DECIBELS_PER_ROW)

        scaled = [
            int(GRID_HEIGHT - power * pixels_per_decibel)
            for power in with_negative_power_replaced
        ]

        return [
            LEFT_TOP_GRID_Y_POSITION if power < LEFT_TOP_GRID_Y_POSITION else power
            for power in scaled
        ]

    def _make_canvas_input(self, x, y):
        return [
            list(coords_tuple) for coords_tuple in zip(x, y)
        ]
