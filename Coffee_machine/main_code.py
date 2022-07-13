from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
money = MoneyMachine()
maker_coffee = CoffeeMaker()
menu = Menu()


maker_coffee.report()
money.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        maker_coffee.report()
        money.report()
    else:
        order = menu.find_drink(choice)
        print(order)


