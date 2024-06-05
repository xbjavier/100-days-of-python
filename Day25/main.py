import pandas

data = pandas.read_csv("Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


squirrel_gray = data[data["Primary Fur Color"] == "Gray"]
squirrel_red = data[data["Primary Fur Color"] == "Cinnamon"]
squirrel_black = data[data["Primary Fur Color"] == "Black"]

summary = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(squirrel_gray), len(squirrel_red), len(squirrel_black)]
}

data_frame = pandas.DataFrame(summary)
csv = data_frame.to_csv("Day25/squirrels_summary.csv", index=False)
print(data_frame)
