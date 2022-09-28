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


profit = 0
# coffee_maker_on = True


def enough_money(drink, money_inserted):
    global profit
    money_needed = MENU[drink]["cost"]
    if money_needed > money_inserted:
        print(f"Sorry that's not enough money. Money refunded: ${money_inserted}.")
        money_returned = 0
        make_drink = False
        return money_returned, make_drink
    elif money_needed <= money_inserted:
        money_returned = round(money_inserted - money_needed, 2)
        profit += round(money_needed, 2)
        make_drink = True
        return money_returned, make_drink


def modify_resources(drink):
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    resources['water'] -= MENU[drink]['ingredients']['water']
    if drink != 'espresso':
        resources['milk'] -= MENU[drink]['ingredients']['milk']


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def enough_resources(drink):
    coffee_needed = MENU[drink]['ingredients']['coffee']
    water_needed = MENU[drink]['ingredients']['water']
    if coffee_needed > resources['coffee']:
        print("Sorry there is not enough coffee.")
        make_drink = False
        return make_drink
    # else:
    #     make_drink = True
    if water_needed > resources['water']:
        print("Sorry there is not enough water.")
        make_drink = False
        return make_drink
    else:
        make_drink = True
    if drink != 'espresso':
        milk_needed = MENU[drink]['ingredients']['milk']
        if milk_needed > resources['milk']:
            make_drink = False
            return make_drink
        else:
            make_drink = True

    return make_drink


def insert_coins():
    print('Please Insert coins:')
    quarters = int(input("How many Quarters? "))
    dimes = int(input('How many Dimes? '))
    nickels = int(input('How many Nickels? '))
    pennies = int(input('How many Pennies? '))
    money_inserted = round((quarters*0.25)+(dimes*0.1)+(nickels*0.05)+(pennies*0.01), 2)
    return money_inserted


def turn_off():
    coffee_maker_on = False
    return coffee_maker_on


def add_resources():
    water = int(input("How many water? "))
    coffee = int(input("How many coffee? "))
    milk = int(input("How many milk? "))
    resources['water'] += water
    resources['coffee'] += coffee
    resources['milk'] += milk
    print("Done!!!")
    print_report()


def main():
    coffee_maker_on = True
    while coffee_maker_on:
        drink = input("What would you like? (espresso/latte/cappuccino):").lower()
        if drink == 'report':
            print_report()
        elif drink == 'off':
            print("Powering the Coffee Maker Machine off")
            coffee_maker_on = turn_off()
        elif drink == 'espresso' or drink == 'cappuccino' or drink == 'latte':
            can_make = enough_resources(drink)
            if can_make:
                money_inserted = insert_coins()
                money_returned, make_drink = enough_money(drink, money_inserted)
                if make_drink:
                    modify_resources(drink)
                    print(f"Here's your {drink}")
                    if money_returned > 0:
                        print(f"Your change is ${money_returned}.")
                    print_report()
        elif drink == 'add resources':
            add_resources()
        else:
            print('Please enter a valid option ')


main()
