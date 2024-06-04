base_path = "Day24/Input"

with open(f"{base_path}/Names/invited_names.txt") as invited_names:
    global names
    names = invited_names.readlines()

with open(f"{base_path}/Letters/starting_letter.txt", mode="r") as letter:
    original = letter.read()
    for name in names:
        name = name.replace('\n', '')
        temp = original.replace("[name]", name.strip())
        with open(f"Day24/Output/ReadyToSend/letter_to_{name}.txt", mode="w") as new_letter:
            new_letter.write(temp)
