import random
import os
from art import logo, vs
from game_data import data


score = 0
local_data = data.copy();

def random_data():
    return local_data.pop(random.randint(0, len(local_data) - 1))

def print_data(data_a, data_b):
    print(f"Compare A: {data_a["name"]}, a {data_a["description"]}, from {data_a["country"]}")
    print(vs)
    print(f"Compare B: {data_b["name"]}, a {data_b["description"]}, from {data_b["country"]}")

def get_right_answer(data_a, data_b):
    if(data_a["follower_count"] > data_b["follower_count"]):
        return 'a'
    return 'b'

compare_a = random_data()
compare_b = random_data()

while True:
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")

    print_data(compare_a, compare_b)

    correct_answer = get_right_answer(compare_a, compare_b) 
    answer = input("Who has more followers? Type 'a' or 'b'\n> ")
    if answer.lower() == correct_answer:
        score += 1
        os.system('cls')
        compare_a = compare_b
        compare_b = random_data()
    else:
        print(f"Wrong, your score is: {score}")
        score = 0
        continue_playing = input("Do you wish to continue playing? y/n\n> ")
        if continue_playing.lower() != 'y':
            break
