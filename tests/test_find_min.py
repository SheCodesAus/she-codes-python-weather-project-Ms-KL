import unittest
import weather


class FindMinTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None

    def test_find_min_positive(self):
        temperatures = [49, 57, 56, 55, 53]
        expected_result = (49.0, 0)
        result = weather.find_min(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_min_negative(self):
        temperatures = [-10, -8, 2, -16, 4]
        expected_result = (-16.0, 3)
        result = weather.find_min(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_min_floats(self):
        temperatures = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7]
        expected_result = (8.9, 3)
        result = weather.find_min(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_min_strings(self):
        temperatures = ["49", "57", "56", "55", "53", "49"]
        expected_result = (49.0, 5)
        result = weather.find_min(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_min_empty_list(self):
        temperatures = []
        expected_result = ()
        result = weather.find_min(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_min_repeated_value(self):
        temperatures = [49, 57, 56, 55, 53, 49]
        expected_result = (49.0, 5)
        result = weather.find_min(temperatures)
        self.assertEqual(result, expected_result)

