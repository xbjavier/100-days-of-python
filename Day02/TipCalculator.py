print("Welcome to the tip calculator")
total_bill = input("What was the total bill?\n")
tip = input("What percentage tip would you like to give?\n")
total_persons = input("how many people will participate?\n")

tip = float(tip)/100
tip_amount = float(total_bill) * tip;
total_per_person = (float(total_bill) + tip_amount)/float(total_persons)

print(f"Each person should pay {"{:.2f}".format(total_per_person)}")