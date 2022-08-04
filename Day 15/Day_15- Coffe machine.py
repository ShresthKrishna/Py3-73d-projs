
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def check_resources(cof):
    for i in resources:
        if i in resources and MENU[cof]["ingredients"]:
            if resources[i]>MENU[cof]["ingredients"][i]:
                return 1
            else:
                return 0


def coins(q, d, n, p, cof):
    cost = MENU[cof]["cost"]
    count = q + d + n + p
    change = count - cost
    return change


def success_payment(change1):
    if change1 < 0:
        print("sorry that you are broke")
        return False
    else:
        global profit
        profit+= change1
        return True

def transaction(money):
    if money:
        return True
    else:
        return False

is_on=True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    change1 = 0
    if choice=='report':
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\n Profit: {profit}")

    elif choice=='off':
        is_on=False
    else:
        if check_resources(choice):

            quarters = int(input("How many quarters"))*0.25
            dime = int(input("How many dimes"))*0.1
            nickels = int(input("How many nickels"))*0.05
            pennies = int(input("How many pennies"))*0.01
            pay=coins(quarters, dime, nickels, pennies, choice)

            if transaction(success_payment(pay)):
                print(f"Here is your{choice}")
                print(f"Here is your {pay}")







