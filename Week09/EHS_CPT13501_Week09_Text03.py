"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Text_03
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-03-28
    Purpose:	The purpose of this program is to create a deck of cards, states all of the created cards,
                shuffles the deck, and deals two hands of five cards.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-03-28	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import random
import pprint

suit_names = ["Spades", "Hearts", "Diamonds", "Clubs"]
suit_symbols = ["♠", "♥", "♦", "♣"]
card_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

#Defining a list for each attribute that the cards will have. (Color comes later)

cards = {}
for suit_name, suit_symbol in zip(suit_names, suit_symbols):
    color = "Red" if suit_name in ["Hearts", "Diamonds"] else "Black"
    for rank in card_ranks:
        card_name = rank + suit_symbol if rank == "10" else rank[0] + suit_symbol
        cards[card_name] = {"Rank:" rank, "Suit:" suit_name, "Suit Symbol:" suit_symbol, "Color:" color}

#After defining a dictionary for the deck, I can use a zip function to pair the suit names with their
#corresponding symbol. Then the color is defined by an if statement. The for loop iterates through each
#rank and takes the first number or letter only, shortening them for the card names. The last line assigns 
#the previously defined variables to each card name created.

pprint.pprint(cards, )

#Instead of using just print(cards), which was illegible, I asked AI how to make it 
#readable and it showed me this built in module: "Pretty Print".

card_keys = list(cards.keys())
random.shuffle(card_keys)
cards = {key: cards[key] for key in card_keys}

#This chunk shuffles the deck. After creating a list of the cards they can be shuffled.
#A new dictionary is created from the shuffled deck by iterating through the shuffled
#list and recreating the cards dictionary.

my_hand = {}
your_hand = {}
deck_keys = list(cards.keys())

#Defining variables to be used for dealing the cards.

for i in range(5):
    my_card_key = deck_keys.pop(0)
    my_hand[my_card_key] = cards[my_card_key]
    your_card_key = deck_keys.pop(0)
    your_hand[your_card_key] = cards[your_card_key]

#To deal the now shuffled cards a for loop pops a card from the deck for each hand
#and stores the card in the hand's list. This iterates five times and deals ten cards.

print("\nMyHand:")
pprint.pprint(my_hand)
print("\nYourHand:")
pprint.pprint(your_hand)
print("\n")