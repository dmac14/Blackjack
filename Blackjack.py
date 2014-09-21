"""
A rough program for one person to play blackjack
Thus far a deck and a hand can be initiated and cards can be dealt
"""

import random


class Deck():
    
    #On init creates lists from which cards will be created and a list to track
    #dealt cards.
    def __init__(self):
        self.cardNum=[]
        self.dealtCards=[]
        for num in range(1,14):
            self.cardNum.append(num)
        self.cardType=["Heart","Spade","Diamond","Club"]
        
    #Choses a number and type for the card to be dealt. Checks if it has already
    #been dealt (if yes, calls method again). If not, deals it and adds it to
    #list of dealt cards.
    def dealCard(self):
        self.randCardNum=random.randint(0,12)
        self.randCardType=random.randint(0,3)
        self.dealtCard=(str(self.cardNum[self.randCardNum]),self.cardType[self.randCardType],)
        for card in self.dealtCards:
            if self.dealtCard==card:
                print("match")
                return self.dealCard()
        self.dealtCards.append(self.dealtCard)
        return self.dealtCard

class PlayerHand():
    def __init__(self):
        self.heldCards=[]


myDeck=Deck()
myHand=PlayerHand()
myDeck.dealCard()



