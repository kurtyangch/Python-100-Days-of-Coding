from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.speed("fastest")
screen.colormode(255)
direction = [0, 90, 180, 270]


# generate random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_c = (r, g, b)
    return random_c

# 畫三角形到十邊形
# def draw(n):
#     degree = 360 / n
#     for _ in range(n):
#         turtle.right(degree)
#         turtle.forward(50)
#
# for i in range(3, 11):
#     draw(i)

# random walk
# for _ in range(100):
#     turtle.pencolor(random_color())
#     turtle.forward(20)
#     turtle.setheading(random.choice(direction))


# 畫圓形
def draw_spirograph(angle):
    for _ in range(int(360/angle)):
        turtle.pencolor(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading()+angle)


draw_spirograph(5)

screen.exitonclick()
