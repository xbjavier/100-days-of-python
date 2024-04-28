from random import random, randint
from turtle import Turtle, Screen


def draw_square_on_starting_point(posX: float, posY: float, startBackwards=False):
    t = Turtle()
    t.penup()
    t.setpos(posX, posY)
    if startBackwards:
        t.right(180)
    t.pendown()
    for i in range(4):
        t.forward(100)
        t.left(90)


def challenge_1_draw_a_square():
    draw_square_on_starting_point(0, 0)
