from turtle import Turtle, Screen

from challenge_1 import challenge_1_draw_a_square as challenge_1_process
from challenge_2 import challenge_2_dashed_line as challenge_2_process
from challenge_3 import process as challenge_3_process
from challenge_4 import process as challenge_4_process
from challenge_5 import process as challenge_5_process

screen = Screen()
screen.colormode(255)

t = Turtle()
# challenge_1_process(t)
# challenge_2_process(t, screen, 100)
# challenge_3_process(t)
# challenge_4_process(t, 3000)
challenge_5_process(t, 100, 18)
screen.exitonclick()
