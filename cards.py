import random

class Card:
    def __init__(self, suit, value, color):
        self.suit = suit
        self.value = value
        self.color = color

    def show(self):
        print(f"Suit: {self.suit}\nValue: {self.value}\nColor: {self.color}")
