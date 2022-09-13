from turtle import Turtle, Screen
import random

screen = Screen()
turt = Turtle()
turt.speed(0)


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    turt.color(R, G, B)

for _ in range(0,361,2):
    change_color()
    turt.circle(100)
    turt.left(2)



screen.exitonclick()
