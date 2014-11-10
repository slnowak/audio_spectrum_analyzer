import numpy as np
import cmath
import math

__author__ = 'novy'


def fft(signal):
    result = __fft(pad(signal))
    return np.array(result)


def __fft(signal):
    signal_length = len(signal)
    if signal_length == 1:
        return signal
    else:
        even_part = __fft([signal[i] for i in xrange(0, signal_length, 2)])
        odd_part = __fft([signal[i] for i in xrange(1, signal_length, 2)])

        combined = [0] * signal_length

        for i in xrange(signal_length/2):
            combined[i] = even_part[i] + omega(signal_length, -i) * odd_part[i]
            combined[i + signal_length/2] = even_part[i] - omega(signal_length, -i) * odd_part[i]

        return combined


def omega(p, q):
    return cmath.exp((2.0 * cmath.pi * 1j * q) / p)


def get_nearest_greater_power_of_two(number):
    return int(2 ** math.ceil(np.log2(number)))
    

def pad(input_list):
    list_length = len(input_list)
    return np.concatenate((input_list, [0] * (get_nearest_greater_power_of_two(list_length) - list_length)), 0)