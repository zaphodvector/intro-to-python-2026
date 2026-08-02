"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT12301_Week04_Text_Project3
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-14
    Purpose:	The purpose of this program is to find the closest whole numbers greater to and less 
                than the users input.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-14	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""

import math

#Importing the math module

fltnum = float(input('Please input a number.'))

#Defining a variable equal to the float of the user input

strlessthan = math.floor(fltnum)
strgreaterthan = math.ceil(fltnum)

#Defining two variables equal to the closest whole numbers greater and less than the user input

print('The closest whole numbers to your input are', strlessthan, 'and', strgreaterthan)