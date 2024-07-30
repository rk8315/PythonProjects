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

#region Functions
def resource_check(menu_ingredients):
    for ingredient in menu_ingredients:
        if(menu_ingredients[ingredient] >= resources[ingredient]):
            print(f"Sorry, there is not enough {ingredient} for your order.")
            return False
    return True

def transaction_check(menu_item):
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    amount_tendered = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    if(amount_tendered >= MENU[menu_item]["cost"]):
        if(amount_tendered == MENU[menu_item]["cost"]):
            print(f"Here is your {MENU[menu_item]}!")
        else:
            change = round(amount_tendered - MENU[menu_item]["cost"], 2)
            print(f"Here is your {menu_item} and change of ${change}!")
    else:
        print("Sorry, that is not enough money. Refund issued.")
        return False
    return True

def resource_update(menu_item): 
    for ingredient in MENU[menu_item]["ingredients"]:
        resources[ingredient] -=  MENU[menu_item]["ingredients"][ingredient]

#endregion Functions

profit = 0

while True:
    user_selection = input("What would you like? (espresso/latte/cappuccino/report): ")
    if user_selection == "report":
        print(f"~ Water: {resources['water']}ml\n~ Milk: {resources['milk']}ml\n~ Coffee: {resources['coffee']}g\n~ Money: ${profit:.2f}")
    elif user_selection == "off":
        print("Turning off coffee machine")
        break
    elif user_selection == "espresso" or user_selection == "latte" or user_selection == "cappuccino":
        if resource_check(MENU[user_selection]["ingredients"]):
            if transaction_check(user_selection):
                resource_update(user_selection)
                profit += MENU[user_selection]["cost"]
    else:
        print("Invalid response.")
