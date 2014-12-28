from view.canvas_panel import GRID_WIDTH, GRID_HEIGHT, LEFT_TOP_GRID_X_POSITION, ROWS, COLUMNS

__author__ = 'novy'


class GridScaler(object):
    def __init__(self, power_per_row, grid_width=GRID_WIDTH, grid_height=GRID_HEIGHT,
                 left_top_x=LEFT_TOP_GRID_X_POSITION, left_top_y=LEFT_TOP_GRID_X_POSITION,
                 rows=ROWS, columns=COLUMNS, ):
        super(GridScaler, self).__init__()

        self.frequency_scaler = FrequencyPointsScaler(grid_width, left_top_x)
        self.power_scaler = PowerPointsScaler(grid_height, left_top_y, rows, power_per_row)

    def scale_frequency(self, frequency_points):
        return self.frequency_scaler.scale(frequency_points)

    def scale_power(self, power_points):
        return self.power_scaler.scale(power_points)


class FrequencyPointsScaler(object):
    def __init__(self, grid_width, left_top_x_position):
        super(FrequencyPointsScaler, self).__init__()
        self.grid_width = grid_width
        self.left_top_x_position = left_top_x_position

    def scale(self, frequency_points):
        pixels_per_frequency_gap = float(self.grid_width) / len(frequency_points)

        return [
            int(i * pixels_per_frequency_gap + self.left_top_x_position)
            for i in xrange(len(frequency_points))
        ]


class PowerPointsScaler(object):
    def __init__(self, grid_height, left_top_y, rows, power_per_row):
        super(PowerPointsScaler, self).__init__()
        self.grid_height = grid_height
        self.left_top_y = left_top_y
        self.rows = rows
        self.power_per_row = power_per_row

    def scale(self, power_points):
        with_negative_power_replaced = [
            power if power >= 0 else 0 for power in power_points
        ]

        pixels_per_decibel = float(self.grid_height) / (self.rows * self.power_per_row)

        scaled = [
            int(self.grid_height - power * pixels_per_decibel)
            for power in with_negative_power_replaced
        ]

        return [
            self.left_top_y if power < self.left_top_y else power
            for power in scaled
        ]
