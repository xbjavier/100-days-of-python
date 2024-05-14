from turtle import Turtle, Screen


class PongPad:
    def __init__(self, screen_min, screen_max, x_position) -> None:
        self.pad = Turtle("square")
        self.pad.shapesize(0.5, 2.5, 1)
        self.pad.setheading(90)
        self.pad.color("white")
        self.pad.penup()
        self.screen_min = (
            screen_min[0],
            screen_min[1] + self.pad.shapesize()[1] / 2.0,
        )
        self.screen_max = (screen_max[0], screen_max[1] - self.pad.shapesize()[1] / 2.0)
        self.pad.teleport(x_position, 0)

        self.score_turtle = Turtle()
        self.score_turtle.penup()
        self.score_turtle.color("white")
        self.score_turtle.hideturtle()
        self.score_turtle.goto(x_position, screen_max[1] + 20)
        self.pixel_size = 20
        self.score = 0
        self.update_score()

    def position(self):
        return (self.pad.pos()[0], self.pad.pos()[1])

    def height(self):
        return self.pad.shapesize()[1]

    def update_score(self):
        self.score_turtle.clear()
        self.score_turtle.write(
            arg=f"{self.score}",
            align="center",
            font=("Arial", int(self.pixel_size), "normal"),
        )

    def add_points(self, points=1):
        self.score += points
        self.update_score()

    def bind_movement(self, screen: Screen, up_key: str, down_key: str):
        screen.onkeypress(self.up, up_key)
        screen.onkeypress(self.down, down_key)
        pass

    def up(self):
        if self.pad.ycor() >= self.screen_max[1]:
            return
        self.pad.forward(10)

    def down(self):
        if self.pad.ycor() <= self.screen_min[1]:
            return
        self.pad.backward(10)
