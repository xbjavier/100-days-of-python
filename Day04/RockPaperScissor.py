import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

print("Rock, Paper, Scissors!")

while True:
    player = int(input("What do you choose? \n0 for Rock\n1 for paper\n2 for scissors\n>"))
    if player > 2:
        print("invalid option, try again")
        continue

    computer = random.randint(0,2)

    print(images[player])
    print(f"computer chose:\n{images[computer]}")

    if player == computer:
        print("it's a draw!")
    elif player == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and player == 2:
        print("You lose")
    elif computer > player:
        print("You lose")
    elif player > computer:
        print("You win!")

    play_again = input("Play again? Y/n > ")
    if not play_again.lower() == 'y':
        break