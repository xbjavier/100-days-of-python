import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o' 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password?\n>"))
numbers = int(input("How many numbers would you like?\n>"))
symbols = int(input("How many symbols would you like?\n>"))

password = ""

for i in range(0, letters):
  password += random.choice(alphabet) 

for i in range(0, numbers):
    password += str(random.randint(0, 9))

for i in range(0, symbols):
    password += random.choice(symbol)

# shuffle the password
password = ''.join(random.sample(password, len(password)))

print(password)