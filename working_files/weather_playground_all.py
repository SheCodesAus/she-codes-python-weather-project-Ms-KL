
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
# weather_data = [
#     ["2020-06-19T07:00:00+08:00", 47, 46],
#     ["2020-06-20T07:00:00+08:00", 51, 67],
#     ["2020-06-21T07:00:00+08:00", 58, 72],
#     ["2020-06-22T07:00:00+08:00", 59, 71],
#     ["2020-06-23T07:00:00+08:00", 52, 71],
#     ["2020-06-24T07:00:00+08:00", 52, 67],
#     ["2020-06-25T07:00:00+08:00", 48, 66],
#     ["2020-06-26T07:00:00+08:00", 53, 66]
# ]
# weather_data = [
#     ["2020-06-19T07:00:00+08:00", -47, -46],
#     ["2020-06-20T07:00:00+08:00", -51, 67],
#     ["2020-06-21T07:00:00+08:00", 58, 72],
#     ["2020-06-22T07:00:00+08:00", 59, 71],
#     ["2020-06-23T07:00:00+08:00", -52, 71],
#     ["2020-06-24T07:00:00+08:00", 52, 67],
#     ["2020-06-25T07:00:00+08:00", -48, 66],
#     ["2020-06-26T07:00:00+08:00", 53, 66]
# ]

# --------------------------------------------------------------------------------------------------
# FUNCTIONS
# --------------------------------------------------------------------------------------------------






def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

#--2
def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_time = datetime.fromisoformat(iso_string)
    convert_date = date_time.strftime("%A %d %B %Y")
    return convert_date
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
    return round(mean, 1)
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
    return csv_list
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

#--7
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

# #--8
# def generate_summary(weather_data):
#     """Outputs a summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """
#     # STEP 1:
#     # variables to get: min_temp + max_temp
#     # use def functions: find_min & find_max
#     # use data: weather data
#     # note: result of find_min/max function is (F,int), so we need [0] for F
#     # convert these f values to c using function

#     min_temp = convert_f_to_c((find_min(weather_data)[0]))
#     max_temp = convert_f_to_c((find_max(weather_data)[0]))

#     # STEP 2:
#     # variables to get: min_date and max_dates
#     # use def functions: find_min & find_max
#     # use data: weather data
#     # note: result of find_min/max function is (F,int), so we need [1] for the index.
#     # the index = the row of data
#     # use the row number to cross reference and index for the date in the weather data
#     # convert the date to the proper format

#     min_temp_row = (find_min(weather_data)[1])
#     max_temp_row = (find_min(weather_data)[1])

#     for weather_date in weather_data[min_temp_row]:
#         # min_date = convert_date(weather_data[0])
#         min_date = weather_data[0]

#     for weather_date in weather_data[max_temp_row]:
#         # max_date = convert_date(weather_data[0])
#         max_date = weather_data[0]


#     # STEP 3:
#     # get average minimum and average maximum values using calculate_mean function
#     # create a list first for minimums and maximums using for loop to pass into the mean function

#     minimums = []
#     maximums = []

#     for i in weather_data:
#         minimums.append(float(i[1]))
#         maximums.append(float(i[2]))

#     mean_low = calculate_mean(minimums)
#     mean_high = calculate_mean(maximums)

#     # STEP 4:
#     # establish how many days for summary

#     count = len(weather_data)

#     return f"{count} Day Overview\n  The lowest temperature will be {min_temp}, and will occur on {min_date}.\n  The highest temperature will be {max_temp}, and will occur on {max_date}.\n  The average low this week is {mean_low}.\n  The average high this week is {mean_high}.\n"
#     # return f"count = {count}, min temp =  {min_temp}, max_temp = {max_temp}, min_temp_row = {min_temp_row}, max_temp_row = {max_temp_row}"
#     pass

#--9
# def generate_daily_summary(weather_data):
#     """Outputs a daily summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """
#     pass

# print(generate_summary(weather_data))



# --------------------------------------------------------------------------------------------------
# REQUIREMENTS for SUMMARIES
# --------------------------------------------------------------------------------------------------

# count = 5
# min_temp =    f"9.4{DEGREE_SYBMOL}"
# min_date =    "Friday 02 July 2021"
# max_temp =    f"20.0{DEGREE_SYBMOL}"
# max_date =    "Saturday 03 July 2021"
# mean_low =    f"12.2{DEGREE_SYBMOL}"
# mean_high =   f"17.8{DEGREE_SYBMOL}"



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












# STEP 1:
# variables to get: min_temp + max_temp
# use def functions: find_min & find_max
# use data: weather data
# note: result of find_min/max function is (F,int), so we need [0] for F
# convert these f values to c using function

# min_temp = convert_f_to_c((find_min(weather_data)[0]))
# max_temp = convert_f_to_c((find_max(weather_data)[0]))

# # STEP 2:
# # variables to get: min_date and max_dates
# # use def functions: find_min & find_max
# # use data: weather data
# # note: result of find_min/max function is (F,int), so we need [1] for the index.
# # the index = the row of data
# # use the row number to cross reference and index for the date in the weather data
# # convert the date to the proper format

# min_temp_row = (find_min(weather_data)[1])
# max_temp_row = (find_min(weather_data)[1])

# for weather_date in weather_data[min_temp_row]:
#     min_date = convert_date(weather_data[0])

# for weather_date in weather_data[max_temp_row]:
#     max_date = convert_date(weather_data[0])


# # STEP 3:
# # get average minimum and average maximum values using calculate_mean function
# # create a list first for minimums and maximums using for loop to pass into the mean function

# minimums = []
# maximums = []

# for i in weather_data:
#     minimums.append(i[1])
#     maximums.append(i[2])

# mean_low = calculate_mean(minimums)
# mean_high = calculate_mean(maximums)

# # STEP 4:
# # establish how many days for summary

# count = len(weather_data)


#------------------ 5:45pm

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # ----- GOALS ------
    # TEMPS: min_temp + max_temp
    # DATES: min_date + max_date
    # MEANS: mean_low + mean_high 
    # COUNT

    # STEP 1 GET DATA:
    # convert weather data into 3x lists to use for functions
    
    dates_list = []
    min_list = []
    max_list = []
    for row in weather_data:
        dates_list.append(convert_date(row[0]))
        min_list.append(convert_f_to_c(row[1]))
        max_list.append(convert_f_to_c(row[2]))


    # STEP 2 GET TEMPS:
    # find min_temp and max_temp in lists using functions

    min_temp_n_index = find_min(min_list)
    min_temp = min_temp_n_index[0]
    max_temp_n_index = find_max(max_list)
    max_temp = max_temp_n_index[0]

    # STEP 3 GET DATES:
    # find min_date and max_date using temp_n_index[1] (index position of min or max) @ return item @ index 0
    # need to convert these dates using function

    min_date = dates_list[min_temp_n_index[1]]
    max_date = dates_list[max_temp_n_index[1]]

    # STEP 4 GET MEANS:
    # find mean_low and mean_high using functions

    mean_low = calculate_mean(min_list)
    mean_high = calculate_mean(max_list)


    # STEP 5 GET COUNT:
    # find count using length of weather data
    count = len(weather_data)

    return f"{count} Day Overview\n  The lowest temperature will be {min_temp}{DEGREE_SYBMOL}, and will occur on {min_date}.\n  The highest temperature will be {max_temp}{DEGREE_SYBMOL}, and will occur on {max_date}.\n  The average low this week is {mean_low}{DEGREE_SYBMOL}.\n  The average high this week is {mean_high}{DEGREE_SYBMOL}.\n"


#--9
def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

# --- working it out

# GOALS:
# day_date
# day_min_temp
# day_max_temp

    # STEP 1 GET DATA:
    # convert weather data a list to allocate to required variables
    
    weather_list = []
    for row in weather_data:
        weather_list.append([
            convert_date(row[0]),
            convert_f_to_c(row[1]),
            convert_f_to_c(row[2])
            ])
    
    # STEP 2 ALLOCATE VARIABLES:
    # index the weather_list and allocate to date_time, min and max

    daily_summary_string = ""
    last_string = ""
    for row in weather_list:
        day_date = row[0]
        day_min_temp = row[1]
        day_max_temp = row[2]
        daily_summary_string = last_string + f"---- {day_date} ---\n  Minimum Temperature: {day_min_temp}{DEGREE_SYBMOL}\n  Maximum Temperature: {day_max_temp}{DEGREE_SYBMOL}\n\n"
        last_string = daily_summary_string
    return daily_summary_string

   

       
        # for i in range(len(weather_list)):
        #     day[i] = 



    # STEP 2 GET TEMPS:
    # find min_temp and max_temp in lists using functions

    # min_temp_n_index = find_min(min_list)
    # min_temp = min_temp_n_index[0]
    # max_temp_n_index = find_max(max_list)
    # max_temp = max_temp_n_index[0]

    # return weather_list

    # return f"---- {day_date} ---\n  Minimum Temperature: {day_min_temp}{DEGREE_SYBMOL}\n  Maximum Temperature: {day_max_Temp}\n\n"


# print(generate_summary(weather_data))
print(generate_daily_summary(weather_data))















































    # # STEP 1:
    # # variables to get: min_temp + max_temp
    # # use def functions: find_min & find_max
    # # use data: weather data
    # # note: result of find_min/max function is (F,int), so we need [0] for F
    # # convert these f values to c using function

    # # min_temp = convert_f_to_c((find_min(weather_data)[0]))
    # # max_temp = convert_f_to_c((find_max(weather_data)[0]))
    # min_temp = find_min(weather_data)
    # min_temp = min_temp[0]
    # max_temp = find_max(weather_data)
    # max_temp = max_temp[0]

    # # STEP 2:
    # # variables to get: min_date and max_dates
    # # use def functions: find_min & find_max
    # # use data: weather data
    # # note: result of find_min/max function is (F,int), so we need [1] for the index.
    # # the index = the row of data
    # # use the row number to cross reference and index for the date in the weather data
    # # convert the date to the proper format

    # min_temp_row = (find_min(weather_data)[1])
    # max_temp_row = (find_min(weather_data)[1])

    # for weather_date in weather_data[min_temp_row]:
    #     # min_date = convert_date(weather_data[0])
    #     min_date = weather_data[0]

    # for weather_date in weather_data[max_temp_row]:
    #     # max_date = convert_date(weather_data[0])
    #     max_date = weather_data[0]


    # # STEP 3:
    # # get average minimum and average maximum values using calculate_mean function
    # # create a list first for minimums and maximums using for loop to pass into the mean function


    # mean_low = calculate_mean(min_list)
    # mean_high = calculate_mean(max_list)

    # # STEP 4:
    # # establish how many days for summary

    # count = len(weather_data)

    # return f"{count} Day Overview\n  The lowest temperature will be {min_temp}, and will occur on {min_date}.\n  The highest temperature will be {max_temp}, and will occur on {max_date}.\n  The average low this week is {mean_low}.\n  The average high this week is {mean_high}.\n"
    # # return f"count = {count}, min temp =  {min_temp}, max_temp = {max_temp}, min_temp_row = {min_temp_row}, max_temp_row = {max_temp_row}"
    # pass