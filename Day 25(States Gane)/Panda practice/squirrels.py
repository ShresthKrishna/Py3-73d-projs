import pandas
data = pandas.read_csv("Squirrel_Data.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == 'Gray'])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_squirrel = len(data[data["Primary Fur Color"] == 'Black'])
print(grey_squirrel)
print(cinnamon_squirrel)
print(black_squirrel)
furs = {
    'Fur Color':['grey', 'cinnamon', 'black'],
    'Count':[grey_squirrel, cinnamon_squirrel, black_squirrel]
}
data_color = pandas.DataFrame(furs)
data_color.to_csv("Squirrel Fur.csv")
