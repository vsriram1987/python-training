'''
Created on 19-May-2019

@author: vsrir
'''
from deckofcards import Deck, Card, EmptyDeck
import time

class NoBalance(Exception):
    pass

class Participant:
    def __init__(self, playertype, chips):
        self.playertype = playertype
        self.chips = chips
        self.cards = []
        self.points = 0
        
    def addchips(self, chips):
        self.chips = self.chips + chips
    
    def addcard(self, card):
        self.cards.append(card)
        
    def count(self):
        cardpoints = (1,2,3,4,5,6,7,8,9,10,10,10,10)
        hasace = False
        self.points = 0
        for card in self.cards:
            self.points = self.points + cardpoints[Card.values.index(card.value)]
            if card.value == "Ace" and hasace == False:
                hasace = True
        print(self.playertype + ":" + str(self.points))
        return hasace
    
    def showcards(self):
        print(self.playertype + ":")
        for card in self.cards:
            print(card)
    
    def addextrapoints(self):
        if self.points + 9 <= 21:
                self.points  = self.points + 9

class Dealer(Participant):
    def __init__(self):
        Participant.__init__(self, "Dealer", 0)
        self.cards = []
        self.deck = Deck()
        self.deck.shuffle()
        
    def dealcard(self):
        return self.deck.deal()
    
    def showcards(self):
        print(self.playertype + ":")
        for card in self.cards:
            if self.cards.index(card) != 1:
                print(card)
            else:
                print("Hidden")
    
    def endofgame(self):
        Participant.showcards(self)

class Player(Participant):
    def __init__(self, name, chips, bet):
        Participant.__init__(self, "Player", chips)
        self.cards = []
        self.name = name
        self.bet = bet
        
    def removechips(self, bet):
        if self.chips - bet < 0:
            raise NoBalance
        else:
            self.chips = self.chips - bet
            
    def count(self):
        if Participant.count(self) == True:
            Participant.addextrapoints()
            
    def endofgame(self):
        Participant.showcards(self)
        print("Total balance is: {}".format(player.chips))
        
if __name__ == '__main__':
    print("Welcome to black jack!")
    playername = input("What is your name?: ")
    while True:
        try:
            playerchips = int(input("How many chips do you have?: "))
            break
        except ValueError:
            print("Please enter a number!")
    while True:
        try:
            bet = int(input("What is your starting bet?: "))
            break
        except ValueError:
            print("Please enter a number!")
    player = Player(playername, playerchips, bet)
    player.removechips(bet)
    totalbet = bet
    dealer = Dealer()
    player.addcard(dealer.dealcard())
    player.addcard(dealer.dealcard())
    dealer.addcard(dealer.dealcard())
    dealer.addcard(dealer.dealcard())
    currentParticipant = player
    while True:
        dealer.showcards()
        player.showcards()
        if type(currentParticipant) == type(player):
            while True:
                action = input("Do you want to hit again and raise your bet or stay? Type h/s: ")
                if action.upper() == "H" or action.upper() == "S":
                    break
        else:
            action = "H"
            time.sleep(1)
        if action.upper() == "H":
            if type(currentParticipant) == type(player):
                bet = bet * 2
                print("Bet raised to {}".format(bet))
                try:
                    currentParticipant.removechips(bet)
                except NoBalance:
                    print("Sorry, no balance!")
                    currentParticipant = dealer
                totalbet = totalbet + bet
            try:
                currentParticipant.addcard(dealer.dealcard())
            except EmptyDeck:
                print("Deck is empty.")
                break
        else:
            currentParticipant = dealer
        player.count()
        dealer.count()
        if player.points >= 21 or dealer.points >= 17 or (dealer.points > player.points and type(currentParticipant) == type(dealer)):
            break
    if player.points > 21 or dealer.points > player.points:
        print("You lost")
    else:
        print("You won")
        player.addchips(totalbet * 2)
    dealer.endofgame()
    player.endofgame()
        