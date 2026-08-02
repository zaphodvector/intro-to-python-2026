"""
-----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT_13501_Week06_Text2
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-27
    Purpose:	The purpose of this program is to play the High Low game with the user, looping until the
                user wins or exits. As well as letting the user start a new game in the middle of a 
                current game.
-----------------------------------------------------------------------------------------------------------
    Change Log
-----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-27	Original Version of Code
-----------------------------------------------------------------------------------------------------------
"""
import random                       #Importing the random module.

quitsentinel = 0                    #Defining a sentinel.

def play_game():                        #Defining a function to play the game.
    answer = random.randint(1, 100)     #Picking a random number as the answer.
    guesses = 0                         #Defining the number of guesses as zero.

    print("\nI have picked a number between 1 and 100.")        #Printing instructions for the user with
    print("Enter", quitsentinel, "at any time to quit.\n")      #the sentinel embedded

    guess = -1                                      #Defining the guess variable as an invalid number first.
    while guess != answer:                          #Creating a loop that runs while the guess is wrong
        guess_input = input("Your guess: ")         #Defining a variable for the string the user inputs.
        while not guess_input.isdigit():            #Creating another loop while the answer isn't a number
            print("Please enter a whole number.")   #to screen for non-answers.
            guess_input = input("Your guess: ")     #Prompting for another guess.
        guess = int(guess_input)                    #Converting the users string input to a integer if valid.

        if guess == quitsentinel:                   #Using an if statement to check for the quit sentinel.
            print("You quit! The number was", answer)   #Telling the user the correct answer if they quit.
            return                                  #Exiting the play_game function and returning to the
                                                    #main function.
        guesses += 1                                #Adding one guess for each incorrect input.

        if guess < 1 or guess > 100:                #Using an if statement to check if the number is in the
            print("Please guess a number between 1 and 100.")   #correct range. If no, telling the user and
            guesses -= 1                            #subtracting 1 from the guesses for an non-answer.
        elif guess < answer:                #Using two elif functions to tells the user if their guess is
            print("Too low! Try higher.")   #too high or too low.
        elif guess > answer:
            print("Too high! Try lower.")
        else:                                             #Using an else statement for the correct answer.
            print("\nCorrect! The number was", answer)
            if guesses == 1:                              #Another if statement if the user got lucky. 
                print("You got it in 1 guess!")
            else:                                         #Else the amount of guesses they used is printed.
                print("You got it in", guesses, "guesses!")

def main():                                             #Defining the Main function.
    print("========================================")   #Printing a title bar for the game.
    print("      Welcome to the Hi-Lo Game!")
    print("========================================")

    again = "yes"                           #Defining a function to be part of a loop to let the user  
    while again == "yes" or again == "y":   #play again.
        play_game()                         #Calling the play game function to start the game.
        again = input("\nWould you like to play again? (yes/no): ").strip().lower()
            #Checking if the user would like to play again and assigning their input to the again variable.
    print("\nThanks for playing! Goodbye!")

main()      #Calling the main function.