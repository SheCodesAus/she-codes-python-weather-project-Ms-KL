import unittest
import weather


class FindMaxTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None

    def test_find_max_positive(self):
        temperatures = [49, 57, 56, 55, 53]
        expected_result = (57.0, 1)
        result = weather.find_max(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_max_negative(self):
        temperatures = [-10, -8, 2, -16, 4]
        expected_result = (4.0, 4)
        result = weather.find_max(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_max_floats(self):
        temperatures = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7]
        expected_result = (14.5, 1)
        result = weather.find_max(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_min_strings(self):
        temperatures = ["49", "57", "56", "55", "53", "49"]
        expected_result = (57.0, 1)
        result = weather.find_max(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_max_empty_list(self):
        temperatures = []
        expected_result = ()
        result = weather.find_max(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_max_repeated_value(self):
        temperatures = [49, 57, 56, 55, 57, 53, 49]
        expected_result = (57.0, 4)
        result = weather.find_max(temperatures)
        self.assertEqual(result, expected_result)
