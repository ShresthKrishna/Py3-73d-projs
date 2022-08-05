from turtle import Turtle
from snake import Snake
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.turtlesize(0.5,0.5)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        self.goto(random.randint(-270,270),random.randint(-270,270))
