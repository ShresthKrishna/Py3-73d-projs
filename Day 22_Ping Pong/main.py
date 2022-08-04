from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
score = ScoreBoard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Ping - Pong")
# paddle = Turtle("square")
# paddle.up()
# paddle.shapesize(stretch_len=1, stretch_wid=5)
# paddle.color("white")
# paddle.goto(350, 0)
r_paddle = Paddle(pos=(350, 0))
l_paddle = Paddle(pos=(-350, 0))
ball = Ball()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="s", fun=l_paddle.go_down)
speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        speed *= 0.9

    elif ball.xcor() > 370:
        ball.restart()
        score.l_count()


    elif ball.xcor() < -370:
        ball.restart()
        score.r_count()


screen.exitonclick()


