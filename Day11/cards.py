class card:
    def __init__(self, symbol, values):
        self.symbol = symbol
        self.values = values


cards = {
    "A": [1,11],
    "1": [1],
    "2": [2],
    "3": [3],
    "4": [4],
    "5": [5],
    "6": [6],
    "7": [7],
    "8": [8],
    "9": [9],
    "10": [10],
    "J": [10],
    "Q": [10],
    "K": [10]
}

def get_cards_list() -> [card]:
    cards_list = []
    for symbol in cards:
        for i in range(0,4):
            cards_list.append(card(symbol, cards[symbol]))
    return cards_list