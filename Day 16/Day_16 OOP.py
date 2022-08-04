from turtle import Turtle, Screen

import another_module


print(another_module.another_var)

timmy = Turtle("turtle")
timmy.color("blue4", "chartreuse3")
timmy.forward(100)
print(timmy)
# Screen for our canvas

my_screen = Screen()
print(my_screen.bgcolor("orange"))
# Above print prints canvas height and width can be printed with canvwidth
my_screen.exitonclick()
# This helps to keep screen

# from prettytable import PrettyTable
#
# table = PrettyTable(border=True, align= "l")
#
# table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type",["Electric", "Water", "Fire"])
# print(table)
