from menu import MENU

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def print_report():
    for key in resources:
        if key == "water" or key == "milk":
            print(f"{key.title()}: {resources[key]}ml")
        elif key == "coffee":
            print(f"{key.title()}: {resources[key]}g")

    print(f"Money: ${profit}")


def check_resources(order):
    recipe = MENU[order]["ingredients"]
    for item in recipe:
        if recipe[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def process_coins(order):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    total_coins = 0
    total_coins += quarters * .25
    total_coins += dimes * .10
    total_coins += nickels * .05
    total_coins += pennies * .01
    return total_coins


def verify_transaction(total_coins, order):
    change = 0
    cost = float(MENU[order]["cost"])
    if total_coins >= cost:
        change = total_coins - cost
        if change > 0:
            if change >= 1:
                print("Here is ${:.2f}".format(change) + " dollars in change.")
            else:
                print("Here is ${:.2f}".format(change) + " cents in change.")
        global profit
        profit += cost
    else:
        print("Sorry that's not enough money.  Money refunded.")


def make_coffee(order):
    drink = MENU[order]["ingredients"]
    for item in drink:
        resources[item] -= drink[item]


def run_machine():
    take_orders = True

    while take_orders:
        order = input("What would you like? (espresso/latte/cappuccino):").lower()
        if order == "off":
            print("OK.  Shutting down coffee machine...")
            take_orders = False
        elif order == "report":
            print_report()
        elif order not in MENU:
            print(f"Sorry, we don't have {order} on the menu. Please try another item.")
        else:
            if check_resources(order):
                total_coins = process_coins(order)
                verify_transaction(total_coins, order)
                make_coffee(order)
            else:
                print("test")


run_machine()
