


import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# cd C:\GIT\python-assignment\she-codes-python-weather-project-Ms-KL
# python weather_playground_play.py

# weather_data = ["49", "57", "56", "55", "53", "49"]
weather_data = []


# STEP 1: format lists

def format_single_list (weather_data):
    """converts unformatted list input to formatted list

    Args:
        weather_data: A list of numbers.
    Returns:
        List of numbers as a float
    """
    if weather_data == []:
        return ()
    else:
        formatted_list = []
        for i in weather_data:
            formatted_list.append(float(i))
        return formatted_list



print(weather_data)
print(format_single_list (weather_data))

# STEP 2: avoid repetition and group min/max calc in one function

# def min_or_max (weather_data):
#     '''calculates min or max values from list input
#         formats the list using the format_single_list function

#     Args:
#         weather_data: a list of numbers
    
#     Returns:
#         list of numbers and their indexes
#         [min_temp, min_index, max_temp, max_index]
#     '''
#     if weather_data != []:
#         calc_list = format_single_list(weather_data)
#         min_temp = min(calc_list)
#         max_temp = max(calc_list)
#         for i in range(len(calc_list)):
#             if calc_list[i] == min_temp:
#                 min_index = i
#             if calc_list[i] == max_temp:
#                 max_index = i
#         return [min_temp, min_index, max_temp, max_index]
#     else:
#         return ()

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.
    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    if weather_data == []:
        return ()
    else:
        calc_list = format_single_list(weather_data)
        min_temp = min(calc_list)
        for i in range(len(calc_list)):
            if calc_list[i] == min_temp:
                min_index = i
        return min_temp, min_index

    # if weather_data != []:
    #     calc_list = min_max_list(weather_data)
    #     min_temp = min(calc_list)
    #     for i in range(len(calc_list)):
    #         if calc_list[i] == min_temp:
    #             min_index = i
    #     return min_temp, min_index
    # else:
    #     return ()

def find_max(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if weather_data == []:
        return ()
    else:
        calc_list = format_single_list(weather_data)
        max_temp = max(calc_list)
        for i in range(len(calc_list)):
            if calc_list[i] == max_temp:
                max_index = i
        return max_temp, max_index

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    if weather_data == []:
        return 0
    else:
        calc_list = format_single_list(weather_data)
        sum = 0
        for i in calc_list:
            sum = sum+i
        mean = sum / len(calc_list)
        return mean



print(find_min(weather_data))
print(find_max(weather_data))
print(calculate_mean(weather_data))