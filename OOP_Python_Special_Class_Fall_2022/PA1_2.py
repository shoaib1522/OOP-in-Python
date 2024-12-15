from random import *
class PlayingCard:
    def get_value_string(value):
        if value == 1:  return 'ace';
        elif value == 2:  return 'two';
        elif value == 3:  return 'three';
        elif value == 4:  return 'four';
        elif value == 5:  return 'five';
        elif value == 6:  return 'six';
        elif value == 7:  return 'seven';
        elif value == 8:  return 'eight';
        elif value == 9:  return 'nine';
        elif value == 10:  return 'ten';
        elif value == 11:  return 'jack';
        elif value == 12:  return 'queen';
        elif value == 13:  return 'king';
        
    def get_suit_string(suit):
        if suit == 1:  return 'heart';
        elif suit == 2:  return 'diamond';
        elif suit == 3:  return 'spade';
        elif suit == 4:  return 'club';

    def __init__(self, value, suit):
        self.value = value
        self.value_string = PlayingCard.get_value_string(value)
        self.suit = suit
        self.suit_string = PlayingCard.get_suit_string(suit)

    def __str__(self):
        return f'Value: {self.value}\tSuit: {self.suit}\t {self.value_string} of {self.suit_string}\n'

class Hand:
    def is_exist(cards, value, suit):
        for i in range(len(cards)):
            if cards[i].value == value and cards[i].suit == suit:
                return True
        return False
    
    def __init__(self):
        self.cards = []
        i = 0
        while i < 5:
            value = randint(1, 13)
            suit = randint(1, 4)
            if Hand.is_exist(self.cards, value, suit) == False:
                self.cards.append(PlayingCard(value, suit))
                i += 1
                
    def __str__(self):
        s = ''
        for card in self.cards:
            s += str(card)
        return s

    
def main():
    hand = Hand()
    print(hand)

main()
