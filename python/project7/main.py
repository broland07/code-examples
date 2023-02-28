import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

first = len(data[data["Primary Fur Color"] == "Gray"])
second = len(data[data["Primary Fur Color"] == "Cinnamon"])
third = len(data[data["Primary Fur Color"] == "Black"])
print(first)
print(second)
print(third)

data_dict = {
    "Color": ["Gray," "Cinnamon", "Black"],
    "Count": [first, second, third]
}

print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("count.csv")