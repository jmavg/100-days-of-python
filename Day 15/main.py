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

VALUE = {"quarters": 0.25,
"dimes": 0.10,
"nickles": 0.05,
"pennies": 0.01
}

nb_coins = {"quarters": 0,
"dimes": 0,
"nickles": 0,
"pennies": 0
}

end = False


def ask_user() -> str:

    return input("What would you like? (espresso/latte/cappuccino): ")

def check_resources(option) -> str:

    ingredients = option["ingredients"]

    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            return(ingredient)

        else:
            return("")

def calc_money() -> float:
    global nb_coins
    total = 0

    for coin in nb_coins:
        total += nb_coins[coin]*VALUE[coin]

    return total



while end == False:
    choice = ask_user()

    if choice == "off":
        end = True

    elif choice == "report":
        print(resources)

    else:
        choice = MENU[choice]

        if check_resources(choice) != "":
            print(f"Sorry, there's not enough {check_resources(choice)}")

        else:
            print("Insert coins:")

            for coin in nb_coins:
                nb_coins[coin] = int(input(f"How many {coin}? "))

            money = calc_money()
            cost = choice["cost"]

            if money >= cost:
                if "Money" not in resources.keys():
                    resources["Money"] = cost
                else:
                    resources["Money"] += cost

                print(F"Here's your change: {round((money - cost),3)}")

                for ingredient in choice["ingredients"]:
                    resources[ingredient] -= choice["ingredients"][ingredient]

                print("Here's your drink ")
            else:
                print("You don't have enough money u poor fuck")
