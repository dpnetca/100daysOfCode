#!/usr/bin/env python

import pandas

# squirrel_df = pandas.read_csv(
#     "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
# )

# # Close, but not formatted right.. could maybe start here and manipulate
# unique_color_count = squirrel_df["Primary Fur Color"].value_counts()
# unique_color_count.to_csv("squirrel_count.csv")

# # this works:
# colors = squirrel_df["Primary Fur Color"].dropna().unique()

# color_dict = {"Fur Color": [], "Count": []}
# for color in colors:
#     if color != "nan":
#         color_dict["Fur Color"].append(color)
#         shape = squirrel_df[squirrel_df["Primary Fur Color"] == color].shape
#         color_dict["Count"].append(shape[0])

# squirrel_count = pandas.DataFrame(color_dict)
# squirrel_count.to_csv("squirrel_count.csv")


# Instructor solution:
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = data[data["Primary Fur Color"] == "Gray"]
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
black = data[data["Primary Fur Color"] == "Black"]
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray), len(cinnamon), len(black)],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
