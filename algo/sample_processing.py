__author__ = 'novy'

from numpy import arange
from math import ceil
import numpy

from algo.fft import fft


def prepare_trace(sound_sample, sample_frequency):
    sample_length = len(sound_sample)

    frequency_points = generate_frequency_points(sample_length, sample_frequency)
    power_points = generate_power_points(sound_sample, sample_length)

    return frequency_points, power_points


def generate_frequency_points(sample_length, sample_frequency):
    frequency_points = arange(0, get_unique_points_number(sample_length), 1)
    return frequency_points * (sample_frequency / sample_length)


def generate_power_points(sound_sample, sample_length):
    unique_points_number = get_unique_points_number(sample_length)
    fft_data = fft(sound_sample)[0:unique_points_number]
    fft_data = abs(fft_data)
    fft_data /= float(sample_length)
    fft_data **= 2

    if sample_length % 2 > 0:
        fft_data[1:len(fft_data)] = fft_data[1:len(fft_data)] * 2
    else:
        fft_data[1:len(fft_data) - 1] = fft_data[1:len(fft_data) - 1] * 2

    return 10 * numpy.log10(fft_data)


def get_unique_points_number(sample_length):
    return ceil((sample_length + 1) / 2.0)
