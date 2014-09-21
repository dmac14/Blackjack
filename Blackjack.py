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
    def dealCard(self,hand):
        self.randCardNum=random.randint(0,12)
        self.randCardType=random.randint(0,3)
        self.dealtCard=(str(self.cardNum[self.randCardNum]),self.cardType[self.randCardType],)
        for card in self.dealtCards:
            if self.dealtCard==card:
                print("match")
                return self.dealCard(hand)
        self.dealtCards.append(self.dealtCard)
        hand.heldCards.append(self.dealtCard)
        return self.dealtCard

class PlayerHand():
    def __init__(self):
        self.heldCards=[]


print("Welcome to our humble Blackjack table! Have a seat and we'll get you started :D")

#Create a Deck and PlayerHand objects
myDeck=Deck()
myHand=PlayerHand()

#Deal two cards to the player
print("Alright then, here are your first two cards.")
myDeck.dealCard(myHand)
myDeck.dealCard(myHand)
for card in myHand.heldCards:
    print(card[0]+" of "+card[1])



