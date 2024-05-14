import time
from turtle import Screen
from pad import PongPad
from pong_ball import PongBall

screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
screen.tracer(0)
screen.setup(600, 400)

screen_min = (-(screen.window_width() / 2.0) + 15, -(screen.window_height() / 2.0) + 50)
screen_max = ((screen.window_width() / 2.0) - 15, (screen.window_height() / 2.0) - 50)

left_pad = PongPad(screen_min, screen_max, screen_min[0])
right_pad = PongPad(screen_min, screen_max, screen_max[0] - 5)

left_pad.bind_movement(screen, "w", "s")
right_pad.bind_movement(screen, "Up", "Down")

pong_ball = PongBall(screen_min, screen_max, left_pad, right_pad)
screen.listen()
game_on = True

screen.update()
while game_on:
    time.sleep(0.1)
    screen.update()
    pong_ball.pad_detection()
    if pong_ball.player_point():
        continue
    pong_ball.wall_detection()
    pong_ball.move()


screen.exitonclick()
