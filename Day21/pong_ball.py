from random import randint
import math
from turtle import Turtle
from pad import PongPad


class PongBall:
    def __init__(
        self, min_screen, max_screen, left_pad: PongPad, right_pad: PongPad
    ) -> None:
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.shapesize(0.5)
        self.ball.up()
        self.restart_ball()
        self.screen_min = min_screen
        self.screen_max = max_screen
        self.speed = 10
        self.left_pad = left_pad
        self.right_pad = right_pad

    def move(self):
        self.ball.forward(self.speed)

    def wall_detection(self):
        pos = self.ball.pos()
        if pos[1] >= self.screen_max[1] + 15:
            self.calculate_reflection((0, -1))
        elif pos[1] <= self.screen_min[1] - 15:
            self.calculate_reflection((0, 1))

    def pad_detection(self):
        left_distance = self.ball.distance(self.left_pad.position())
        if left_distance <= (10 + self.left_pad.height()):
            self.calculate_reflection((1, 0))
        right_distance = self.ball.distance(self.right_pad.position())
        if right_distance <= (10 + self.right_pad.height()):
            self.calculate_reflection((-1, 0))

    def player_point(self) -> bool:
        pos = self.ball.pos()
        if pos[0] >= self.screen_max[0] + 10:
            self.left_pad.add_points()
            self.restart_ball()
        elif pos[0] <= self.screen_min[0] - 10:
            self.right_pad.add_points()
            self.restart_ball()
        pass

    def restart_ball(self):
        self.ball.goto(0, 0)
        rotation = randint(0, 360)
        self.ball.setheading(rotation)

    def calculate_reflection(self, normal):
        ball_pos = self.ball.pos()
        ball_x, ball_y = ball_pos[0], ball_pos[1]
        normal_x, normal_y = normal[0], normal[1]

        magnitud = math.sqrt(ball_x**2 + ball_y**2)
        vector_normal = (ball_x / magnitud, ball_y / magnitud)

        dot_product = (-vector_normal[0] * normal_x) + (-vector_normal[1] * normal_y)
        reflection = (2 * dot_product * normal_x, 2 * dot_product * normal_y)
        reflection = (
            reflection[0] + vector_normal[0],
            reflection[1] + vector_normal[1],
        )

        magnitude = math.sqrt(reflection[0] ** 2 + reflection[1] ** 2)
        reflection = (reflection[0] / magnitude, reflection[1] / magnitude)

        angle = math.atan2(reflection[1], reflection[0])
        radians = (float(angle) * 180.0) / math.pi
        self.ball.setheading(radians)
