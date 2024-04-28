from random import randint
from turtle import Turtle, Screen


def challenge_3(
    pen_color_r: int,
    pen_color_g: int,
    pen_color_b: int,
    repetition: int,
    angle: float,
    t: Turtle,
    distance=25,
):
    t.pencolor(pen_color_r, pen_color_g, pen_color_b)

    for i in range(repetition):
        t.left(angle)
        t.forward(distance)

    for i in range(repetition):
        t.right(angle)
        t.forward(distance)
    pass


figures = [
    {"figure": "triangle", "moves": 3},
    {"figure": "square", "moves": 4},
    {"figure": "pentagon", "moves": 5},
    {"figure": "hexagon", "moves": 6},
    {"figure": "heptagon", "moves": 7},
    {"figure": "octagon", "moves": 8},
    {"figure": "nonagon", "moves": 9},
    {"figure": "decagon", "moves": 10},
]

screen = Screen()
screen.colormode(255)

t = Turtle()


def process():
    for figure in figures:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        challenge_3(r, g, b, figure["moves"], 360 / figure["moves"], t)
