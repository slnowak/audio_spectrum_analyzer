from tkSimpleDialog import askstring
from algo.frequency_filtering import FrequencyFilterer
from algo.sample_processing import prepare_trace
from presenter.grid_scaling import GridScaler
from presenter.int_parser import IntParser
from presenter.sound_reader import SoundReader
from view.canvas_panel import ROWS

__author__ = 'novy'

DECIBELS_PER_ROW = 10

MIN_FREQUENCY = 0
MAX_FREQUENCY = 22000

DEFAULT_POWER_RANGE = {
    'min': 0, 'max': ROWS * DECIBELS_PER_ROW
}


class CanvasPresenter(object):
    def __init__(self, canvas_view=None, sound_reader=SoundReader(),
                 grid_scaler=GridScaler(power_per_row=DECIBELS_PER_ROW),
                 frequency_filterer=FrequencyFilterer(),
                 int_parser=IntParser()):
        self.canvas_view = canvas_view
        self.sound_reader = sound_reader
        self.frequency_filterer = frequency_filterer
        self.grid_scaler = grid_scaler
        self.int_parser = int_parser

        self.start_freq = MIN_FREQUENCY
        self.stop_freq = MAX_FREQUENCY

    def get_sound_reader(self):
        return self.sound_reader

    def drawing_loop(self):
        audio_sample = self.read_sound_sample()
        self.draw_spectrum(audio_sample)
        self.canvas_view.do_after(10, self.drawing_loop)

    def read_sound_sample(self):
        return self.sound_reader.get_sound_sample()

    def draw_spectrum(self, sound_sample):
        frequency, power = prepare_trace(sound_sample, self.sound_reader.rate)

        frequency_range = {'min': self.start_freq, 'max': self.stop_freq}
        filtered_freq, filtered_power = self.frequency_filterer.filter(
            frequency, power, frequency_range
        )

        frequency_scaled = self.grid_scaler.scale_frequency(filtered_freq)
        power_scaled = self.grid_scaler.scale_power(filtered_power)

        self.canvas_view.draw_spectrum(
            str(self.sound_reader.get_sample_size()),
            DEFAULT_POWER_RANGE,
            frequency_range,
            self._make_canvas_input(frequency_scaled, power_scaled)
        )

    def _make_canvas_input(self, x, y):
        return [
            list(coords_tuple) for coords_tuple in zip(x, y)
        ]

    # todo: consider extracting it somewhere else
    def read_start_freq(self):
        start_freq_string = askstring("Start frequency: ", "Value: " + str(self.start_freq) + " Hz\n\nNew value:\n")
        parsed_start_freq = self.int_parser.parse(start_freq_string)
        if parsed_start_freq is not None and frequency_range_valid(parsed_start_freq, self.stop_freq):
            self.start_freq = parsed_start_freq

    def read_stop_freq(self):
        stop_freq_string = askstring("Stop : ", "Value: " + str(self.stop_freq) + " Hz\n\nNew value:\n")
        parsed_stop_freq = self.int_parser.parse(stop_freq_string)
        if parsed_stop_freq is not None and frequency_range_valid(self.start_freq, parsed_stop_freq):
            self.stop_freq = parsed_stop_freq


def frequency_range_valid(start_freq, stop_freq):
    return MIN_FREQUENCY <= start_freq <= stop_freq <= MAX_FREQUENCY


