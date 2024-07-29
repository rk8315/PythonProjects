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
#endregion Functions

while True:
    profit = 0
    initial_prompt = input("What would you like? (espresso/latte/cappuccino/report): ")
    if initial_prompt == "espresso":
        if(resources["coffee"] >= 18):
            if(resources['water'] >= 50):
                print("Please insert coins")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                amount_tendered = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

                if(amount_tendered >= MENU["espresso"]["cost"]):
                    if(amount_tendered == MENU["espresso"]["cost"]):
                        print("Here is your espresso!")
                    else:
                        change = round(amount_tendered - MENU["espresso"]["cost"], 2)
                        profit += MENU["espresso"]["cost"]
                        resources["coffee"] -= 18
                        resources["water"] -= 50
                        print(f"Here is your ${change} in change.")
                else:
                    print("Sorry, that is not enough money, money refunded.")
            else:
                print("Sorry, there is not enough water.")
        else:
            print("Sorry, there is not enough coffee.")
    elif initial_prompt == "latte":
        if resource_check(MENU["latte"]["ingredients"]):
            print("latte made")
    elif initial_prompt == "cappuccino":
        if(resources["coffee"] >= 24):
            if(resources["water" >= 250]):
                if(resources["milk"] >= 100):
                    print("cappuccino made")
                else:
                    print("Sorry, there is not enough milk.")
            else:
                print("Sorry, there is not enought water.")
        else:
            print("Sorry, there is not enough coffee.")
    elif initial_prompt == "report":
        print(f"~ Water: {resources['water']}\n~ Milk: {resources['milk']}\n~ Coffee: {resources['coffee']}\n~ Money: $2")
    elif initial_prompt == "off":
        print("turning off coffee machine")
        break
    else:
        print("Invalid statement")
