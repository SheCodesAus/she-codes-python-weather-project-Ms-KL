import unittest
import weather


class ConvertDateTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None

    def test_convert_date(self):
        date = "2021-07-05T07:00:00+08:00"
        expected_result = "Monday 05 July 2021"
        result = weather.convert_date(date)
        self.assertEqual(result, expected_result)

        date = "2021-07-02T07:00:00+08:00"
        expected_result = "Friday 02 July 2021"
        result = weather.convert_date(date)
        self.assertEqual(result, expected_result)

        date = "2010-01-27T07:00:00+08:00"
        expected_result = "Wednesday 27 January 2010"
        result = weather.convert_date(date)
        self.assertEqual(result, expected_result)

        date = "2030-12-25T07:00:00+08:00"
        expected_result = "Wednesday 25 December 2030"
        result = weather.convert_date(date)
        self.assertEqual(result, expected_result)

    def test_convert_date_leap_year(self):
        date = "2024-02-29T07:00:00+08:00"
        expected_result = "Thursday 29 February 2024"
        result = weather.convert_date(date)
        self.assertEqual(result, expected_result)

    def test_convert_date_first_day_of_month(self):
        date = "2021-10-01T07:00:00+08:00"
        expected_result = "Friday 01 October 2021"
        result = weather.convert_date(date)
        self.assertEqual(result, expected_result)

    def test_convert_date_last_day_of_month(self):
        date = "2021-10-31T07:00:00+08:00"
        expected_result = "Sunday 31 October 2021"
        result = weather.convert_date(date)
        self.assertEqual(result, expected_result)
