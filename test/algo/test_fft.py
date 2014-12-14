import numpy
import numpy.testing
from unittest import TestCase

import algo.fft as cyt


__author__ = 'novy'

SOUND_SAMPLE = [
    -1.0454864643287543e-16, 4.846319866662846e-07, 1.938284923694356e-06, 4.360823082168972e-06,
    7.751465544800973e-06, 1.2111556301075734e-05, 1.7442823466806953e-05, 2.374680510995941e-05,
    3.102209392876061e-05, 3.927019835191851e-05, 4.848999333041171e-05, 5.868834958071126e-05,
    6.986315603283535e-05, 8.202564686887153e-05, 9.51935843710725e-05, 0.00010932979398867541,
    0.00012444778473455313, 0.00014058776539047432, 0.000157731874181258, 0.00017587051928744262,
    0.00019500410702421808, 0.00021515049078745007, 0.00023636337626591154, 0.00025857710215897693,
    0.000281812647758827, 0.00030609851604547717, 0.00033141714919009537, 0.0003578310397090338,
    0.0003853100053466747, 0.00041379384372002226, 0.00044340360793714836, 0.0004740805966332837
]


class TestFft(TestCase):
    def test_fft_with_sound_sample(self):
        expected_fft_result = numpy.fft.fft(SOUND_SAMPLE, len(SOUND_SAMPLE))
        fft_result = cyt.fourier(SOUND_SAMPLE,len(SOUND_SAMPLE))

        numpy.testing.assert_array_almost_equal(fft_result, expected_fft_result)

    def test_fft_with_random_data(self):
        random_data = numpy.random.random(1024)
        expected_fft_result = numpy.fft.fft(random_data, len(random_data))

        numpy.testing.assert_array_almost_equal(expected_fft_result, cyt.fourier(random_data,len(random_data)))

