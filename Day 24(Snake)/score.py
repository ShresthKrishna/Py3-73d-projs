from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal ')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.clear()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.clear_scr()


    def clear_scr(self):
        self.clear()
        self.write(f"Score :{self.score} High Score: {self.high_score} ", font=FONT, align=ALIGNMENT)

    def highs(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear_scr()

    def score_add(self):
        self.score += 1

        self.clear_scr()
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
