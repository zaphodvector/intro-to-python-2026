"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPY13501_Week05_Text03
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-21
    Purpose:	The purpose of this program is to flip a coin nine times and print the outputs using if
                statements.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-21	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import random                                   #Importing the random module.

heads_count = 0                                 #Defining two variables that will be modified for each
tails_count = 0                                 #coin flip.

                                                                                                        

flip1 = random.choice(['Heads', 'Tails'])       #Using the random choice function to randomly select 
print("Flip 1:", flip1 + '!')                   #between two options in a list.
if flip1 == 'Heads':                            #Using an if statement to determine if the coin
    heads_count += 1                            #landed on heads, then adding 1 to heads.
else:                                           #Using an else statement to add 1 to tails.
    tails_count += 1



flip2 = random.choice(['Heads', 'Tails'])       #Repeat 8 more times for each coin flip.
print("Flip 2:", flip2 + '!')
if flip2 == 'Heads':
    heads_count += 1
else:
    tails_count += 1



flip3 = random.choice(['Heads', 'Tails'])
print("Flip 3:", flip3 + '!')
if flip3 == 'Heads':
    heads_count += 1
else:
    tails_count += 1



flip4 = random.choice(['Heads', 'Tails'])
print("Flip 4:", flip4 + '!')
if flip4 == 'Heads':
    heads_count += 1
else:
    tails_count += 1



flip5 = random.choice(['Heads', 'Tails'])
print("Flip 5:", flip5 + '!')
if flip5 == 'Heads':
    heads_count += 1
else:
    tails_count += 1



flip6 = random.choice(['Heads', 'Tails'])
print("Flip 6:", flip6 + '!')
if flip6 == 'Heads':
    heads_count += 1
else:
    tails_count += 1



flip7 = random.choice(['Heads', 'Tails'])
print("Flip 7:", flip7 + '!')
if flip7 == 'Heads':
    heads_count += 1
else:
    tails_count += 1



flip8 = random.choice(['Heads', 'Tails'])
print("Flip 8:", flip8 + '!')
if flip8 == 'Heads':
    heads_count += 1
else:
    tails_count += 1



flip9 = random.choice(['Heads', 'Tails'])
print("Flip 9:", flip9 + '!')
if flip9 == 'Heads':
    heads_count += 1
else:
    tails_count += 1

                                                                                                        #|

heads_percent = f"{((heads_count / 9) * 100):.2f}"      #Defining new variables for the total percentages,
tails_percent = f"{((tails_count / 9) * 100):.2f}"      #and formatting to two decimals for cleanliness

print("\nResults:")                                     #Printing results and listing final outcomes with
print("Heads count:", heads_count)                      #percentages.
print("Tails count:", tails_count)
print("Heads percentage:", heads_percent, "%")
print("Tails percentage:", tails_percent, "%")