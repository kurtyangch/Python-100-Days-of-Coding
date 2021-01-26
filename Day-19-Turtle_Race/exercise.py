from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.listen()


def forward():
    t.forward(30)


def backward():
    t.back(30)


def clockwise():
    t.right(30)


def counterclockwise():
    t.left(30)


def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="a", fun=counterclockwise)
screen.onkey(key="d", fun=clockwise)

screen.exitonclick()
