from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal ')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.clear()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.clear_scr()

    def clear_scr(self):

        self.write(f"Score :{self.score} ", False, font=FONT, align=ALIGNMENT)

    def score_add(self):
        self.score +=1
        self.clear()
        self.clear_scr()
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)