"""
A program for one person to play blackjack.

Version History:
1.0 A deck and a hand can be initiated and cards can be dealt
1.1 Cards are dealt to the player's hand and text to user added
1.11 Added version history, made card types plural,changed dealt card to list from tuple.
    Methods added:
       -PlayerHand.displayHand = displays the player's hand
       -PlayerHand.hit = adds another card to the player's hand
       -PlayerHand.calcHandTotal = calculates the player's current total (UNDER CONSTRUCTION)
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
        self.cardType=["Hearts","Spades","Diamonds","Clubs"]
        
    #Choses a number and type for the card to be dealt. Checks if it has already
    #been dealt (if yes, calls method again). If not, deals it and adds it to
    #list of dealt cards.
    def dealCard(self,_Hand):
        self.randCardNum=random.randint(0,12)
        self.randCardType=random.randint(0,3)
        self.dealtCard=[str(self.cardNum[self.randCardNum]),self.cardType[self.randCardType]]
        for card in self.dealtCards:
            if self.dealtCard==card:
                print("match")
                return self.dealCard(_Hand)
        self.dealtCards.append(self.dealtCard)
        _Hand.heldCards.append(self.dealtCard)
        return self.dealtCard

class PlayerHand():

    #On init creates a list for the player's hand
    def __init__(self):
        self.heldCards=[]

    def displayHand(self):
        for card in self.heldCards:
            print(card[0]+" of "+card[1])

    #Method to take a hit (get another card from the dealer)
    def hit(self,_Deck):
        _Deck.dealCard(self)

    def calcHandTotal(self):
        # UNDER CONSTRUCTION
        pass

    



print("Welcome to our humble Blackjack table! Have a seat and we'll get you started :D")

#Create a Deck and PlayerHand objects
myDeck=Deck()
myHand=PlayerHand()

#Deal two cards to the player
print("Alright then, here are your first two cards.")
myDeck.dealCard(myHand)
myDeck.dealCard(myHand)
myHand.displayHand()



