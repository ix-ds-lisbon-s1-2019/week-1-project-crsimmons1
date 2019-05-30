# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:34:44 2019

@author: Caroline
"""

"""
Needs to be written on a file named poker_game.py
The game can be played by running python poker_game.py NUMBER_OF_PLAYERS
The script accepts an argument number_of_players which is a number indicating the number of players.
For each player the script will ask the name (using input() function).
The script will deal 5 cards to each player (you can use random.choice to select at random from a list). The different cards, sorted from lowest to highest are 2,3,4,5,6,7,8,9,10,J,Q,K,A. There are four suits, clubs, spades, hearts, diamonds. 
The script will print out each one of the players' hand, find out which one of the players have a winning hand and will print out the name of the winner
For the winning rules, there are two possible implementations:
Easy version, where we just compare the hands and the hand with the highest cards wins. For example, if Player 1 has the hand 2,3,K,Q,7 and Player 2 has the hand 8,10, ACE,J,2 Player 2 would win because 1 ACE beats a K. If Player 1 has the hand 2,3,K,Q,7, and Player 2 has the hand J,J,K,7,3 then Player 1 would win (since K,Q beats K,J).
Hard version, where we implement the different poker hands taking the suits into account (flush, poker, straight, etc).

hint: You can use the __gt__ , __lt__ or __eq__ methods on a class to implement comparisons (greater than, less than).
Finally, we will create a repository on github called poker_game, upload the poker_game.py file and a README.md file explaining what the game does. Then we will link the repository on the blog post.
"""
#%%
import sys
import random
#from random import shuffle

#%%
#here we use int() to convert the string input into an integer
NUMBER_OF_PLAYERS = int(sys.argv[1])
#print(NUMBER_OF_PLAYERS) 

# Start with a list containing no names.
names = []

# Ask the user for a name.
for i in range(NUMBER_OF_PLAYERS):
    new_name = input("Please enter the player name ")
    # Add the new name to our list.
    names.append(new_name)

# Show that the name has been added to the list.
print(names)
        
#%%

def Ranks(): return ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" ]
def Suits(): return [ "Clubs", "Diamonds", "Hearts", "Spades" ]
def Values(): return [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#%%
class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.rank + " of " + self.suit

#%%

class Deck:
    def __init__(self, rank, suit, value, deck):
        self.rank = rank
        self.suit = suit
        self.value = value
        self.deck = []
        self.deck = [ Card(rank, suit, value) for rank in Ranks() for suit in Suits() for value in Values() ]
        random.shuffle(self.deck)
    
    def __str__(self):
        return self.rank + " of " + self.suit
    
    def dealhand():
        return random.sample(Deck.deck, 5)
    
#%%
" Generate a list of player hands"

name_deck = []

for i in range(NUMBER_OF_PLAYERS):
    #Create a deck for i player
    name_deck = Deck.dealhand()
    #add the decks to a list 
    name_deck.append = (name_deck)
    #Return the deck as Rank of Suit
    def __str__(self):
        return name_deck

#%%
"Sort and print the hands of each player"

for names in NUMBER_OF_PLAYERS:
    #sort deck in acending order by value"
    name_deck.sort(Deck.value)
    #print each player's hand
    print("{}'s hand is {}".format(names, Deck.name_deck))

#%%
"Rate the poker hands"
 

#%%
"Print the Winner's Name" 


#list(deck1)