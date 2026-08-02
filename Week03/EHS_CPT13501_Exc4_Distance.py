"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Exc4_Distance
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-07
    Purpose:	The purpose of this program is to convert miles to kilometers and return to the user with
                two decimal places of precision
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-07	Original Version of Code
----------------------------------------------------------------------------------------------------------
""" 
print('This program converts miles into kilometers.')

miles = input('\nPlease enter the distance in miles: ')

#Using a print function and an input function to ask the user to input a 
#distance in miles and assigning that value to the variable 'miles'.

kilometers = float(miles) * 1.60935

print(f'\n{miles} miles is equal to {kilometers} kilometers!\n')

#Defined a new variable called 'kilometers' and set it equal
#to the floating number of miles times the conversion rate.
#Used a f string to tell the user how many kilometers 
#their input is equal to.