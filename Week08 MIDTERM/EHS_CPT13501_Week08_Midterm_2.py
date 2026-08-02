"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week08_Midterm
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-03-09
    Purpose:	The purpose of this program is to play an automatic game of Yahtzee! until all five dice
                are rolled to be the same within three rolls. Then it asks the user if they would like
                to play again.
                I used an A.I. agent for this project that had starting instructions not to give me any
                lines of code, just to explain what types of functions I should use or how I could fix
                the problems I had. My dad called this a 'Socratic' agent.  
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-03-09	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import random
import time
#Importing modules for dice rolling and implementing a small wait time for readability.

start = False

while start == False:
    userbegin = input('Would you like to see how long it takes to roll \'Yahtzee!\'? Y/N:')
    if (userbegin.upper()) == 'Y':
        start = True
    elif (userbegin.upper()) == 'N':
        print('Maybe next time!')
        exit()
    else:
        print('Please enter a valid input, either Y or N.')

#Creating a while loop to ask the user if they would like to begin. Prompting them to try again for an 
#invalid input and exiting if they say no.
    

if start == True:
    print('Let\'s Begin!\nThis program will print a result for each game.')
    time.sleep (1)

#Beginning the game and using time.sleep to let the user read the message.

def count_rolls(rolls):
    dice = {}
    for roll in rolls:
        if roll in dice:
            dice[roll] += 1
        else:
            dice[roll] = 1
    return dice

#This function's purpose is to rank the dice by which number was rolled the most.
#For example [3, 3, 3, 5, 3] becomes {3: 4, 5: 1}. Four threes and one five.
#Rolls is the list of the numbers that are rolled for each time, and dice is an empty dictionary that 
#is used to store the rankings for each number to later choose which to keep/reroll.
#'For roll in rolls:' iterates through each roll and adds the number plus it's count if it isn't in 
#the dictionary yet, or adds one to the count if it is in the dictionary.

def best_roll(dice):
    return max(dice, key=dice.get)

#This function selects the dice not to reroll by choosing the highest ranked number.
#If there is no winner or there is a tie between two the function chooses whichever came first in
#the dictionary.

def reroll(results, best_number):
    for i in range(len(results)):
        if results[i] != best_number:
            results[i] = random.randint(1, 6)
    return results

#Results is the list of the five dice, and best number is the number the program will try to reroll for. 
#The for loop goes through each number in the results list, and compares them against the selected
#best number, if they are not equal, they are rerolled with random.randint.
#Results and best number are defined in the play yahtzee loop.

games_played = 0
#Defining a variable for a game counter.

def play_yahtzee():
    global games_played
    results = []
    for i in range(5):
        results.append(random.randint(1, 6))

#Play yahtzee is the start of the main game function. It defines the results list and rolls the fist
#five dice. Global tells the computer that it needs to grab from the previously defined games_played
#function and not to create a new local one.   
        
    for i in range(2):  #2 rerolls
        dice = count_rolls(results)
        best_number = best_roll(dice)
        if len(dice) == 1:
            break
        else:
            results = reroll(results, best_number)

#This loop runs up to two times. It defines the dictionary (dice) and checks the length to see 
#if the program has achieved Yahtzee and will exit the loop. So if the length of the dictionary
#is one, then all of the numbers must bee the same. Otherwise the program calls the reroll 
#function up to two more times.  

    dice = count_rolls(results)
    if len(dice) == 1:
        print(f"#{games_played + 1}    {results}")
        print("YAHTZEE!")
        games_played += 1
        print(f'It took {games_played} games to get Yahtzee.')
        return True
    else:
        print(f"#{games_played + 1}    {results}")
        print("No Yahtzee this time.\n")
        time.sleep(.1)
        games_played += 1
        return False

#This if else statement is the final check of the state of the dice before deciding whether to begin a
#new game or not. Dice is defined again and once again compared to see if the length of the dictionary
#is one. If it is, the program prints the number of games played, the results of the game, and a 
#congratulatory string. If it is unsuccessful the program prints the results of the unsuccessful game,
#along with what iteration of game it was. It also sleeps for a tenth of a second to visualize the rolls
#better for the user. Games_played is increased by one and the program returns false to start a new game.  

while True:
    games_played = 0

    while play_yahtzee() == False:
        pass

#This while true loop runs until the program is closed. This contains the play again part of the program.
#Games played is reset at the start of this loop for each time the player wants to play again. The second
#while loop calls play_yahtzee and checks what it returns. If it is false then it does nothing and runs 
#the loop again. If it returns true, this loop exits and goes to the playagain loop.       

    playagain = False

    while playagain == False:
        useragain = input('Would you like to play again? Y/N:')
        if (useragain.upper()) == 'Y':
            playagain = True
        elif (useragain.upper()) == 'N':
            print('Goodbye!')
            exit()
        else:
            print('Please enter a valid input, either Y or N.')

#This while loop asks the user if they would like to play again, and will only accept the proper input.
#It runs almost exactly the same as the beginning while loop, just with different print statements and 
#variables.     