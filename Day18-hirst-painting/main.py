from turtle import Turtle, Screen
import random
# import colorgram
#
# color_list = []
# color = colorgram.extract("images.jpg", 15)
#
# for c in color:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     rgb = (r, g, b)
#     color_list.append(rgb)

color_list = [(204, 154, 113), (132, 164, 187),
              (150, 89, 55), (60, 106, 134), (195, 140, 160),
              (134, 177, 156), (138, 72, 97), (61, 121, 93),
              (222, 202, 130), (170, 149, 49), (208, 90, 69)]

dot = 100
turtle = Turtle()
turtle.penup()
turtle.speed("fastest")
turtle.hideturtle()
screen = Screen()
screen.colormode(255)


turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)


for dot_count in range(1, dot+1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen.exitonclick()
