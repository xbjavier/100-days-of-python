import random

from hangman_art import logo, stages
from hangman_words import word_list

stages_len = len(stages) - 1

while True:
    print(logo)
    random_word = word_list[random.randint(0, len(word_list) - 1)]
    display_word = list('_'*len(random_word))
    played_letters = []
    print(f"The random word has {len(random_word)} letters")
    game_over = False
    current_guess = 0
    while not game_over:
        print(stages[stages_len - current_guess])
        guess = input("Guess a letter from the word\n> ")

        if guess in played_letters:
            print(f"You have already played letter '{guess}', try another one")
            input("Press any key to try again...")
            continue

        played_letters.append(guess)
        if guess in random_word:
            for i, c in enumerate(random_word):
                if c == guess:
                    display_word[i] = guess
            print(' '.join(map(str, display_word)))
        else:
            current_guess += 1
            print(stages[stages_len - current_guess])

        if not '_' in display_word:
            print("You won!")
            game_over = True
        
        if (current_guess) == stages_len:
            game_over = True
            print(f"You lost, the word is: {random_word}")
    
    play_again = input("Play again? y/N\n> ").lower()
    if play_again != 'y':
        break
    
