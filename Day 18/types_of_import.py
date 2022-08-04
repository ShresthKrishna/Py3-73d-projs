# from turtle import Turtle, Screen
# This method of import is a normal habit
# def square(turt):
#     for i in range(4):
#         turt.forward(100)
#         turt.left(90)
#
#
# tim = Turtle("turtle")
# tim.color("blue", "green")
# print(square(tim))
# screen = Screen()
# screen.exitonclick()
# ==========================================================
# This method is import is not a good habit
# from turtle import *
# def move(num):
#     for i in range(num):
#         forward(100)
#         left(90)
#
# move(4)
# Screen().exitonclick()

# ==========================================================
# use this method for small purpose and clearity

# import turtle
#
# tim = turtle.Turtle()

# ==========================================================

#importing as alias is also a good habit

# import turtle as t
#
# tim = t.Turtle()

# ==========================================================

# some libraries cannot be directly accessed as it is not a root part of pycharm
# but it can be installed easiy as pycharm shows the option to install it
# such as heroes library
import heroes

print(heroes.gen())

import villains

print(villains.gen())