# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:34:44 2019

@author: Caroline
"""


#%%

""" Import modules """

import sys
import random

#%%
""" Ask for player names  """

#here we use int() to convert the string input into an integer
NUMBER_OF_PLAYERS = int(sys.argv[1])

# Start with a list containing no names.
names = []

# Ask the user for a name.
for i in range(NUMBER_OF_PLAYERS):
    new_name = input("Please enter the player name: ")
    # Add the new name to our list.
    names.append(new_name)

        
#%%
""" Create lists and dictionary for ranks, suits, and values """

#list of rank, suit, values of each card
Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" ]
Values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#multiply each list by 4 to create a deck 
rank = Rank * 4
values = Values *4

#create two dictionaries : one with values as the key, the other with rank as the key 
dic_VR= {k:v for k,v in zip(values, rank)}
dic_RV= {k:v for k,v in zip(rank, values)}
#%%
"""take a random sample (without replacement) of the deck """

dealt_cards = random.sample(rank, 35) 

#%%
""" Deal hands"""

hand1 = dealt_cards[0:5]
hand2 = dealt_cards[5:10]
hand3 = dealt_cards[10:15]
hand4 = dealt_cards[15:20]
hand5 = dealt_cards[20:25]
hand6 = dealt_cards[25:30]
hand7 = dealt_cards[30:35]

#%%
""" Print each hand"""

while 1:
    try:
        if NUMBER_OF_PLAYERS <= 1:
            print("Sorry! You need at least two player's to play poker")
            break
        elif NUMBER_OF_PLAYERS == 2:
            print("{}'s hand is {}".format(names[0],hand1))
            print("{}'s hand is {}".format(names[1],hand2))
            break
        elif NUMBER_OF_PLAYERS == 3:
            print("{}'s hand is {}".format(names[0],hand1))
            print("{}'s hand is {}".format(names[1],hand2))
            print("{}'s hand is {}".format(names[2],hand3))
            break
        elif NUMBER_OF_PLAYERS == 4:
            print("{}'s hand is {}".format(names[0],hand1))
            print("{}'s hand is {}".format(names[1],hand2))
            print("{}'s hand is {}".format(names[2],hand3))
            print("{}'s hand is {}".format(names[3],hand4))
            break
        elif NUMBER_OF_PLAYERS == 5:
            print("{}'s hand is {}".format(names[0],hand1))
            print("{}'s hand is {}".format(names[1],hand2))
            print("{}'s hand is {}".format(names[2],hand3))
            print("{}'s hand is {}".format(names[3],hand4))
            print("{}'s hand is {}".format(names[4],hand5))
            break
        elif NUMBER_OF_PLAYERS == 6:
            print("{}'s hand is {}".format(names[0],hand1))
            print("{}'s hand is {}".format(names[1],hand2))
            print("{}'s hand is {}".format(names[2],hand3))
            print("{}'s hand is {}".format(names[3],hand4))
            print("{}'s hand is {}".format(names[4],hand5))
            print("{}'s hand is {}".format(names[5],hand6))
            break
        elif NUMBER_OF_PLAYERS == 7:
            print("{}'s hand is {}".format(names[0],hand1))
            print("{}'s hand is {}".format(names[1],hand2))
            print("{}'s hand is {}".format(names[2],hand3))
            print("{}'s hand is {}".format(names[3],hand4))
            print("{}'s hand is {}".format(names[4],hand5))
            print("{}'s hand is {}".format(names[5],hand6))
            print("{}'s hand is {}".format(names[6],hand7))
            break
        elif NUMBER_OF_PLAYERS >= 8:
            print("Sorry, the maximum number of players is 7")
    except ValueError:
        print("Error: the value {} can't be converted to an integer".format(NUMBER_OF_PLAYERS))
#%%
for n, i in enumerate(hand1):
    if i == "J":
        hand1[n] = 11
    elif i == "Q":
        hand1[n] = 12
    elif i == "K":
        hand1[n] = 13
    elif i == "A":
        hand1[n] = 14
    else:
        hand1[n] = int(i)

for n, i in enumerate(hand2):
    if i == "J":
        hand2[n] = 11
    elif i == "Q":
        hand2[n] = 12
    elif i == "K":
        hand2[n] = 13
    elif i == "A":
        hand2[n] = 14
    else:
        hand2[n] = int(i)

for n, i in enumerate(hand3):
    if i == "J":
        hand3[n] = 11
    elif i == "Q":
        hand3[n] = 12
    elif i == "K":
        hand3[n] = 13
    elif i == "A":
        hand3[n] = 14
    else:
        hand3[n] = int(i)

for n, i in enumerate(hand4):
    if i == "J":
        hand4[n] = 11
    elif i == "Q":
        hand4[n] = 12
    elif i == "K":
        hand4[n] = 13
    elif i == "A":
        hand4[n] = 14
    else:
        hand4[n] = int(i)

for n, i in enumerate(hand5):
    if i == "J":
        hand5[n] = 11
    elif i == "Q":
        hand5[n] = 12
    elif i == "K":
        hand5[n] = 13
    elif i == "A":
        hand5[n] = 14
    else:
        hand5[n] = int(i)

for n, i in enumerate(hand6):
    if i == "J":
        hand6[n] = 11
    elif i == "Q":
        hand6[n] = 12
    elif i == "K":
        hand6[n] = 13
    elif i == "A":
        hand6[n] = 14
    else:
        hand6[n] = int(i)

for n, i in enumerate(hand7):
    if i == "J":
        hand7[n] = 11
    elif i == "Q":
        hand7[n] = 12
    elif i == "K":
        hand7[n] = 13
    elif i == "A":
        hand7[n] = 14
    else:
        hand7[n] = int(i)

#%%
while 1:
    try:
        if NUMBER_OF_PLAYERS <= 1:
            print("Find a friend to play with you! Exiting game")
            break
        elif NUMBER_OF_PLAYERS == 2:
            highcard = [max(hand1), max(hand2)]
            winning_card = max(highcard)
            winner = highcard.index(winning_card)
            print("The winner is {}".format(names[winner]))
            break 
        elif NUMBER_OF_PLAYERS == 3:
            highcard = [max(hand1), max(hand2), max(hand3)]
            winning_card = max(highcard)
            winner = highcard.index(winning_card)
            print("The winner is {}".format(names[winner]))
            break 
        elif NUMBER_OF_PLAYERS == 4:
            highcard = [max(hand1), max(hand2), max(hand3), max(hand4)]
            winning_card = max(highcard)
            winner = highcard.index(winning_card)
            print("The winner is {}".format(names[winner]))
            break 
        elif NUMBER_OF_PLAYERS == 5:
            highcard = [max(hand1), max(hand2), max(hand3), max(hand4), max(hand5)]
            winning_card = max(highcard)
            winner = highcard.index(winning_card)
            print("The winner is {}".format(names[winner]))
            break 
        elif NUMBER_OF_PLAYERS == 6:
            highcard = [max(hand1), max(hand2), max(hand3), max(hand4), max(hand5), max(hand6)]
            winning_card = max(highcard)
            winner = highcard.index(winning_card)
            print("The winner is {}".format(names[winner]))
            break 
        elif NUMBER_OF_PLAYERS == 7:
            highcard = [max(hand1), max(hand2), max(hand3), max(hand4), max(hand5), max(hand6), max(hand7)]
            winning_card = max(highcard)
            winner = highcard.index(winning_card)
            print("The winner is {}".format(names[winner]))
            break
    except ValueError:
        print("Error: the winner cannot be computed")