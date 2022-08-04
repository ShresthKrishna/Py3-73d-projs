from turtle import Turtle
class States(Turtle):
    def __init__(self):
        super().__init__()

    def check(self, name, pos):
        self.name = name
        self.pos = pos
        self.up()
        self.hideturtle()
        self.goto(self.pos)
        self.write(f"{self.name}",font=("Arial", 8, "normal"), align="left")
        self.color("black")
        self.hideturtle()

