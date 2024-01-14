import os
from art import logo

bids = {}
bigger_bid = {
    "name": None,
    "amount": 0
}

while True:
    os.system('cls')
    print(logo)
    print("Welcome to the secret auction program.")
    name = input("What is your name?\n> ")
    bid = float(input("What's your bid?\n> $"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Y/n\n> ")

    if(bid > bigger_bid["amount"]):
        bigger_bid["name"] = name
        bigger_bid["amount"] = bid

    if more_bidders.lower() != 'y':
        break

print(f"The winner is {bigger_bid['name']} with a bid of ${ bigger_bid['amount']:.2f}")

