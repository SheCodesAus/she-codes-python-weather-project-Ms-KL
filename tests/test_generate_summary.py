import unittest
import weather


class GenerateSummaryTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None
        self.example_one = [
            ["2021-07-02T07:00:00+08:00", 49, 67],
            ["2021-07-03T07:00:00+08:00", 57, 68],
            ["2021-07-04T07:00:00+08:00", 56, 62],
            ["2021-07-05T07:00:00+08:00", 55, 61],
            ["2021-07-06T07:00:00+08:00", 53, 62]
        ]
        self.example_two = [
            ["2020-06-19T07:00:00+08:00", 47, 46],
            ["2020-06-20T07:00:00+08:00", 51, 67],
            ["2020-06-21T07:00:00+08:00", 58, 72],
            ["2020-06-22T07:00:00+08:00", 59, 71],
            ["2020-06-23T07:00:00+08:00", 52, 71],
            ["2020-06-24T07:00:00+08:00", 52, 67],
            ["2020-06-25T07:00:00+08:00", 48, 66],
            ["2020-06-26T07:00:00+08:00", 53, 66]
        ]
        self.example_three = [
            ["2020-06-19T07:00:00+08:00", -47, -46],
            ["2020-06-20T07:00:00+08:00", -51, 67],
            ["2020-06-21T07:00:00+08:00", 58, 72],
            ["2020-06-22T07:00:00+08:00", 59, 71],
            ["2020-06-23T07:00:00+08:00", -52, 71],
            ["2020-06-24T07:00:00+08:00", 52, 67],
            ["2020-06-25T07:00:00+08:00", -48, 66],
            ["2020-06-26T07:00:00+08:00", 53, 66]
        ]

    def test_generate_summary_example_one(self):
        with open("tests/expected_output/example_one_summary.txt", encoding="utf8") as txt_file:
            expected_result = txt_file.read()
        result = weather.generate_summary(self.example_one)
        self.assertEqual(expected_result, result)

    def test_generate_summary_example_two(self):
        with open("tests/expected_output/example_two_summary.txt", encoding="utf8") as txt_file:
            expected_result = txt_file.read()
        result = weather.generate_summary(self.example_two)
        self.assertEqual(expected_result, result)

    def test_generate_summary_example_three(self):
        with open("tests/expected_output/example_three_summary.txt", encoding="utf8") as txt_file:
            expected_result = txt_file.read()
        result = weather.generate_summary(self.example_three)
        self.assertEqual(expected_result, result)
