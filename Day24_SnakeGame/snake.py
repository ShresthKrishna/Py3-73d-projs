from turtle import Turtle
POS = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segment = []
        self.create()
        self.head = self.segment[0]
    def create(self):
        for i in POS:
            self.addsegment(i)
    def addsegment(self,pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segment.append(new_segment)

    def extend(self):
        self.addsegment(self.segment[-1].pos())
    def move(self):
        for i in range(len(self.segment)-1,0,-1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)
        self.segment[0].fd(MOVE_DISTANCE)

    def reset(self):
        for i in self.segment:
            i.goto(4000,4000)
        self.segment.clear()
        self.create()
        self.head = self.segment[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)