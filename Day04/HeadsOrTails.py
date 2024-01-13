import random

response = input("heads or tails? > ")
rand = random.randint(0, 1)
res = None
print(rand)
if rand == 0:
    res = "heads"
    print("It was heads")
else:
    res = "tails"
    print("It was tails")

if res == response:
    print("You won!")
else:
    print("You lose :(")

