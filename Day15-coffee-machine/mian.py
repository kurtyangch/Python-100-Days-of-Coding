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

money = 0
on = True


def check_sufficient(ordered_drink):
    for item in ordered_drink:
        if ordered_drink[item] >= resources[item]:
            print(f"Sorry, {item} is not sufficient")
            return False
    return True


def process_coins():
    print("Please insert coins ")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def check_payment(payment_received, price):
    if payment_received >= price:
        change = round(payment_received - price, 2)
        print(f"Here's ${change} in change.")

        global money
        money += price
        return True
    else:
        print("Sorry that's not enough money. Money refunded  ")
        return False


def make_coffee(drink, ingredient):
    for item in ingredient:
        resources[item] -= ingredient[item]
    print(f"Here is you {drink}, enjoy it !!😁")


while on:
    ask = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if ask == "off":
        on = False

    elif ask == "report":
        print("water: ", str(resources["water"]))
        print("milk: ", str(resources["milk"]))
        print("coffee: ", str(resources["coffee"]))
        print("money: ", str(money))

    else:
        if check_sufficient(MENU[ask]["ingredients"]):
            payment = process_coins()
            if check_payment(payment, MENU[ask]["cost"]):
                make_coffee(ask, MENU[ask]["ingredients"])



