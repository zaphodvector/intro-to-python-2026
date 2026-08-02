"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Text02
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-04-17
    Purpose:	The purpose of this program is to use the print function to ask the user for three numbers
                and average them together.
----------------------------------------------------------------------------------------------------------
    Change Log: A try and except block was added for value errors.
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-07	Original Version of Code
----------------------------------------------------------------------------------------------------------
""" 
print('Please enter three numbers you would like to average together. (Hit enter after each one)\n')

#Using a print function to ask the user for three numbers and 
#telling them how to properly enter them.

try:
    num1 = input()
    print()                                 
    num2 = input()
    print()                                 
    num3 = input()

#Using the input function with empty strings to ask for
#three separate numbers and assigning each of them to a variable.

    average = (float(num1) + float(num2) + float(num3))/3

    print('\nThe average of your three numbers is ' f'{average:.2f}''!')

#I define a variable called average and set it equal to 
#the float of each input added together and divided by three. 

#Use a print function with a literal string and
#formatting function before the 'average' variable
#to stop the computer after two decimal places. 

except ValueError:
    print('Invalid input. Please enter numbers only.')

# The only possible crash in this program is a value error which is fixed by this try and except block.

