import time
from turtle import Turtle, Screen
from random import randint
from typing import List
from snake import Snake, vector2
from score_board import ScoreBoard

screen = Screen()
screen.setup(300, 300)
screen.colormode(255)
screen.bgcolor("black")
screen.tracer(0)


food = None

min_x = int(-(screen.window_width() / 2.0) + 20.0)
max_x = int((screen.window_width() / 2.0) - 20.0)

min_y = int(-(screen.window_height() / 2.0) + 20.0)
max_y = int((screen.window_height() / 2.0) - 20.0)

min = vector2()
min.x = min_x
min.y = min_y

max = vector2()
max.x = max_x
max.y = max_y

snake = Snake()
snake.setup("white", screen, min, max)
score_board = ScoreBoard((0, max.y - 20.0))

game_on = True


def random_food():
    global food

    if food == None:
        food = Turtle("circle")
        food.shapesize(0.5)
        food.color("white")
        food.penup()

    r = random_position()
    food.goto(r[0], r[1])


def random_position():
    x = randint(min_x, max_x)
    y = randint(min_y, max_y)
    return (x, y)


screen.listen()

random_food()

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.wall_collision():
        game_on = False
        break
    if snake.check_food(food):
        score_board.add_points()
        random_food()


screen.exitonclick()
