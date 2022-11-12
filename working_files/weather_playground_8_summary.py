import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# --------------------------------------------------------------------------------------------------
# TEST DATA
# --------------------------------------------------------------------------------------------------

# weather_data = ["5","-2","6","10","-2","10"]

weather_data = [
    ["2021-07-02T07:00:00+08:00", 49, 67],
    ["2021-07-03T07:00:00+08:00", 57, 68],
    ["2021-07-04T07:00:00+08:00", 56, 62],
    ["2021-07-05T07:00:00+08:00", 55, 61],
    ["2021-07-06T07:00:00+08:00", 53, 62]
]
weather_data = [
    ["2020-06-19T07:00:00+08:00", 47, 46],
    ["2020-06-20T07:00:00+08:00", 51, 67],
    ["2020-06-21T07:00:00+08:00", 58, 72],
    ["2020-06-22T07:00:00+08:00", 59, 71],
    ["2020-06-23T07:00:00+08:00", 52, 71],
    ["2020-06-24T07:00:00+08:00", 52, 67],
    ["2020-06-25T07:00:00+08:00", 48, 66],
    ["2020-06-26T07:00:00+08:00", 53, 66]
]
weather_data = [
    ["2020-06-19T07:00:00+08:00", -47, -46],
    ["2020-06-20T07:00:00+08:00", -51, 67],
    ["2020-06-21T07:00:00+08:00", 58, 72],
    ["2020-06-22T07:00:00+08:00", 59, 71],
    ["2020-06-23T07:00:00+08:00", -52, 71],
    ["2020-06-24T07:00:00+08:00", 52, 67],
    ["2020-06-25T07:00:00+08:00", -48, 66],
    ["2020-06-26T07:00:00+08:00", 53, 66]
]


# --------------------------------------------------------------------------------------------------
# DEFINED FUNCTIONS
# --------------------------------------------------------------------------------------------------

#--1 -------- DONE
def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

# ------------------------
# NOT COMPLETE
# ------------------------

#--2
def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass


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

#--4 ------ DONE
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

#--5 -------- DONE
def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    csv_list = []
    with open(csv_file, encoding="utf-8") as csv_open:
        reader = csv.reader (csv_open)
        header = next(reader)
        for line in reader:
            if not (line):
                continue
            csv_list.append([line[0],int(line[1]),int(line[2])])
    return (csv_list)
    pass

#--6 ---- DONE
def find_min(weather_data):
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
        min_temp = min(weather_data_list)
        for i in range(len(weather_data_list)):
            if weather_data_list[i] == min_temp:
                min_index = i
        return min_temp, min_index
    else:
        return ()

    pass

#--7 ---- DONE
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

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------


#--8
def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

                                    # --- REQUIRED:
                                    # count = 5
                                    # min_temp = f"9.4{DEGREE_SYBMOL}"
                                    # min_date = "Friday 02 July 2021"
                                    # max_temp = f"20.0{DEGREE_SYBMOL}"
                                    # max_date = "Saturday 03 July 2021"
                                    # mean_low = f"12.2{DEGREE_SYBMOL}"
                                    # mean_high = f"17.8{DEGREE_SYBMOL}"

    # --------- pull data in from find_min and find_max + use for find_date ------
    min_temp = (find_min(weather_data)[0])
    min_temp_row = (find_min(weather_data)[1])
    max_temp = (find_max(weather_data)[0])
    max_temp_row = (find_min(weather_data)[1])

    def find_date(min_temp_row, max_temp_row):
        '''
        use the index values to find the dates in the weather_data list
        '''
        mindate = 0
        maxdate = 0
        return (mindate, maxdate)
        pass

    # ----- pull data in from find_date and use for SUMMARY
    min_date, max_date = find_date(min_temp, max_temp)[0], find_date(min_temp, max_temp)[1]

    def find_mean(weather_data):
        '''
        create list of only minimum numbers
        create list of only maximum numbers
        use the mean function to find the mean of each list
        '''
        min_list = []
        max_list = []
        meanlow = 0
        meanhigh = 0
        use_mean = calculate_mean(weather_data)
        return (meanlow, meanhigh)
    
    # ----- pull data in from find_mean and use for SUMMARY
    mean_low = (find_mean(weather_data)[0])
    mean_high = (find_mean(weather_data)[1])



    return f"{count} Day Overview\n  The lowest temperature will be {min_temp}, and will occur on {min_date}.\n  The highest temperature will be {max_temp}, and will occur on {max_date}.\n  The average low this week is {mean_low}.\n  The average high this week is {mean_high}.\n"
    pass

print(generate_summary(5))


# --- what it should look like:

# 5 Day Overview
#   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#   The average low this week is 12.2°C.
#   The average high this week is 17.8°C.


# 8 Day Overview
#   The lowest temperature will be -46.7°C, and will occur on Tuesday 23 June 2020.
#   The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
#   The average low this week is -16.1°C.
#   The average high this week is 12.4°C.

# 8 Day Overview
#   The lowest temperature will be 8.3°C, and will occur on Friday 19 June 2020.
#   The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
#   The average low this week is 11.4°C.
#   The average high this week is 18.8°C.
