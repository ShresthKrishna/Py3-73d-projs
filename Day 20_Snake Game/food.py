from turtle import Turtle
import random as r

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red", "blue")
        self.up()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = r.randint(-280,280)
        random_y = r.randint(-280,280)
        self.goto(random_x, random_y)