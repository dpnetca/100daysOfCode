from menu import Menu  # , MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cofee_maker = CoffeeMaker()
money_machine = MoneyMachine()

item_list = menu.get_items().split("/")

# remove empty items
while "" in item_list:
    item_list.remove("")

menu_options = ["report", "off"]
menu_options.extend(item_list)
machine_is_on = True

while machine_is_on:
    choice = input(f"What would you like? ({'/'.join(item_list)}): ").lower()
    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        cofee_maker.report()
        money_machine.report()
    elif choice in item_list:
        drink = menu.find_drink(choice)
        if cofee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                cofee_maker.make_coffee(drink)
                money_machine.money_received = 0
    else:
        print("invalid selection")
