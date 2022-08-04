from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPEED =5
INCREASE = 10

class Cars:
    def __init__(self):
        super().__init__()
        self.speed = SPEED
        self.gari = []

    def create(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new = Turtle("square")
            new.shapesize(stretch_wid=1, stretch_len=2)
            new.color(random.choice(COLORS))
            new.up()
            rand_y = random.randint(-250, 250)
            new.goto(300, rand_y)
            self.gari.append(new)

    def move(self):
        for i in self.gari:
            i.bk(self.speed)

    def car_speed(self):
        self.speed += 10
