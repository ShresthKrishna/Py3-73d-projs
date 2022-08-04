import turtle
from turtle import Turtle, Screen
import random
# tim = Turtle("turtle")
screen = Screen()
screen.setup(width=500, height=400)
race_on = False
user_bet = screen.textinput(title="MAke BEts Dannasama", prompt="Which kachua will win?")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
x = -230
y = -70

all_turtle = []
for i in range(0,6):
    new = Turtle("turtle")
    new.up()
    new.color(color[i])
    y += 30
    new.goto(x=x, y=y)
    all_turtle.append(new)
# tim.color(color[i+1])
# tim.goto(x, y)
if user_bet:
    race_on = True
while race_on:
    for j in all_turtle:
        if j.xcor() > 230:
            race_on = False
            winning_col = j.pencolor()
            if winning_col == user_bet:
                print(f"Tum ssattebazi jeet gaye {winning_col} jeeta hai")
            else:
                print(f"Aaj se tumhari biwi hamari hui {winning_col} mard nikla")
        rand_dist = random.randint(0, 10)
        j.forward(rand_dist)

screen.exitonclick()