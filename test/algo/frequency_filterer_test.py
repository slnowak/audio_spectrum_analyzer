from unittest.case import TestCase
from algo.frequency_filtering import FrequencyFilterer

__author__ = 'novy'


class FrequencyFiltererTest(TestCase):
    def setUp(self):
        super(FrequencyFiltererTest, self).setUp()
        self.object_under_test = FrequencyFilterer()

    def test_should_raise_error_when_frequency_size_and_power_size_does_not_match(self):
        freq_points = [1, 2, 3]
        power_points = [1, 2, 3, 4]
        freq_range = {}

        self.assertRaises(ValueError, self.object_under_test.filter, freq_points, power_points, freq_range)

    def test_should_raise_error_given_end_frequency_greater_than_start_frequency(self):
        freq_points = [1, 2, 3, 4]
        power_points = [1, 2, 3, 4]
        freq_range = {
            'min': 15000,
            'max': 0
        }

        self.assertRaises(ValueError, self.object_under_test.filter, freq_points, power_points, freq_range)

    def test_should_filter_frequency_points_according_to_frequency_range(self):
        freq_points = [10, 200, 3000, 10000, 20000, 45000, 60000]
        power_points = [1, 2, 3, 4, 5, 6, 7]

        freq_range = {
            'min': 3000,
            'max': 45000
        }

        filtered_freq, filtered_power = self.object_under_test.filter(freq_points, power_points, freq_range)

        self.assertEqual([3000, 10000, 20000, 45000], filtered_freq)

    def test_filter_power_points_according_to_filtered_frequency_points(self):
        freq_points = [10, 200, 3000, 10000, 20000, 45000, 60000]
        power_points = [1, 2, 3, 4, 5, 6, 7]

        freq_range = {
            'min': 3000,
            'max': 45000
        }

        filtered_freq, filtered_power = self.object_under_test.filter(freq_points, power_points, freq_range)

        self.assertEqual([3, 4, 5, 6], filtered_power)

    def test_should_work_properly_given_min_freq_less_than_lowest_freq_in_collection(self):
        freq_points = [10000, 20000, 30000, 40000, 42000, 45000, 60000]
        power_points = [1, 2, 3, 4, 5, 6, 7]

        freq_range = {
            'min': 3000,
            'max': 45000
        }

        filtered_freq, filtered_power = self.object_under_test.filter(freq_points, power_points, freq_range)

        self.assertEqual([10000, 20000, 30000, 40000, 42000, 45000], filtered_freq)

    def test_should_work_properly_given_max_freq_greater_than_highest_freq_in_collection(self):
        freq_points = [10, 200, 3000, 10000, 20000, 42000, 43000]
        power_points = [1, 2, 3, 4, 5, 6, 7]

        freq_range = {
            'min': 3000,
            'max': 45000
        }

        filtered_freq, filtered_power = self.object_under_test.filter(freq_points, power_points, freq_range)

        self.assertEqual([3000, 10000, 20000, 42000, 43000], filtered_freq)

    def test_should_return_empty_lists_given_frequencies_out_of_range(self):
        freq_points = [10, 200, 3000, 10000, 20000, 42000, 43000]
        power_points = [1, 2, 3, 4, 5, 6, 7]

        freq_range = {
            'min': 60000,
            'max': 70000
        }

        filtered_freq, filtered_power = self.object_under_test.filter(freq_points, power_points, freq_range)

        self.assertEqual([], filtered_freq)
        self.assertEqual([], filtered_power)