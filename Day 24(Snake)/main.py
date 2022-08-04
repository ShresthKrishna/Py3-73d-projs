from turtle import Screen
from snake import Snake
import time
from food import Food
from score import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)    #to turn of the tracer
# turtle.Turtle
# square_1=turtle.Turtle(shape="square")
# square_1.color("white")
# square_1.setx(0)
# square_2 = turtle.Turtle(shape= "square")
# square_2.up()
# square_2.setx(-20)
# square_3 = turtle.Turtle(shape= "square")
# square_3.up()
# square_3.setx(-40)
# square_2.color("white")
# square_3.color("white")
#   =======================    ooo   0000000  ================
#                             00000  0000000
#                             00000  00  00
#   =======================    000   00   00 =================
snake = Snake()
s_food = Food()
screen.listen()
score = ScoreBoard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update() # to update/refresh the screen
    time.sleep(0.09)
    snake.move()
    score
    #Detects collision with food
    if snake.head.distance(s_food) < 15:
        s_food.refresh()
        score.score_add()
        score.clear_scr()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < (-280) or snake.head.ycor() > 280 or snake.head.ycor() < (-280):
        score.highs()
        snake.reset()
    # Detects collision with body part
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            score.highs()











screen.exitonclick()
