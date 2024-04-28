from random import random, randint
from turtle import Turtle, Screen


def challenge_2_dashed_line(screen: Screen, max_passes=100):
    t = Turtle()
    initial_point = -(screen.window_width() / 2)
    t.penup()
    t.teleport(initial_point, 0)
    t.pendown()
    for i in range(max_passes):
        if i % 2 == 0:
            t.pendown()
        else:
            t.penup()
        t.forward(10)

        if i * 10 > screen.window_width():
            break
