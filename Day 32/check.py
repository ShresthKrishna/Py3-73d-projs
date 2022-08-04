import random
with open("./letter_templates/letter_1.txt") as file:
    letter_1 = file.readlines()
with open("./letter_templates/letter_2.txt") as file:
    letter_2 = file.readlines()
with open("./letter_templates/letter_3.txt") as file:
    letter_3 = file.readlines()
letters = [letter_3, letter_2, letter_1]
x = random.choice(letters)
x = [y.replace('[NAME]', f"{x['name']}") for y in x]