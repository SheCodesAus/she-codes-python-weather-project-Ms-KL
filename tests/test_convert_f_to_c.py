import unittest
import weather


class ConvertTempTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None

    def test_convert_f_to_c(self):
        temp_in_f = 90
        expected_result = 32.2
        result = weather.convert_f_to_c(temp_in_f)
        self.assertEqual(result, expected_result)

    def test_convert_f_to_c_negative(self):
        temp_in_f = -10
        expected_result = -23.3
        result = weather.convert_f_to_c(temp_in_f)
        self.assertEqual(result, expected_result)

    def test_convert_f_to_c_float(self):
        temp_in_f = 64.4
        expected_result = 18
        result = weather.convert_f_to_c(temp_in_f)
        self.assertEqual(result, expected_result)

    def test_convert_f_to_c_string(self):
        temp_in_f = "77"
        expected_result = 25.0
        result = weather.convert_f_to_c(temp_in_f)
        self.assertEqual(result, expected_result)
