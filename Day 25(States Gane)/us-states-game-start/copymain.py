from turtle import Screen, Turtle
import pandas

screen = Screen()
states = pandas.read_csv("50_states.csv")
screen.setup(width=750, height=500)
screen.bgpic("blank_states_img.gif")
count = 0
game_on = True
state_names = states.state.to_list()
while count!=10 and game_on:
    guess = screen.textinput(title="Guess the States", prompt="Your Guess").title()
    if guess in state_names:
        print(guess)
        x = int(states.x[states.state == guess])
        y = int(states.y[states.state == guess])
        pos = (x,y)
        turt = Turtle()
        turt.hideturtle()
        turt.up()
        turt.goto(pos)
        name = guess

        turt.write(f"{name}",font=("Arial", 8, "normal"))
    else:
        count+=1
        if count == 10:
            game_on = False
            print("Loser")
screen.exitonclick()