position = "B3"

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
# Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letters = ['a','b', 'c']
row = int(position[1])- 1
column = int(letters.index(position[0].lower()))

map[row][column] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")