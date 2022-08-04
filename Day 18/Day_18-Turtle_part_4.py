# import turtle as t
# import random as r
# angle = [0, 90, 180, 270]
#
# def random_color():
#     red = r.randint(0,255)
#     g = r.randint(0, 255)
#     b = r.randint(0, 255)
#     r_color = (red, g, b)
#     return r_color
#
# def spirograph(obj,angle):
#     for i in range(round(360/angle)):
#             obj.color(random_color())
#             obj.circle(150)
#             obj.right(angle)
#
#
# tim = t.Turtle()
# t.colormode(255)
# tim.pensize(1)
# tim.speed('fastest')
# spirograph(tim,1)
# screen = t.Screen()
# screen.exitonclick()
import random
import turtle
from color import col_list
turtle.colormode(255)
turtle.heading()
x=-150
y=-150
for i in range(10):
    turtle.up()
    turtle.setpos(x,y)
    turtle.down()
    for j in range(10):
        turtle.penup()
        turtle.fd(50)
        turtle.pendown()
        turtle.dot(20, random.choice(col_list))
        y+=5
turtle.position()



turtle.Screen().exitonclick()
