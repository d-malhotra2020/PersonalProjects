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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def make_coffee(drink_name, order_ingredients):
    #deduct the required ingredients from the resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕️☕️☕️☕️☕️☕️☕️☕️ Enjoy")
def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough


def process_coins():
    """returns the total caluclated from coins inserted"""

    print("Please insert coins")
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.10
    total += int(input("how many nickels: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total


def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 3)
        print(f"Here is your ${change} in change ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded")
        return False


is_on = True

while is_on:
    option = input("What would you like? (espresso/latte/cappuccino: ")
    if option == "off":
        is_on = False
    elif option == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['milk']}ml")
        print(f"Money: {profit}")
    else:
        drink = MENU[option]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(option, drink["ingredients"])

