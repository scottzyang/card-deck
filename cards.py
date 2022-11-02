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

    def shuffle(self):
        random.shuffle(self.cards)
        # for card in self.cards:
        #     print(card.value, card.suit, card.color)

    def draw(self):
        print(self.cards[0].suit, self.cards[0].value, self.cards[0].color)
        # print(self.cards[51].suit, self.cards[51].value, self.cards[51].color)
        self.cards.append(self.cards.pop(0))
        # print(self.cards[0].suit, self.cards[0].value, self.cards[0].color)
        # print(self.cards[51].suit, self.cards[51].value, self.cards[51].color)

newDeck = Deck()
newDeck.create_deck()
newDeck.shuffle()
newDeck.draw()
newDeck.draw()
newDeck.draw()