# cd C:\GIT\python-assignment\she-codes-python-weather-project-Ms-KL
# python weather_playground_7_max.py


import csv

def find_max(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if weather_data != []:
        weather_data_list = []
        for i in weather_data:
            weather_data_list.append(float(i))
        max_temp = max(weather_data_list)
        for i in range(len(weather_data_list)):
            if weather_data_list[i] == max_temp:
                max_index = i
        return max_temp, max_index
    else:
        return ()
    pass


print(find_max(["5","-2","6","10","-2","10"]))
# print(find_min([]))