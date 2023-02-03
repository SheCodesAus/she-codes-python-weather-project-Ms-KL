
weather_data = [
    ["2021-07-02T07:00:00+08:00", 49, 67],
    ["2021-07-03T07:00:00+08:00", 57, 68],
    ["2021-07-04T07:00:00+08:00", 56, 62],
    ["2021-07-05T07:00:00+08:00", 55, 61],
    ["2021-07-06T07:00:00+08:00", 53, 62]
]

# --------------------------


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


min_list = []
for min in weather_data:
    min_list.append(min[1])

max_list = []
for max in weather_data:
    max_list.append(max[2])

mean_low = calculate_mean(min_list)
mean_high = calculate_mean(max_list)

print(min_list)
print (mean_low)
print(max_list)
print(mean_high)







# min_list = [min[1] for min in weather_data]
# # output [49,57,56,55,53]

# min_list = []
# for min in weather_data:
#     min_list.append(min[1])
# # output [49,57,56,55,53]

# print(min_list)

# min_list = [min[2] for min in weather_data]
# # # output [67,68,62,61,62]

# min_list = [min for min in weather_data]
# # # output same as weather_data