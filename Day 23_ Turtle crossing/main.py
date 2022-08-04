from turtle import Screen
import time
from cars import Cars
from player import Player
from score import Score

# Configuring the Interface of Game
screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
'''THIS TURNS OFF THE SCREEN TRACING I.E HOW THE TURTLE OBJECTS GO TO CERTAIN POSITION AT START'''
player = Player()

car = Cars()
screen.onkey(key="w", fun=player.go_up)
screen.onkey(key='s', fun=player.go_down)
screen.onkey(key='d', fun=player.go_right)
score = Score()
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()

    for car_s in car.gari:
        if player.distance(car_s) < 20:
            game_on = False
            score.game_over()

    if player.ycor() > 280:
        player.restart()
        score.add()
        car.car_speed()
screen.exitonclick()
