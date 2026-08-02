"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_UserInputsAndFormattedOutputs
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-04
    Purpose:	The purpose of this program is to take user inputs and give formatted outputs.(Example)
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-04	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
print("Please enter your name: ")            # prompt the user for their name
strYourName = input()                        # get the user's name and put it in the variable
print("Well!  Hello there,",
      strYourName + "!")        # say hello to the user  - Notice the + instead of a comma
                                # to control the removal of the extra separator space!
''' 
In this next block of code, we will prompt the user to enter variable of different types.
'''
print("Please enter your height (in inches): ")
intHeightInInches = int(input())                # get a string but convert to an integer
print("Also, please tell me your favorite color: ")
strFavColor = input()
print("Cool!  So, you are", intHeightInInches, "inches tall and your",
    "favorite color is", strFavColor + "!")     # text is joined with commas
                                            # but has a space separator... so the + skips it!       
'''
 In this next block of code, we will do some math using the numeric values we have collected.
 We will see the difference between integer math and floating point math.
''' 
print("-" * 80)         # prints a line of 80 dashes in the output

# This next line shows INTEGER division.  Both operands are integers so the answer is an integer
intHeightInFeetOnly = intHeightInInches // 12   # note double // for integer division!
print("Well, by my calculations, you are", intHeightInFeetOnly, "feet tall!")
fltHeightInFeetWithFraction = float(intHeightInInches / 12)  # forces to float
print("However, you are more accurately",
    f'{fltHeightInFeetWithFraction:.2f}',     # format to 2 decimal places
    "feet tall.")
print("But that isn't how we normally refer to people's heights!") # notice ' inside of ""
intLeftoverInches = intHeightInInches % 12     # the % operator delivers the remainder!
print("We would normally say that you are", intHeightInFeetOnly, "feet and",
    intLeftoverInches, "inches tall.")
print("-" * 80)  
