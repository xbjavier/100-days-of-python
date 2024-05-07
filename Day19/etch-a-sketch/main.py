from turtle import Turtle, Screen

t = Turtle()
t.speed(0)
screen = Screen()


def move_forward():
    t.forward(20)


def rotate(right):
    if right:
        t.setheading(t.heading() - 10)
    else:
        t.setheading(t.heading() + 10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.onkeypress(lambda: rotate(True), "Right")
screen.onkeypress(lambda: rotate(False), "Left")
screen.onkeypress(lambda: rotate(True), "d")
screen.onkeypress(lambda: rotate(False), "a")
screen.onkeypress(clear, "c")
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_forward, "w")

screen.listen()
screen.exitonclick()
