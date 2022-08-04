from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.clear()
        self.up()
        self.hideturtle()
        self.goto(-100, 250)
        self.color("black")
        self.count()

    def count(self):

        self.write(f"Score:{self.score}", font= FONT, align="right")

    def add(self):
        self.score += 1
        self.clear()
        self.count()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Sorry Game Over!!!!", font= FONT, align="center")

