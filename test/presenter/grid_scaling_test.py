from unittest.case import TestCase

from presenter.grid_scaling import FrequencyPointsScaler, PowerPointsScaler


__author__ = 'novy'


class FrequencyPointsScalerTest(TestCase):
    def setUp(self):
        super(FrequencyPointsScalerTest, self).setUp()
        self.grid_width = 700
        self.left_top_x_grid_position = 20
        self.object_under_test = FrequencyPointsScaler(self.grid_width, self.left_top_x_grid_position)

    def test_scaling_frequency_points(self):
        frequency_points = [1, 2, 3, 4, 5, 6]

        expected_scaled_points = [
            20, 136, 253, 370, 486, 603
        ]

        self.assertEqual(self.object_under_test.scale(frequency_points), expected_scaled_points)


class PowerPointsScalerTest(TestCase):
    def setUp(self):
        super(PowerPointsScalerTest, self).setUp()
        self.grid_height = 500
        self.left_top_y = 20
        self.rows = 10
        self.power_per_row = 10
        self.db_level = 0
        self.object_under_test = PowerPointsScaler(self.grid_height, self.left_top_y, self.rows, self.power_per_row,
                                                   self.db_level)

    def test_points_with_zero_or_negative_value_should_be_on_bottom_of_the_screen(self):
        power_points = [0, -14.2, 0, -5]

        expected_scaled_points = [self.grid_height + self.left_top_y for _ in power_points]

        self.assertEqual(expected_scaled_points, self.object_under_test.scale(power_points))

    def test_points_with_huge_power_should_not_lay_outside_the_grid(self):
        power_points = [500, 1000]

        expected_scaled_points = [self.left_top_y for _ in power_points]

        self.assertEqual(expected_scaled_points, self.object_under_test.scale(power_points))

    def test_scaling_power_points(self):
        power_points = [10, 66, 20]

        expected_scaled_points = [470, 190, 420]

        self.assertEqual(expected_scaled_points, self.object_under_test.scale(power_points))
