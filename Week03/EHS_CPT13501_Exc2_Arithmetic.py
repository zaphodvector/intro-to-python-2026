"""
-----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Exc2_Arithmetic
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-07
    Purpose:	The purpose of this program is to prompt the user for two floating point numbers, find the
                sum, difference and product of the two numbers and print each outcome to two decimals.
-----------------------------------------------------------------------------------------------------------
    Change Log
-----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-07	Original Version of Code
-----------------------------------------------------------------------------------------------------------
"""     
print('Please enter two numbers and press enter after typing each one.')

num1 = input('\nFirst Number: ')

num2 = input('\nSecond Number: ')

#I start with a print statement asking the user two input their two numbers properly and then use the 
#imput function with a string to define the two variables that I will be working with.

sum = float(num1) + float(num2)

difference = float(num1) - float(num2)

product = float(num1) * float(num2)

#I define three new variables and assign their values to the sum, difference, and product of the two 
#numbers respectively.

print('\nThe sum of your two numbers is: ' f'{sum:.2f}')

print('\nThe difference of your two numberes is: ' f'{difference:.2f}')

print('\nThe product of your two numbers is: ' f'{product:.2f}\n')

#I return the final outcome to the user with seperate print functions and format the answer to two 
#decimal places. I also include newline markers throughout the code to make it look pretty in the terminal.