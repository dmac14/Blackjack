"""
A program for one person to play blackjack.

Version History:
1.0 A deck and a hand can be initiated and cards can be dealt
1.1 Cards are dealt to the player's hand and text to user added
1.11 Added version history, made card types plural,changed dealt card to list from tuple
    Methods added:
       -PlayerHand.displayHand = displays the player's hand
       -PlayerHand.hit = adds another card to the player's hand
       -PlayerHand.calcHandTotal = calculates the player's current hand total
1.13  Removed 11,12,13 and replaced with 10's
      Methods added:
       -PlayerHand.userAction=gets and executes user's action of choice: Get another card,
                             switch an ace value, or stay with current hand.
       -PlayerHand.switchAce=switches the ace value between 1 and 11
       -PlayerHand.winOrLose=method to determine end game comment
"""

import random


class Deck():
    
    #On init creates lists from which cards will be created and a list to track
    #dealt cards.
    def __init__(self):
        self.cardNum=["Ace"]
        self.dealtCards=[]
        for num in range(2,11):
            self.cardNum.append(num)
        #for loop for Jack, Queen, and King values (three 10's)
        for i in range (3):
            self.cardNum.append(10)
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
        if self.dealtCard[0]=="Ace":
            print("Your Ace is current valued at 1. You may switch it at your convenience")
            self.dealtCard[0]=1
            _Hand.hasAce=1
        self.dealtCards.append(self.dealtCard)
        _Hand.heldCards.append(self.dealtCard)
        _Hand.calcHandTotal(self.dealtCard)
        return self.dealtCard

    #Lets the user choose what they want to do
    def userAction(self,_Hand):
        #Get users choice and make sure its an integer
        try:
            userChoice=int(input("What would you like to do? "))
        except ValueError:
            print("Ruh-roh, that didn't seem to be a valid number. Pls try again :)")
            self.userAction(_Hand)
        #Perform associated action
        #Deal another card
        if userChoice==1:
            self.dealCard(_Hand)
            _Hand.displayHand()
        #Switch ace value
        elif userChoice==2:
            if _Hand.hasAce==1:
                _Hand.switchAce(_Hand.flag)
        #Stay
        elif userChoice==3:
            _Hand.stay=1
        #Choice was an integer but not one of the given options
        else:
            print("Ruh-roh, bad choice bud. Try again...")
            self.userAction(_Hand)

class PlayerHand():

    def displayHand(self):
        print("\nIn your hand you currently have: ")
        for card in self.heldCards:
            print(str(card[0])+" of "+card[1])
        print("Your current total is: "+str(self.handTotal))

    #Determines end of the game peanut gallery comment
    def winOrLose(self):
        if self.handTotal>21:
            print("Whoops Icarus, you went to high :(")
        elif self.handTotal<21:
            print("Hey, nice work, you stayed under 21.")
        else:
            print("WOW YOU NAILED IT MAN! :D:D:D:D")
        

    #Method to take a hit (get another card from the dealer)
    def hit(self,_Deck):
        _Deck.dealCard(self)

    def switchAce(self,flag):
        #Depending on current Ace value, switches between 1 and 11
        if flag==0:
            self.handTotal+=10
            self.flag=1
        else:
            self.handTotal-=10
            self.flag=0
        ######### WORK IN PROGRESS   ##########
        

    #Calculates the total of the cards in the player's hand
    def calcHandTotal(self,dealtCard):
        self.handTotal+=dealtCard[0]
        
        
    #On init creates a list for the player's hand
    def __init__(self):
        self.heldCards=[]
        self.handTotal=0
        self.stay=0
        self.hasAce=0
        self.flag=0

    



print("Welcome to our humble Blackjack table! Have a seat and we'll get you started :D")

#Create a Deck and PlayerHand objects
myDeck=Deck()
myHand=PlayerHand()

#Deal two cards to the player
print("Alright then, here are your first two cards.")
myDeck.dealCard(myHand)
myDeck.dealCard(myHand)
myHand.displayHand()
while(myHand.handTotal<21 and myHand.stay==0):
    print("\n1: Get another card")
    print("2: Switch an ace value")
    print("3: Stay with what you have")
    myDeck.userAction(myHand)
print("Alright buddy, that's it! Your total comes to:")
print(myHand.handTotal)
myHand.winOrLose()




