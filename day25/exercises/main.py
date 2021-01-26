#!/usr/bin/env pythong

# with open("weather_data.csv") as f:
#     data = f.readlines()

# import csv

# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)


# # temperatures = data["temp"].to_list()
# # print(temperatures)
# # print(sum(temperatures) / len(temperatures))
# print(data["temp"].mean())

# print(data["temp"].max())
# print(data.temp.max())

# get Row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp * 9 / 5 + 32)
# print(int(monday.temp) * 9 / 5 + 32)


data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

data = pandas.DataFrame(data_dict)
# print(data)

data.to_csv("new_data.csv")
