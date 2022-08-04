from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on =True

while is_on:
    choice = input(f"What would you like? {menu.get_items()} : ").lower()
    print(f"Your cost for your {menu.find_drink(choice).name} is: ${menu.find_drink(choice).cost} ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        enough_resources = coffee_maker.is_resource_sufficient(menu.find_drink(choice))
        payment = money_machine.make_payment(menu.find_drink(choice).cost)

        if enough_resources and payment:
            coffee_maker.make_coffee(menu.find_drink(choice))