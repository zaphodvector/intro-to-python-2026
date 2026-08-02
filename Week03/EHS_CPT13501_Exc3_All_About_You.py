"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Exc3_All_About_You
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-07
    Purpose:	The purpose of this program is to ask the user for their name, age, college, and pet's
                name and print it back to the user in a cohesive paragraph.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-07	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
name = input('\nEnter your name: ')

age = input('\nEnter your age: ')

college = input('\nEnter your college: ')

petname = input('\nEnter your pet\'s name: ')

#I am using the input function attatched to a literal string to ask the user for their name, age, 
#college, and pet's name individually and assign them to a variable

print(f'\nHello, my name is {name} and I am {age} years '
      f'old. \nI\'m enjoying my time at {college}, \nthough '
      f'I miss my pet {petname} very much.')

#I am using the print function with f strings to print a properly formatted paragraph while 
#inserting the user inputs into the correct places with the curly braces.