from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.up()
        self.goto(-170,270)
        self.hideturtle()
        self.color("white")
        self.highscore = int(open("highscore.txt").read())
        self.write(f"Score : {self.score}        High Score: {self.highscore}",font=('Arial', 22, 'normal'))

    def update(self):
        self.clear()
        self.color("white")
        self.write(f"Score : {self.score} High Score: {self.highscore}", font=('Arial', 22, 'normal'))
    def game_over(self):

        self.goto(-180,0)
        self.clear()
        if self.score>self.highscore:
            with open("highscore.txt","w+") as file:
                file.write(f"{self.score}")
                self.highscore = self.score
                file.close()

        self.write(f"Your Score:{self.score}   High Score:{self.highscore}",font=('Arial', 22, 'normal'))

    def score_add(self):
        self.score+=1
        self.update()
