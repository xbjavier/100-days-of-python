from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

table = PrettyTable()
table.field_names = ["Coffee", "Cost"]

for item in menu.get_items().split("/"):
    data = menu.find_drink(item)
    if data:
        table.add_row([f"{data.name}", f"${data.cost:.2f}"])

while True:
    selection = input(f"Select your coffee\n{table}\n>").lower()

    if selection == "off":
        break

    if selection == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    coffee = menu.find_drink(selection)
    if coffee == None:
        continue

    if not coffee_maker.is_resource_sufficient(coffee):
        continue

    if money_machine.make_payment(coffee.cost):
        coffee_maker.make_coffee(coffee)
