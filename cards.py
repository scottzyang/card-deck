import random

class Card:
    def __init__(self, suit, value, color):
        self.suit = suit
        self.value = value
        self.color = color

    def show(self):
        print(f"Suit: {self.suit}\nValue: {self.value}\nColor: {self.color}")


class Deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        suits = ['hearts', 'diamonds', 'spades', 'clubs']

        for suit in suits:
            for i in range(1, 14):
                # print(i)
                if suit == 'hearts' or suit == 'diamonds':
                    temp = Card(suit, i, 'red')
                else: 
                    temp = Card(suit, i, 'black')
                self.cards.append(temp)
        
        # test to see if cards list was populated
        # for card in self.cards:
        #     print(card.value, card.suit, card.color)
                