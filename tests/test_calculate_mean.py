import unittest
import weather


class CalculateMeanTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None

    def test_calculate_mean(self):
        temperatures = [49, 57, 56, 55, 53]
        expected_result = 54
        result = weather.calculate_mean(temperatures)
        self.assertEqual(result, expected_result)

    def test_calculate_mean_floats(self):
        temperatures = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
        expected_result = 52.90375
        result = weather.calculate_mean(temperatures)
        self.assertEqual(result, expected_result)

    def test_calculate_mean_strings(self):
        temperatures = ["51", "58", "59", "52", "52", "48", "47", "53"]
        expected_result = 52.5
        result = weather.calculate_mean(temperatures)
        self.assertEqual(result, expected_result)
    
    def test_calculate_mean_negative(self):
        temperatures = [-51, -58, -59, -52, -52, -48, -47, -53]
        expected_result = -52.5
        result = weather.calculate_mean(temperatures)
        self.assertEqual(result, expected_result)
