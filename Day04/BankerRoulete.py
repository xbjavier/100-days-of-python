import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(', ')

rand = names[random.randint(0, len(names))]
print(f"{rand} is going to buy the meal today!")