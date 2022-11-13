


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





# -----------------
#--7
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

        list_of_numbers = [5,9,8,2,3,9]
        max_number = max(list_of_numbers)
        # this finds the maximum value in a list of numbers
        # this would be 9 (mentioned twice)

        for i in range(len(list_of_numbers)):
        # for each loop look at the value of i (first loop i= 0, last loop i = len(list_of_numbers))
        # use this i number to index against list_of_numbers

            if list_of_numbers[i] == max_number:
            # for each loop (above), use the i to index the list_of_numbers
            # eg: i = 1
            # eg: list_of_numbers[i] = list_of_numbers[1] = 9 (because 9 is @ index number 1)
                max_index = i
                # if the number you indexed (9) is == to the max number (9), then allocate it to variable max_index

        # the for loop will repeat until the list of numbers is complete
        # the if list_of_numbers[1] == max_number (condition statement) will repeat until the list of numbers is complete
            # as a result of the condition statement repeating, the max_index value gets overwritten from 1, with the new index number 5
            # this will give you the correct result for the end product 
            # eg: max_number = 9, mex_index = 5

        return max_number, max_index

        list_of_numbers = [5,9,8,2,3,9]

        # step 1: find maximum value in a list of numbers ------> max = 9 (mentioned twice)

        # step 2: loop the range of numbers in the list and consider the i value at each loop
            # eg: range = [5,9,8,2,3,9]
            # eg: i @ loop 1 = 0...... i @ loop 2 = 1 etc...

        # step 3: use i during each loop to index against the list
            # eg: loop 2 = list_of_numbers[i] = list_of_numbers[1] = 9

        # step 4: compare the max_value you found earlier and during every loop
            # eg: 

        # list_of_numbers[i] = list_of_numbers[1] = 9 (because 9 is @ index number 1)

list_of_numbers = [5,9,8,2,3,9]

# 1) find the max_value in a list

# 2) use a loop to find the index ( i ) of where each number in a list range ( len )

# 3) inside the loop compare ( == ) the max_value to the values found during each loop ( list[i] )

# 4) if the max_value == loop value ( eg: list[i] ), assign the index number ( i ) to max_index
    # NOTE: if this condition is true again, the max_index can be overwritten with the new index number on a different loop

# the loop will repeat until all numbers have been checked against max_value

# when the loop finds the max_value for a second time, it will replace the value previously set against max_index
    # eg: during loop 2 we found that max_value == list[1] --- > 9 == 9
    # eg: max_index = list[1] == 1
    # eg: during loop 6 we found that max_value == list[5] --- > 9 == 9
    # eg: max_index = list[5] == 5 
    # eg: the condition = TRUE which means the max_index was overwritten from 1 to new number 5

