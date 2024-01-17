import random

difficulties = {
    "easy": 10,
    "hard": 5
}



def get_number_of_guesses():
    while True:
        difficulty = input("Chose a difficulty, type: 'easy' or 'hard'\n> ")
        if difficulty not in difficulties:
            print("Invalud value, try again")
            continue
        return difficulties[difficulty]
    
def guess_number(to_guess: int, guess: int):
    if to_guess == guess:
        return True
    elif to_guess > guess:
        print("Number is higher")
        return False
    else:
        print("Number is lower")
        return False
    
def get_player_guess():
    while True:
        try:
            player_guess = int(input("Guess a number:\n> "))
            return player_guess
        except ValueError:
            print("Not a valid number, try again...")

def play_again(win: bool, number_to_guess: int):
    if win:
        print("You got it right!")   
    else:
        print(f"You lost, the number was: {number_to_guess}")

    return input("Play again? y/n\n> ").lower() == "y"
        


    
def  main_loop():
    while True:
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100") 
        number_to_guess = random.randint(1,100)
        number_of_guesses = get_number_of_guesses()
        win = False
        while number_of_guesses > 0:
            player_guess = get_player_guess()
            if not guess_number(number_to_guess, player_guess):
                if number_of_guesses - 1 > 0:
                    number_of_guesses -= 1
                    print(f"You still have {number_of_guesses} attempts, try again...")
                    continue
                else:
                    win = False
                    break
            else:
                win = True
                break
            
        if not play_again(win, number_to_guess):
            break

main_loop()







