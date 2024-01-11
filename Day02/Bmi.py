height = float(input("height? "))
weight = float(input("weight? "))

bmi = weight / (height**2)

msg = f"Your BMI is {bmi}"
if bmi < 18.5: 
    print(f"{msg}, you are underweight.")
elif bmi < 25:
    print(f"{msg}, you have a normal weight.")
elif bmi < 30:
    print(f"{msg}, you are slightly overweight.")
elif bmi < 35:
    print(f"{msg}, you are obese.")
else:
    print(f"{msg}, you are clinically obese.")