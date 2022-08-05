import turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = turtle.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
pos = [(0,0),(20,0),(40,0)]
new = []
score = 0
screen.tracer(0)
# turtle.penup()
snake = Snake()
screen.listen()
food = Food()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
snake_score = ScoreBoard()
game_on = True
while game_on:
    screen.update()
    time.sleep(.05)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        snake_score.score_add()
    if (snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280):
        snake.reset()
        snake_score.game_over()
        screen.exitonclick()
    for i in snake.segment[1:]:
        if snake.head.distance(i)<10:
            snake.reset()
            snake_score.score = 0
            snake_score.update()



screen.mainloop()