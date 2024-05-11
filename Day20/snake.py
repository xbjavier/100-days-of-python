from turtle import Turtle, Screen
from typing import List


class Snake:
    def __init__(self) -> None:
        self.head = None
        self.body: List[Turtle] = []
        self.color: str = "white"
        self.min_position: vector2 = vector2()
        self.max_position: vector2 = vector2()

    def setup(
        self, color: str, screen: Screen, min_pos, max_pos, initial_pieces: int = 3
    ):
        self.__set_color(color)
        x = 0
        for _ in range(initial_pieces):
            t = self.create_body(x, 0)
            x -= t.shapesize()[0] + 10
            self.body.append(t)
        self.head = self.body[0]
        self.min_position.x = min_pos.x - 10.5
        self.min_position.y = min_pos.y - 10.5
        self.max_position.x = max_pos.x + 10.5
        self.max_position.y = max_pos.y + 10.5
        self.register_input(screen)
        self.head.speed(0)

    def __set_color(self, color: str):
        self.color = color

    def create_body(self, x, y) -> Turtle:
        piece = Turtle("square")
        piece.shapesize(0.5)
        piece.color(self.color)
        piece.penup()
        piece.goto(x, y)
        self.body.append(piece)
        return piece

    def move_north(self):
        heading = self.head.heading()
        if heading == 180 or heading == 0:
            self.head.setheading(90)

    def move_south(self):
        heading = self.head.heading()
        if heading == 180 or heading == 0:
            self.head.setheading(270)

    def move_east(self):
        heading = self.head.heading()
        if heading == 90 or heading == 270:
            self.head.setheading(0)

    def move_west(self):
        heading = self.head.heading()
        if heading == 90 or heading == 270:
            self.head.setheading(180)

    def register_input(self, screen: Screen):
        screen.onkey(self.move_north, "Up")
        screen.onkey(self.move_south, "Down")
        screen.onkey(self.move_east, "Right")
        screen.onkey(self.move_west, "Left")
        screen.onkey(self.move_north, "w")
        screen.onkey(self.move_south, "s")
        screen.onkey(self.move_east, "d")
        screen.onkey(self.move_west, "a")

    def wall_collision(self) -> bool:
        if (
            self.head.xcor() <= self.min_position.x
            or self.head.xcor() >= self.max_position.x
            or self.head.ycor() <= self.min_position.y
            or self.head.ycor() >= self.max_position.y
        ):
            return True
        return False

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            x = self.body[i - 1].xcor()
            y = self.body[i - 1].ycor()
            self.body[i].goto(x, y)
        self.head.forward(10)

    def check_food(self, food: Turtle) -> bool:
        food_pos = food.pos()
        distance = self.head.distance(food_pos[0], food_pos[1])
        if distance <= 15:
            print("food clear")
            part = self.body[-1]
            self.create_body(part.xcor(), part.ycor())
            return True
        return False


class vector2:
    def __init__(self):
        self.x = 0
        self.y = 0
