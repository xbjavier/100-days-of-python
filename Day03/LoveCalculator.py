print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

full_names = (name1 + name2).lower();

ct = 0;
cl = 0;

for x in "true":
    for y in full_names:
        if x == y:
            ct += 1

for x in "love":
    for y in full_names:
        if x == y:
            cl += 1

score = int(f"{ct}{cl}")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")