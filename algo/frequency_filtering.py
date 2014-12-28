__author__ = 'novy'


def first_matching_index(collection, matching_function):
    try:
        return next(item[0] for item in enumerate(collection) if matching_function(item[1]))
    except StopIteration:
        return len(collection)


class FrequencyFilterer(object):
    def filter(self, frequency_points, power_points, frequency_range):
        self._assert_equal_sizes(frequency_points, power_points)

        min_freq, max_freq = frequency_range['min'], frequency_range['max']
        self._assert_proper_range(min_freq, max_freq)

        first_less_or_equal_index = first_matching_index(
            frequency_points, lambda frequency: frequency >= frequency_range['min'])

        first_greater_index = first_matching_index(
            frequency_points, lambda frequency: frequency > frequency_range['max']
        )

        return (frequency_points[first_less_or_equal_index:first_greater_index],
                power_points[first_less_or_equal_index:first_greater_index])

    def _assert_equal_sizes(self, frequency_points, power_points):
        if len(frequency_points) != len(power_points):
            raise ValueError("Frequency points and power points sizes differ")

    def _assert_proper_range(self, min_freq, max_freq):
        if max_freq < min_freq:
            raise ValueError("Max frequency cannot be lower than min frequency")
