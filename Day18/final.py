from turtle import Turtle, Screen, screensize
from random import randint, choice
import colorgram


def process(
    turtle: Turtle,
    screen: Screen,
    rows: int,
    col: int,
    space: float,
    reference: str,
    total_colors: int = 10,
    dot_size: int = 20,
):
    colors = colorgram.extract(reference, total_colors)
    calculated_space = space + dot_size

    total_width = (col + 3) * dot_size + (dot_size / 2)
    total_height = (rows + 4) * dot_size

    initial_x = -(total_width / 2) + calculated_space
    initial_y = -(total_height / 2) + calculated_space + (dot_size / 2)

    screen.setup(total_width, total_height)
    turtle.teleport(initial_x, initial_y)

    screensize(total_width, total_height)
    turtle.hideturtle()

    for i in range(rows):
        for j in range(col):
            color = choice(colors)
            turtle.dot(dot_size, color.rgb)
            turtle.teleport(turtle.xcor() + calculated_space)
        turtle.teleport(initial_x, turtle.ycor() + calculated_space)
