from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("courier", 40, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("courier", 40, "normal"))
    def l_count(self):
        self.l_score +=1

        self.update()
    def r_count(self):
        self.r_score +=1

        self.update()