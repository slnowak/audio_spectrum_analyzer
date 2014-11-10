import numpy
import numpy.testing
from unittest import TestCase

from algo.fft import get_nearest_greater_power_of_two, fft


__author__ = 'novy'

SOUND_SAMPLE = [
    -1.0454864643287543e-16, 4.846319866662846e-07, 1.938284923694356e-06, 4.360823082168972e-06,
    7.751465544800973e-06, 1.2111556301075734e-05, 1.7442823466806953e-05, 2.374680510995941e-05,
    3.102209392876061e-05, 3.927019835191851e-05, 4.848999333041171e-05, 5.868834958071126e-05,
    6.986315603283535e-05, 8.202564686887153e-05, 9.51935843710725e-05, 0.00010932979398867541,
    0.00012444778473455313, 0.00014058776539047432, 0.000157731874181258, 0.00017587051928744262,
    0.00019500410702421808, 0.00021515049078745007, 0.00023636337626591154, 0.00025857710215897693,
    0.000281812647758827, 0.00030609851604547717, 0.00033141714919009537, 0.0003578310397090338,
    0.0003853100053466747, 0.00041379384372002226, 0.00044340360793714836, 0.0004740805966332837,
    0.0005058502549208648, 0.0005387434775695361, 0.0005727028117229332, 0.00060780406138606,
    0.0006440346822749624, 0.000681404583894911, 0.0007198943178235634, 0.0007595720390277462,
    0.0008004204769686475, 0.0008423812616233688, 0.0008856375953750666, 0.0009301406948941051,
    0.0009757875963807524, 0.0010227057667499665, 0.0010707811627466233, 0.0011201531865727792,
    0.0011707927598336764, 0.001222713286074232, 0.0012760865785542933, 0.0013305622021779718,
    0.0013863562462678215, 0.0014437217920366323, 0.0015022679822467664
]


class TestFft(TestCase):
    def test_fft_with_sound_sample(self):
        expected_fft_result = numpy.fft.fft(SOUND_SAMPLE, self.padded_sample_len(SOUND_SAMPLE))
        fft_result = fft(SOUND_SAMPLE)

        numpy.testing.assert_array_almost_equal(fft_result, expected_fft_result)

    def test_fft_with_random_data(self):
        random_data = numpy.random.random(1024)
        expected_fft_result = numpy.fft.fft(random_data, n=self.padded_sample_len(random_data))

        numpy.testing.assert_array_almost_equal(expected_fft_result, fft(random_data))

    def test_fft_with_random_data_of_odd_length(self):
        random_data = numpy.random.random(1025)
        expected_fft_result = numpy.fft.fft(random_data, n=self.padded_sample_len(random_data))

        numpy.testing.assert_array_almost_equal(expected_fft_result, fft(random_data))

    def padded_sample_len(self, data):
        return get_nearest_greater_power_of_two(len(data))