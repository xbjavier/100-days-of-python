from random import random, randint
from turtle import Turtle, Screen


def challenge_2_dashed_line(turtle: Turtle, screen: Screen, max_passes=100):
    initial_point = -(screen.window_width() / 2)
    turtle.penup()
    turtle.teleport(initial_point, 0)
    turtle.st()
    turtle.pendown()
    for i in range(max_passes):
        if i % 2 == 0:
            turtle.pendown()
        else:
            turtle.penup()
        turtle.forward(10)

        if i * 10 > screen.window_width():
            break
