import pandas
import random
data = pandas.read_csv("french_words.csv")
word = pandas.DataFrame(data).to_dict(orient="records")
to_learn= word
choose = random.choice(word)
print(choose)
to_learn.remove(choose)
print(to_learn)

