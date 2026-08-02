"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week03_Project1
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-14
    Purpose:	The purpose of this program is to prompt for the users first and last name and create a 
                username based on the response
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-14	Original Version of Code
----------------------------------------------------------------------------------------------------------
""" 
import random

#importing the random function

strfirstname = input('Please input your first name')
strlastname = input('Please enter your last name')

#defining two variables that are wqual to the user's input

username = strfirstname[:1] + strlastname[:5] + str(random.randint(10, 99))

#defining a new variable, username, that is equal to the first letter of the first name of the user, the first 5 characters
#of the last name, and a random number from 10 to 99

print(username)