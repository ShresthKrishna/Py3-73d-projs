import turtle as t
import random as r
color=["blue","BlueViolet", "brown", "gold", "green",
       "DarkOrchid", "DarkViolet", "black", "red"]
angle = [0, 90, 180, 270]

def random_color():
    red = r.randint(0,255)
    g = r.randint(0, 255)
    b = r.randint(0, 255)
    r_color = (red, g, b)
    return r_color

def headed(obj):
    for i in range(200):
            obj.color(random_color())
            obj.forward(25)
            obj.setheading(r.choice(angle))


tim = t.Turtle("turtle")
t.colormode(255)
tim.pensize(5)
tim.speed('fast')
headed(tim)
screen = t.Screen()
screen.exitonclick()