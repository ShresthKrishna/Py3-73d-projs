
import turtle as t


def dot_line(obj, times):
    for i in range(times):
        obj.forward(5)
        obj.pu()
        obj.forward(5)
        obj.pd()


tim = t.Turtle("turtle")
dot_line(tim, 10)
screen = t.Screen()
screen.exitonclick()
