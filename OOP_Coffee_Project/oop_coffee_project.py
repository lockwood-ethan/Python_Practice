from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
should_continue = True


while should_continue == True:
    coffee_choice = input(f"What would you like? ({menu.get_items()}) ")
    if coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_drink = menu.find_drink(coffee_choice)
        should_continue = coffee_maker.is_resource_sufficient(coffee_drink)
        if should_continue == True:
            should_continue = money_machine.make_payment(coffee_drink.cost)
            if should_continue == True:
                coffee_maker.make_coffee(coffee_drink)
sys.exit()
