import os
from art import logo

print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}


history = []
while True:
    result = 0
    first =  float(input("What's the first number?\n> "))

    while True:
        sign = input("+\n-\n-\n*\n/\nPick an operation?\n> ")
        
        if sign not in operations:
           print("Operation is not valid, try again")
           continue

        second = float(input("What's the second number?\n> "))
        try:
            calc_function = operations[sign]
            result = calc_function(first, second)
            display = f"{first} {sign} {second} = {result}"
            print(display)
            history.append(display)
            first = result
        except ZeroDivisionError:
            result = first
            print("Can't divide by 0")

        continue_calculation = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation\n> ")
        if continue_calculation.lower() != 'y':
            os.system('cls')
            break
