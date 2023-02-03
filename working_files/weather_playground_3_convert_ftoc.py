# cd C:\GIT\python-assignment\she-codes-python-weather-project-Ms-KL
# python weather_playground_3_convert_ftoc.py


import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

#--3 ------ DONE
def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_c = (float(temp_in_farenheit) - 32) * .5556
    return round(temp_in_c,1) 
    pass







# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------


# # def convert_f_to_c(temp_in_farenheit):
# #     """Converts an temperature from farenheit to celcius.

# #     Args:
# #         temp_in_farenheit: float representing a temperature.
# #     Returns:
# #         A float representing a temperature in degrees celcius, rounded to 1dp.
# #     """
# #     temp_in_c = (float(temp_in_farenheit) - 32) * .5556
# #     return round(temp_in_c,1) 

# #     pass

# # print(convert_f_to_c(90))

# temp_in_farenheit = 90

# temp_in_c = (float(temp_in_farenheit) - 32) * .5556
# print (round(temp_in_c,1)) 