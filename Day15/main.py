from data import coins, flavours

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0.00
}


def check_enough_ingredients(coffe_selection):
    insuficient_resources = []
    ingredients = coffe_selection["ingredients"]

    if ingredients["water"] > resources["water"]:
        insuficient_resources.append("water")
    if ingredients["coffee"] > resources["coffee"]:
        insuficient_resources.append("coffee")
    if ingredients["milk"] > resources["milk"]:
        insuficient_resources.append("milk")

    return (',').join(insuficient_resources)

def prepare_coffee(coffe_selection):
    ingredients = coffe_selection["ingredients"]
    resources["water"] -= ingredients["water"]
    resources["coffee"] -= ingredients["coffee"]
    resources["milk"] -= ingredients["milk"]
    resources["money"] += coffe_selection["cost"]

def request_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters?\n>"))
    dimes = int(input("How many dimes?\n>"))
    nickles  = int(input("How many nickles?\n>"))
    pennies  = int(input("How many pennies?\n>"))

    total = (quarters * coins["quarter"]) + (dimes * coins["dime"]) + (nickles * coins["nickel"]) + (pennies * coins["penny"])
    return total

def show_report():
    print(f"water: {resources['water']:.2f} ml")
    print(f"coffee: {resources['coffee']:.2f} g")
    print(f"milk: {resources['milk']:.2f} ml")
    print(f"money: ${resources['money']:.2f}")

while(True):
    print("What option would you like")
    for i, f in enumerate(flavours):
        print(f"{i}. {f[0]}")

    selection = input("What option wolud you like? espresso/latte/cappuccino\n>").lower()
    if selection == "off":
        break

    if selection == "report":
        show_report()
        continue

    option_selection = int(selection)   
    if option_selection == 0 or option_selection > len(flavours):
        print("That's not a valid option, sorry")
        continue       

    flavour = flavours[option_selection][0]
    flavour_details = flavours[option_selection][1]
    insuficient_resources = check_enough_ingredients(flavour_details)

    if insuficient_resources:
        print(f"Sorry, we don't have enough {insuficient_resources}")
        continue

    # ask for coins
    total_received = request_coins()
    if total_received < flavour_details["cost"]:
        print(f"Sorry, that's not enough, received ${total_received:.2f} but coffee price is ${flavour_details["cost"]:.2f}\nTake your money please...")
        continue

    change = total_received - flavour_details["cost"]
    if change > 0:
        print(f"please collect your change: {change:.2f}")

    # prepare coffee a.k.a remove resources
    prepare_coffee(flavour_details)
    print(f"your {flavour} is ready, beware is hot... ☕️")



    



