from unittest import TestCase

from integer_statistics import IntegerStatistics


class TestIntegerStatistics(TestCase):
    def setUp(self):
        self.int_stat = IntegerStatistics([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])

    def test_calculate_mean(self):
        expected_mean_result = 9.0
        actual_mean_result = self.int_stat.mean()

        self.assertEqual(expected_mean_result, actual_mean_result)

    def test_calculate_standard_deviation(self):
        expected_stdev_result = 3.317
        actual_stdev_result = self.int_stat.stdev()

        self.assertEqual(expected_stdev_result, actual_stdev_result)
