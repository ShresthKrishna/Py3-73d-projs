import turtle
import time
from turtle import Turtle, Screen
import random
turtle.colormode(255)
screen = Screen()
screen.tracer(0)
game = True
def move():
    car.bk(20)
for i in range(20):
    car = Turtle("square")
    car.shape("square")
    car.shapesize(stretch_wid=1, stretch_len=3)
    car.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    car.up()
    car.goto(300, random.randint(-270, 270))
    new_x = car.xcor()
    car.goto(new_x+1, car.ycor())
    time.sleep(0.1)
    screen.update()




screen.exitonclick()