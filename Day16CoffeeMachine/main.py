from coffee import MENU, resources


def is_resource_sufficient(order_ingredients):
    """Returns True if enough resources are available in the machine and False otherwise"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, False otherwise"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources inside the machine"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your ☕️ {drink_name}. Enjoy!")


machine_on = True
money = 0

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino)")
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])
