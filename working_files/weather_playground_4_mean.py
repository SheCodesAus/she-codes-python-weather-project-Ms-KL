# cd C:\GIT\python-assignment\she-codes-python-weather-project-Ms-KL
# python weather_playground_4_mean.py


import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum = 0
    for i in weather_data:
        sum = float(sum)+float(i)
    mean = sum / len(weather_data)

    return mean
    pass

weather_data = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
print(calculate_mean(weather_data))