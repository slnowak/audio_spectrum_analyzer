from algo.frequency_filtering import FrequencyFilterer
from algo.sample_processing import prepare_trace
from presenter.grid_scaling import GridScaler
from presenter.sound_reader import SoundReader

__author__ = 'novy'

DECIBELS_PER_ROW = 10
CHUNK_SIZE = 1024


class CanvasPresenter(object):
    def __init__(self, canvas_view, sound_reader=SoundReader(),
                 grid_scaler=GridScaler(power_per_row=DECIBELS_PER_ROW),
                 frequency_filterer=FrequencyFilterer()):
        self.canvas_view = canvas_view
        self.sound_reader = sound_reader
        self.frequency_filterer=frequency_filterer
        self.grid_scaler = grid_scaler
        self.drawing_loop()

    def drawing_loop(self):
        audio_sample = self.read_sound_sample(CHUNK_SIZE)
        self.draw_spectrum(audio_sample)
        self.canvas_view.do_after(10, self.drawing_loop)

    def read_sound_sample(self, chunk_size):
        return self.sound_reader.get_sound_sample(chunk_size)

    def draw_spectrum(self, sound_sample):
        frequency, power = prepare_trace(sound_sample, self.sound_reader.rate)

        frequency_scaled = self.grid_scaler.scale_frequency(frequency)
        power_scaled = self.grid_scaler.scale_power(power)

        self.canvas_view.draw_spectrum(
            {'min': 0, 'max': 80},
            {'min': 0, 'max': 22000},
            self._make_canvas_input(frequency_scaled, power_scaled)
        )


    def _make_canvas_input(self, x, y):
        return [
            list(coords_tuple) for coords_tuple in zip(x, y)
        ]
