# with open("weather_data.csv") as wdata:
#     lines = wdata.readlines()

# print(lines)

# import csv

# with open("weather_data.csv") as wdata:
#     data = csv.reader(wdata)
#     next(data)
#     temperatures = []
#     for row in data:
# #        int_row = int(row[1])
#         temperatures.append(int(row[1]))

# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

temp_list =  data["temp"].to_list()
# average = sum(temp_list)/len(temp_list)
# print(round(average))

print(data["temp"].mean())