from random import random, randint
from turtle import Turtle


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def process(turtle: Turtle, radius: float, gapSize: float):
    turtle.speed(0)
    for _ in range(int(360 / gapSize)):
        color = random_color()
        turtle.pencolor(color[0], color[1], color[2])
        turtle.setheading(turtle.heading() + gapSize)
        turtle.circle(radius, extent=None, steps=None)
