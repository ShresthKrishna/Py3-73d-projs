import turtle as t
import random as r
color=["blue","BlueViolet", "brown", "gold", "green",
       "DarkOrchid", "DarkViolet", "black", "red"]
def shape(obj):
    for i in range(3,10):
        obj.color(r.choice(color))
        for j in range(1,i+1):
            obj.forward(100)
            obj.right(360/i)

tim = t.Turtle("turtle")
shape(tim)
screen = t.Screen()
screen.exitonclick()