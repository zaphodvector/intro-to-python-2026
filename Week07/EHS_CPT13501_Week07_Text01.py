"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week07_Text02
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-03-04
    Purpose:	The purpose of this program is to print a user's input in a diagonally spaced format as
                long as the user's input is three words or longer.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-03-04	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
phrase = input('Enter a phrase with three or more words.')      #Grabbing the user's input.

while len(phrase.split()) < 3:
    print('Your phrase is not long enough!')
    phrase = input('Enter a phrase with three or more words.')

    #Using a while loop to verify that the user's input is long enough with 'len()'/'.split' and 
    #prompting the user to try again.

for word in phrase.split():
    position = phrase.index(word)
    print(' ' * position + word)
    phrase = phrase.replace(word, ' ' * len(word), 1)

    #Using a for loop to find the starting point of each word in the phrase.
    #Printing the word from the list in the correct place.
    #Replacing the word that was printed with spaces for the next line. 