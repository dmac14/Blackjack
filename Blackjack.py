"""
A program for one person to play blackjack.

Version History:
1.0 A deck and a hand can be initiated and cards can be dealt
1.1 Cards are dealt to the player's hand and text to user added
1.11 Added version history, made card types plural,changed dealt card to list from tuple.
    Methods added:
       -PlayerHand.displayHand = displays the player's hand
       -PlayerHand.hit = adds another card to the player's hand
       -PlayerHand.calcHandTotal = calculates the player's current hand total (W.I.P.) 
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
    #been dealt (if yes, calls method again). If not, deals it to the player's hand
    #adds it to list of dealt cards, and calculates the player's total.
    def dealCard(self,_Hand):
        self.randCardNum=random.randint(0,12)
        self.randCardType=random.randint(0,3)
        self.dealtCard=[self.cardNum[self.randCardNum],self.cardType[self.randCardType]]
        #Checks to see if the card has already been dealt
        for card in self.dealtCards:
            if self.dealtCard==card:
                #if it has, deals a different card
                return self.dealCard(_Hand)
        #if not, adds card to dealt list, the player's hand, and calculates total
        self.dealtCards.append(self.dealtCard)
        _Hand.heldCards.append(self.dealtCard)
        _Hand.calcHandTotal(self.dealtCard)
        return self.dealtCard

class PlayerHand():

    def displayHand(self):
        print("In your hand you currently have: ")
        for card in self.heldCards:
            print(str(card[0])+" of "+card[1])

    #Method to take a hit (get another card from the dealer)
    def hit(self,_Deck):
        _Deck.dealCard(self)

    #Calculates the total of the cards in the player's hand
    def calcHandTotal(self,dealtCard):
        self.handTotal+=dealtCard[0]
        ### W.I.P. ###
        
    #On init creates a list for the player's hand
    def __init__(self):
        self.heldCards=[]
        self.handTotal=0

    



print("Welcome to our humble Blackjack table! Have a seat and we'll get you started :D")

#Create a Deck and PlayerHand objects
myDeck=Deck()
myHand=PlayerHand()

#Deal two cards to the player
print("Alright then, here are your first two cards.")
myDeck.dealCard(myHand)
myDeck.dealCard(myHand)
myHand.displayHand()



