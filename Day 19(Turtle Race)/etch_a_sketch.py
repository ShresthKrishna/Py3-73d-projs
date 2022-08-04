from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move():
    tim.fd(10)


def back():
    tim.bk(10)


def right():
    tim.right(10)


def left():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
#    or just  use tim.reset()


screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=back)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
