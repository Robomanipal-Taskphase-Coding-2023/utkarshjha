import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        self.cards = [Card(value, suit) for value in values for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def check_pair(self, card1, card2):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        # Check if the values are consecutive or cyclic
        index1 = values.index(card1.value)
        index2 = values.index(card2.value)

        return abs(index1 - index2) == 1 or abs(index1 - index2) == len(values) - 1
