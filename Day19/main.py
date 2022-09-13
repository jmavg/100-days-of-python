import random
from turtle import Turtle, Screen, color, position

screen = Screen()
screen.setup(height=400,width=500)
colors = ["red","green","yellow","purple","orange","blue"]
y_position = [-70,-40,-10,20,50,80]
user_bet = screen.textinput(title="Choose color", prompt="Choose a color!")
turtles = []
game_over = False

for i in colors:

    turt = Turtle(shape="turtle")
    turt.penup()
    turt.color(i)
    turt.goto(-240,y_position[0])
    y_position.pop(0)
    turtles.append(turt)

while not game_over:

    for t in turtles:
        if t.xcor() < 230:
            t.fd(random.randint(0,10))
        else:
            game_over = True
            if t.pencolor() == user_bet:
                print(F"The turtle {t.pencolor()} won! You won!")
            else:
                print(F"The turtle {t.pencolor()} won! You lost!")

screen.exitonclick()
