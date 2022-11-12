# cd C:\GIT\python-assignment\she-codes-python-weather-project-Ms-KL
# python weather_playground_5_csv.py

import csv
#--5

csv_list = []

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


print(load_data_from_csv("tests\data\example_three.csv"))











 # csv_list.insert(0,header)

# def load_data_from_csv(csv_file):
#     """Reads a csv file and stores the data in a list.

#     Args:
#         csv_file: a string representing the file path to a csv file.
#     Returns:
#         A list of lists, where each sublist is a (non-empty) line in the csv file.
#     """
#     csv_list = []
#     with open(csv_file, encoding="utf-8") as csv_open:
#         reader = csv.reader (csv_open)
#         for line in reader:
#             if line != "":
#                 csv_list.append(line)
#             else:
#                 next
#     return (csv_list)
#     pass
# print(load_data_from_csv("tests\data\example_one.csv"))
# -------------------------------------------------


# csv_list = []
# with open("tests\data\example_two.csv", encoding="utf-8") as csv_open:
#     reader = csv.reader (csv_open, delimiter=',')
#     for line in reader:
#         if not (line):
#             continue
#         csv_list.append(line)

# print(csv_list)


# https://stackoverflow.com/a/41856836 (if not)