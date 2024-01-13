target = int(input("max number? > "))

for i in range(target + 1):
    fizzbuzz = ""
    if i % 3 == 0:
        fizzbuzz = "Fizz"
    if i % 5 == 0:
        fizzbuzz += "Buzz"

    if fizzbuzz:
        print(fizzbuzz)
    else:
        print(i)