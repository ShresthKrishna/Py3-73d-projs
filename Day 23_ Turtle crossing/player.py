from turtle import Turtle
START = (0,-280)
DIST = 15
END = 280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.up()
        self.goto(START)
        self.settiltangle(90)
        self.color("green", "purple")
        self.go_up()
        self.go_down()

    def go_up(self):
        new_y = self.ycor() + DIST
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - DIST
        self.goto(self.xcor(), new_y)

    def go_right(self):
        new_x = self.xcor() + DIST
        y = self.ycor()
        self.goto(new_x, y)

    def restart(self):
        self.goto(START)