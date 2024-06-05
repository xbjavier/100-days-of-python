from typing import List

def get_number_list_from_file(file: str)-> List[int]:
    with open(file, mode="r") as data:
        temp = data.readlines()
        return [(int)(line.replace('\n','')) for line in temp]

list1 = get_number_list_from_file("Day26/file1.txt")
list2 = get_number_list_from_file("Day26/file2.txt")

result = [num for num in list1 if num in list2]

print(result)

def centigrade_to_fahrenheit(degrees: float)->float:
    return degrees * 9/5 +32

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 19,
    "Sunday": 20
}

fahrenheit_dic = {day:centigrade_to_fahrenheit(weather) for (day,weather) in weather_c.items()}
print(fahrenheit_dic)

import pandas

data = pandas.read_csv("Day26/nato_phonetic_alphabet.csv", index_col=None)
data_dic = {row.letter:row.code for (index, row) in data.iterrows()}
print(data_dic)