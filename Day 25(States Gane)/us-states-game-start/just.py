from turtle import Screen, Turtle
import pandas

screen = Screen()

screen.setup(width=750, height=500)
screen.bgpic("blank_states_img.gif")
states = pandas.read_csv("50_states.csv")
state_names = states.state.to_list()
guess = screen.textinput(title="Guess the States", prompt="Your Guess").title()
if guess in state_names:
    print(guess)
else:
    print("not in list")
# x = int(states.x[states.state == guess])
# y = int(states.y[states.state == guess])
# pos = (x,y)
# turt = Turtle()
# turt.hideturtle()
# turt.up()
# turt.goto(pos)
# name = guess
#
# turt.write(f"{name}",font=("Arial", 8, "normal"))
# screen.exitonclick()