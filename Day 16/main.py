from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


end = False
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


def ask_user() -> str:

    return input("What would you like? (espresso/latte/cappuccino): ")

while end == False:
    choice = ask_user()

    if choice == "off":
        end = True

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        choice = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                coffee_maker.make_coffee(choice)
