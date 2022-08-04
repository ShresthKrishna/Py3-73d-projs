import random
import turtle
from color import col_list
turtle.colormode(255)
turtle.heading()
turtle.speed('fastest')
turtle.hideturtle()
x = -250
y = -100
for i in range(10):
    turtle.up()
    turtle.setpos(x, y)
    turtle.down()
    for j in range(10):
        turtle.penup()
        turtle.fd(50)
        turtle.pendown()
        turtle.dot(20, random.choice(col_list))
        y += 5
turtle.position()
turtle.Screen().exitonclick()

