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
1.2 Re-ordering structure:
       -Added GameState class to control game flow
       -Moved all (except __init__ of course) methods from Deck to PlayerHand class
       -PlayerHand now accepts Deck as a property (??? should I inherit???)

1.21 Added Dealer Class and updated game loop to include a dealer
"""

import random


class Deck():
    
    #On init creates lists from which cards will be created and a list to track
    #dealt cards.
    def __init__(self):
        self.cardNum=[]
        self.dealtCards=[]
        for num in range(1,11):
            self.cardNum.append(num)
        #for loop for Jack, Queen, and King values (three 10's)
        for i in range (3):
            self.cardNum.append(10)
        self.cardType=["Hearts","Spades","Diamonds","Clubs"]
        
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        

class PlayerHand():

    def displayHand(self):
        print("\nIn your hand you currently have: ")
        for card in self.heldCards:
            print("\t"+str(card[0] if card[0]!=1 else "Ace ({})".format(1 if self.flag==0 else 11))+" of "+card[1])
        print("Your current total is: "+str(self.handTotal))
        if self.hasAce==1:
            print("You may switch it at your convenience.")
   
    #Choses a number and type for the card to be dealt. Checks if it has already
    #been dealt (if yes, calls method again). If not, deals it to the player's hand
    #adds it to list of dealt cards, and calculates the player's total.
    def hit(self):
        self.randCardNum=random.randint(0,12)
        self.randCardType=random.randint(0,3)
        self.dealtCard=[self.Deck.cardNum[self.randCardNum],self.Deck.cardType[self.randCardType]]
        #Checks to see if the card has already been dealt
        for card in self.Deck.dealtCards:
            if self.dealtCard==card:
                #if it has, deals a different card
                return self.hit()
        #if not, adds card to dealt list, the player's hand, and calculates total
        if self.dealtCard[0]==1:
            self.hasAce=1
        self.Deck.dealtCards.append(self.dealtCard)
        self.heldCards.append(self.dealtCard)
        self.calcHandTotal(self.dealtCard)
        return self.dealtCard

    def startHand(self):
        self.hit()
        self.hit()
        self.displayHand()

    def switchAce(self,flag):
        #Depending on current Ace value, switches between 1 and 11
        if flag==0:
            self.handTotal+=10
            self.flag=1
        else:
            self.handTotal-=10
            self.flag=0

    #Calculates the total of the cards in the player's hand
    def calcHandTotal(self,dealtCard):
        self.handTotal+=dealtCard[0]

    #Lets the user choose what they want to do
    def userAction(self):
        print("\n1: Get another card")
        print("2: Switch an ace's value")
        print("3: Stay with what you have")
        #Get users choice and make sure its an integer
        try:
            userChoice=int(input("What would you like to do?  "))
        except ValueError:
            print("Ruh-roh, that didn't seem to be a valid number. Pls try again :)")
            self.userAction()
        #Perform associated actions...
        #Deal another card
        if userChoice==1:
            self.hit()
            self.displayHand()
        #Switch ace value
        elif userChoice==2:
            if self.hasAce==1:    #check to see if they have an ace to switch
                if self.handTotal<12:      #check to see if switching their ace would put them over
                    self.switchAce(self.flag)
                    self.displayHand()
                else:
                    print("Switching your ace would put you over... not a smart decision")
            else:
                print("You don't have an ace to switch... nice try guy")
        #Stay
        elif userChoice==3:
            self.stay=1
        #Choice was an integer but not one of the given options
        else:
            print("Ruh-roh, bad choice bud. Try again...")
            self.userAction()
        
        
    #On init creates a list for the player's hand
    def __init__(self, _deck,_handNum):
        self.heldCards=[]
        self.handTotal=0
        self.stay=0
        self.hasAce=0
        self.flag=0
        self.Deck=_deck
        self.handNum=_handNum+1
        

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class dealerHand(PlayerHand):

    #Display one of the dealer's first two cards
    def displayHand(self):
        print("\nThe dealer's hand is showing:")
        print("\t"+str(self.heldCards[0][0] if self.heldCards[0][0]!=1 else "Ace (?)")+" of "+self.heldCards[0][1])

    #Dealer plays out his hand till 17+ 
    def playOut(self):
        if self.hasAce==1:              #if one of first 2 cards is an ace, switch it to 11
            self.switchAce(self.flag)
        while self.handTotal<17:        #keep taking cards till total>=17
            self.hit()
            if self.hasAce==1 and self.startAce==0 and self.handTotal<12:     #if new card is an ace, switch it if possible
                self.switchAce(self.flag)
                self.StartAce=1
            if self.handTotal>21 and self.hasAce==1 and self.flag==1:
                self.switchAce(self.flag)
        
    def __init__(self,_deck):
        PlayerHand.__init__(self,_deck,0)
        self.startHand()
        self.startAce= 1 if self.hasAce==1 else 0        #Flag for if the dealer gets an ace in his first 2 cards
        self.playOut()
        

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        

#Class to manage the state of the game
class GameState():

    #Asks the user how many players will be playing
    def howManyPlayers(self):
        try:
            numPlayers=int(input("How many players are there going to be?"))
        except ValueError:
            print("Not a valid input")
            self.howManyPlayers()
        return numPlayers

    #Creates a list containing the hands of the players
    def createHands(self,numPlayers,myDeck):
        handList=[PlayerHand(myDeck,i) for i in range(numPlayers)]
        return handList

    #Loops through each hand and lets the player play until they stay or are over 21
    def GameLoop(self,myDeck,handList):
        for hand in handList:
            print("\n\t"+("~"*60))
            print("\nAlright Player {}, here are your first two cards.".format(hand.handNum))
            hand.startHand()
            while(hand.handTotal<21 and hand.stay==0):
                hand.userAction()
            if hand.handTotal>21:
                print("Sorry Player {}, you went over :(\n".format(hand.handNum))

    #Once all hands are done, shows totals and checks if they want to play again
    def EndGame(self):
         print("\n\t"+("~"*60))
         print("\nThat's all folks! The totals come to:\n")
         print("Dealer's final total: {}\n".format(self.dealerHand.handTotal if self.dealerHand.handTotal<22 else "BUST"))
         for hand in self.handList:
            print("Player {}'s total was: {}".format(hand.handNum,hand.handTotal if hand.handTotal<22 else "BUST"))
         playAgain=input("\nWould you like to play again? (Y/N)").upper()
         if playAgain=="Y":
             print("\n"+("#"*30)+" NEW GAME "+("#"*30)+"\n")
             return playAgain
                                  
    def __init__(self):
        self.myDeck=Deck()
        self.numPlayers=self.howManyPlayers()
        self.dealerHand=dealerHand(self.myDeck)
        self.handList=self.createHands(self.numPlayers,self.myDeck)
        self.GameLoop(self.myDeck,self.handList)
        self.playAgain=self.EndGame()
        
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


print("Welcome to our humble Blackjack table! Have a seat and we'll get you started :D")

#Create a GameState object
playAGame=GameState()
while playAGame.playAgain=="Y":
    playAGame=GameState()
print("\nThanks for playing :D")




