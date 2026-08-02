"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week06_Text1
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-25
    Purpose:	The purpose of this program is to determine the number of odd, equal, and zero digits in 
                a user's input.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-25	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""

num = input('Please input a number:')       #Asking for input from the user and putting it in a variable.

odds = 0                                    #Defining a variable for each type of number.
evens = 0
zeroes = 0

for char in num:                            #Using a for loop and defining a variable to check if each
    if char.isdigit():                      #character is a number before testing for what type of digit.
         digit = int(char)                  #Converting each digit into an integer for testing.
         if digit == 0:                     #Using an if, elif, and else function to alter the count for 
            zeroes += 1                     #each type of number.
         elif digit % 2 == 0:
             evens += 1
         else:
             odds += 1

print(f'There are {odds} odd digits, {evens} even digits, and {zeroes} zeroes!')   

#Printing my results embedded with an f string.