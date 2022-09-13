from colors import colors_list
from turtle import Turtle, Screen
import random

screen = Screen()
turt = Turtle()
turt.speed(0)
turt.penup()
screen.colormode(255)
turt.setpos(-250,-250)
turt.hideturtle()

for hight in range(10):

    for lenght in range(10):
        turt.dot(20,random.choice(colors_list))
        turt.forward(50)

    turt.left(90)
    turt.forward(50)
    turt.left(90)
    turt.forward(500)
    turt.right(180)


screen.exitonclick()
