'''
Created on 19-May-2019

@author: vsrir
'''

import random

class Card:
    '''
    This class holds the details of one playing card
    '''
    suits = ("Spades","Diamonds","Hearts","Clubs")
    values = ("Ace","Two","Three","Four","Five", \
              "Six","Seven","Eight","Nine","Ten", \
              "Jack", "Queen", "King")

    def __init__(self, suit, value):
        '''
        Constructor
        '''
        if suit not in Card.suits or value not in Card.values:
            raise ValueError
        self.suit = suit
        self.value = value    
    def __str__(self):
        return self.value + " of " + self.suit    

class EmptyDeck(Exception):
    pass

class Deck:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.cards = []
        for suit in Card.suits:
            for value in Card.values:
                self.cards.append(Card(suit, value))
    def display(self):
        for card in self.cards:
            print(card)
        print("Deck has {} cards".format(len(self.cards)))
    
    def shuffle(self):
        attempts = random.randint(1,10)
        while attempts > 0:
            for i in range(len(self.cards)):
                doshuffle = random.randint(0,1)
                if doshuffle == 1:
                    swapwith = random.randint(0,len(self.cards) - 1)
                    self.cards[i],self.cards[swapwith] = self.cards[swapwith],self.cards[i]
            attempts = attempts - 1
            
    def deal(self):
        try:
            return self.cards.pop(0)
        except IndexError:
            raise EmptyDeck

if __name__ == '__main__':
    newDeck = Deck()
    newDeck.shuffle()
    newDeck.display()
    print(newDeck.deal())           
    del newDeck