from turtle import Screen, Turtle
import pandas
from check_states import States

screen = Screen()
states = pandas.read_csv("50_states.csv")
screen.setup(width=750, height=500)
screen.bgpic("blank_states_img.gif")
state_names = states.state.to_list()
game_on = True
state = States()
guessed_list = []
score = 0
incorrect = 0
while game_on:
    guess = screen.textinput(title=f"{score}/50 States Correct", prompt="Your Guess").title()
    if guess == 'Exit':
        break
    elif guess in state_names:
        x = int(states.x[states.state == guess])
        y = int(states.y[states.state == guess])
        posi = (x,y)
        state.check(name=guess, pos= posi)
        if guess not in guessed_list:
            guessed_list.append(guess)
            score += 1
    else:
        incorrect += 1
    if incorrect == 10 or score == 50:
        game_on = False
if score == 50:
    print("You a white Supramist")
elif incorrect == 10:
    print("Know your geography, n- word")
# missed = {"missed_states": []}
# for i in state_names:
#     if i not in guessed_list:
#         missed["missed_states"].append(i)
missed = [name for name in state_names if name not in guessed_list]
data = pandas.DataFrame(missed)
data.to_csv("missed states.csv")
screen.exitonclick()