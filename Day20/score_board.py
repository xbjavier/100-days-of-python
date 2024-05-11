from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(pos[0], pos[1])
        self.pixel_size = 20
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score}",
            align="center",
            font=("Arial", int(self.pixel_size), "normal"),
        )

    def reset(self):
        self.score = 0
        self.update_score()

    def add_points(self, points=10):
        self.score += points
        self.update_score()
