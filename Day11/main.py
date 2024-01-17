import random
from art import logo
from cards import card, get_cards_list

deck = get_cards_list()

print(logo)

def deal_card():
    rand = random.randint(0, len(deck) - 1)
    card = deck.pop(rand)
    return card

def sum_cards(cards: [card]):
    sum = 0
    aces = []
    for c in cards:
        if c.symbol == 'A':
            aces.append(c)
        else:
            sum += c.values[0]

    for ace in aces:
        if sum + ace.values[1] > 21:
            sum += ace.values[0]
        else:
            sum += ace.values[1]

    return sum
    
def print_computer_cards(show_all: False, computer_cards):
    if show_all:
        print(f"Computer cards: [{', '.join(map(lambda card: card.symbol, computer_cards))}]")
    else:
        print(f"Computer's first card: {computer_cards[0].symbol}")

def print_player_cards(player_cards):
    print(f"Your cards: [{', '.join(map(lambda card: card.symbol, player_cards))}]")

def check_results_and_continue(player_sum: int, computer_sum: int, early_result: False):
    should_ask_to_continue_playing = False
    if early_result:
        if player_sum == 21 and computer_sum == 21:
            print("It's a draw")
            should_ask_to_continue_playing = True
        elif player_sum == 21:
            print("You won!")
            should_ask_to_continue_playing = True
    else:
        if computer_sum > 21 or computer_sum < player_sum:
            print("You won!")
            should_ask_to_continue_playing = True
        elif computer_sum == player_sum:
            print("It's a draw")
            should_ask_to_continue_playing = True
        else:
            print("You lost")
            should_ask_to_continue_playing = True

    if should_ask_to_continue_playing:
        want_continue = input("Cotinue? y/N\n >")
        if want_continue.lower() != "y":
            return False
        
    return True

    

while True:

    player_cards = []
    computer_cards = [] 
    game_over = False

    if deck == None or len(deck) < 4:
        deck = get_cards_list()

    player_cards.append(deal_card())
    player_cards.append(deal_card())
    player_sum = sum_cards(player_cards)

    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_sum = sum_cards(computer_cards)

    print_player_cards(player_cards)
    print_computer_cards(False, computer_cards)

    if not check_results_and_continue(player_sum, computer_sum, early_result=True):
       break

    while len(deck) > 0:
        get_another_card = input("Type 'y' to get another card\n>")
        if get_another_card.lower() == "y":
            player_cards.append(deal_card())
            player_sum = sum_cards(player_cards)
            print_player_cards(player_cards)
            if(player_sum > 21):
                print(f"Bust, sum: {player_sum}")
                print_computer_cards(True, computer_cards)
                game_over = True
                break
            continue
        break

    if game_over:
        want_continue = input("Cotinue? y/N\n >")
        if want_continue.lower() != "y":
            break
        else:
            continue

    print_computer_cards(True, computer_cards)

    while computer_sum < 16:
        computer_cards.append(deal_card())
        computer_sum = sum_cards(computer_cards)
        print_computer_cards(True, computer_cards)
        

    if not check_results_and_continue(player_sum, computer_sum, early_result=False):
        break