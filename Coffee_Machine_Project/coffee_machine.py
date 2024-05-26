'''Imported sys module to '''
import sys

MONEY = 0.0
PENNY = .01
NICKEL = .05
DIME = .10
QUARTER = .25
coffee_selection = ''

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def insert_coins():
    '''Prompts user to insert coins to pay for coffee drink'''
    pennies = int(input("Insert pennies: ")) * PENNY
    nickels = int(input("Insert nickels: ")) * NICKEL
    dimes = int(input("Input dimes: ")) * DIME
    quarters = int(input("Insert quarters: ")) * QUARTER
    total = f"{pennies + nickels + dimes + quarters:.2f}"
    return total


def give_change():
    '''Makes change based on how much money the user enters and how much
    coffee drink costs'''
    change = f"{MONEY - MENU.get(coffee_selection).get('cost'):.2f}"
    return change


def report():
    ''' Prints a report of the available resources/money'''
    for key, value in resources.items():
        if key == 'water' or key == 'milk':
            print(f"{key.capitalize()}: {value}ml")
        elif key == 'coffee':
            print(f"{key.capitalize()}: {value}g")
    print(f"Money: ${MONEY:.2f}")


while coffee_selection != 'off':
    coffee_selection = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_selection == 'report':
        report()
    elif coffee_selection in MENU:
        for key, value in resources.items():
            if key in MENU.get(coffee_selection).get('ingredients'):
                if resources[key] < MENU.get(coffee_selection).get('ingredients').get(key):
                    print(f"Sorry there is not enough {key}")
                    break
        else:
            MONEY = float(insert_coins())
            if MONEY > MENU.get(coffee_selection).get('cost'):
                change = give_change()
                MONEY = 0.0
                print(f"Here is ${change} dollars in change.")
                for key in MENU.get(coffee_selection).get('ingredients'):
                    resources[key] = resources[key] - MENU.get(coffee_selection).get('ingredients').get(key)
                print(f"Here is your {coffee_selection}. Enjoy!")
sys.exit()
