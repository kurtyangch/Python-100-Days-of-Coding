from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.listen()
color_list = ["red", "orange", "yellow", "blue", "purple"]
turtle_list = []
user_bet = screen.textinput(title="Make a bet!", prompt="Which turtle will win the race?  Enter a color. ").lower()
game_is_on = False
if user_bet:
    game_is_on = True

# 把烏龜移到原點
    for turtle_index in range(5):
        turtle = Turtle(shape="turtle")
        turtle.color(color_list[turtle_index])
        turtle.penup()
        turtle.goto(-230, -90 + turtle_index * 30)
        turtle_list.append(turtle)

while game_is_on:

    for turtle in turtle_list:
        if turtle.xcor() > 220:
            game_is_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You win, {winner} is the winner.")
            else:
                print(f"You lost, {winner} is the winner")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
