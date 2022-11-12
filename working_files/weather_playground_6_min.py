# cd C:\GIT\python-assignment\she-codes-python-weather-project-Ms-KL
# python weather_playground_6_min.py


# import csv

# def find_min(weather_data):
#     """Calculates the minimum value in a list of numbers.

#     Args:
#         weather_data: A list of numbers.
#     Returns:
#         The minium value and it's position in the list.
#     """
    # for i in range(len(weather_data)):
    #     min_weather = min(weather_data)
    #     min_index = 0
    #     if i == min_weather:
    #         min_index = weather_data[i]
    #     else:
    #         continue
    # return min_weather, min_index
    # pass


    # ---- USE THIS
    # min_index = 0
    # for i in range(len(weather_data)):
    #     min_weather = min(weather_data)
    #     if min_weather == True:
    #         min_index = i
    # return min_weather, min_index
    # pass

# print(find_min([5,6,10,-2,4]))

# for i in range(len(enter_word)):
#     print(i, enter_word[i])



# ------------------------

# import csv

# galaxy_min = 0
# galaxy_max = 0
# galaxies = []

# with open("galaxies.csv ", encoding="utf-8") as csv_file:
# #utf-8 translates unicode characters and turn into binary so computer can understand
#     next(csv_file)
#     reader = csv.reader (csv_file)
#     for line in reader:
#         line_int = [int(line[0]),int(line[1])]
#         galaxies.append((line_int))
#     galaxy_min = (min(galaxies))
#     galaxy_max = (max(galaxies))

# print(f"Galaxy {galaxy_min[0]} has the min velocity of {galaxy_min[1]}km/sec.\nGalaxy {galaxy_max[0]} has the max velocity of {galaxy_max[1]}km/sec. ")

# ------------------

# print one word and index at a time

# for i in range(len(enter_word)):
#     print(i, enter_word[i])
#     # prints index (due to range) and the word index based on iteration






# --------------------------

# import csv

# min_index = 0
# weather_data = ["5","6","10","-2","4"]

# # min_weather = min(weather_data)
# # min_index = weather_data.index(min_weather)


# for i in range(len(weather_data)):
#     weather_data_list = []
#     weather_data_list.append(int(i))

# min_weather = min(weather_data_list)
# min_index = weather_data_list.index(min_weather)

# print ((min_weather, min_index))


# def find_min(weather_data):
#     """Calculates the minimum value in a list of numbers.

#     Args:
#         weather_data: A list of numbers.
#     Returns:
#         The minium value and it's position in the list.
#     """
#     min_weather = min(weather_data)
#     min_index = weather_data.index(min_weather)
#     return min_weather, min_index
#     pass

# -------------------------------------------------------

import csv

# this works but need to convert data from string to float

# min_index = 0
# # weather_data = ["5","6","10","-2","4"]
# weather_data = [5,6,10,-2,4]
# min_weather = min(weather_data)
# min_index = weather_data.index(min_weather)
# print(min_weather, min_index)


# turn string to float

# min_index = 0
# weather_data = ["5","6","10","-2","4"]
# # weather_data = [5,6,10,-2,4]

# weather_data_list = []
# for i in weather_data:
#     weather_data_list.append(float(i))
# min_weather = min(weather_data_list)
# min_index = weather_data_list.index(min_weather)
# print(min_weather, min_index)


# ------------------

# weather_data = ["5","6","10","-2","4"]

# def find_min(weather_data):
#     """Calculates the minimum value in a list of numbers.

#     Args:
#         weather_data: A list of numbers.
#     Returns:
#         The minium value and it's position in the list.
#     """
#     if weather_data != []:
#         min_index = 0
#         weather_data_list = []
#         for i in weather_data:
#             weather_data_list.append(float(i))
#         min_weather = min(weather_data_list)
#         min_index = weather_data_list.index(min_weather)
#         # 2 min values. How do I select then second
#         return (min_weather, min_index)
#     else:
#         return ()

#     pass

# # print(find_min(["5","6","10","-2","4"]))
# print(find_min([]))


# ------------------------- duplicate min value
import csv

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

print(find_min(["5","-2","6","10","-2","4"]))
# print(find_min([]))

# https://stackoverflow.com/questions/44743756/find-last-index-of-element-in-list-with-duplicate-elements-python

# def find_index (mylist):
#     for i in range(len(mylist)):
#         if mylist[i] == min(mylist):
#             index = i
#     return min(mylist),index

# print(find_index([1,12,-3,4,4,5,12,15,-3,11]))


# -----
# https://www.trainingint.com/how-to-find-duplicates-in-a-python-list.html
