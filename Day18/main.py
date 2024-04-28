from random import random, randint
from turtle import Turtle, Screen

from challenge_4 import process as challenge_4_process

screen = Screen()
screen.colormode(255)

t = Turtle()
challenge_4_process(t, 300)
screen.exitonclick()
