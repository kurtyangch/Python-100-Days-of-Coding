from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

on = True
while on:
    option = menu.get_items()
    ask = input(f"What would you like? {option}: ").lower()
    if ask == "off":
        on = False
    elif ask == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(ask)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)






