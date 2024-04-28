from random import random, randint
from turtle import Turtle

turtle: Turtle = None

directions = [
    {"label": "north", "angle": 90.0},
    {"label": "south", "angle": 270.0},
    {"label": "east", "angle": 180.0},
    {"label": "west", "angle": 0.0},
]

step = 10
starting_direction = directions[randint(0, 3)]


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return {"r": r, "g": g, "b": b}


def process(t: Turtle, repetitions: int):
    global turtle
    turtle = t
    turtle.speed(0)
    for i in range(repetitions):

        color = random_color()
        direction = directions[randint(0, 3)]
        look_towards_direction(direction)
        turtle.pencolor(color["r"], color["g"], color["b"])
        turtle.forward(step)


def look_towards_direction(new_direction):
    turtle.setheading(new_direction["angle"])
