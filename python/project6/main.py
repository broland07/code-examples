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
print(data["temp"])