from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from add_resources import AddResources

# creating objects
coffee_menu = Menu()
maker = CoffeeMaker()
money_pad = MoneyMachine()
refill_resources = AddResources()

is_on = True

while is_on:

    name = input(f'What would you like? ({coffee_menu.get_items()}): ').lower()
    # Turning the machine off
    if name == 'off':
        print("Turning the coffee maker machine off")
        is_on = False
    elif name == 'report':
        maker.report()
        money_pad.report()
    elif name == "latte" or name == "espresso" or name == "cappuccino":
        ingredients = coffee_menu.find_drink(name).ingredients
        cost_of_drink = coffee_menu.find_drink(name).cost
        can_make = maker.is_resource_sufficient(MenuItem(name, ingredients["water"], ingredients["milk"],
                                                         ingredients["coffee"], cost_of_drink))
        if can_make:
            proceed_payment = money_pad.make_payment(cost_of_drink)
            if proceed_payment:
                maker.make_coffee(MenuItem(name, ingredients["water"], ingredients["milk"], ingredients["coffee"],
                                           cost_of_drink))
    # To refill the resources od the machine
    elif name == 'refill':
        refill_resources.add_more_resources()





