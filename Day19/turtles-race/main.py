from turtle import Turtle, Screen, textinput
from random import randint, randrange

colors = ["red", "green", "yellow", "purple", "black", "gray", "orange"]

number_of_turtles = 1

turtles = []

screen = Screen()
screen.setup(500, len(colors) * 10 + 500)
screen.colormode(255)


x = -((screen.window_width() / 2.0) - 10)
y = -(screen.window_height() / 2.0)
y_space_between = screen.window_width() / float(len(colors))

y_distance = y + y_space_between

for i in range(len(colors)):
    t = Turtle()
    t.shape("turtle")
    t.penup()
    t.color(colors[i])
    t.teleport(x, y_distance)
    turtles.append(t)
    y_distance += y_space_between

selection = textinput(
    "What turtle will win?", f"select one color:\n{', '.join(colors)}"
)

winner = None
final_position = screen.window_width() / 2.0

while winner == None:
    for timmy in turtles:
        rand_step = randint(1, 10)
        timmy.fd(rand_step)
        if timmy.xcor() >= final_position:
            winner = timmy
            break


if selection == winner.color():
    print("You won!")
else:
    print(f"You lost :( , winner is: {winner.color()[0]}")


screen.mainloop()
