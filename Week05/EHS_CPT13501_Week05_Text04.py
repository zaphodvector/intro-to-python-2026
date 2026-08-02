"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week05_Text04
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-21
    Purpose:	The purpose of this program is to simulate a person playing poker five times and shows 
                the results of each game and the total result.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-21	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import random                                   #Importing random module

balance = 500                                   #Defining total balance
buy_in = 100                                    #Defining buy in cost

good_nights = 0                                 #Defining good and bad nights
bad_nights = 0

print("Starting balance: $" + str(balance))     #Printing balance with a string modifier

#Night 1
balance -= buy_in                               #Subtracting and re-defining the balance after the buy in
luck1 = random.choice(["good", "bad"])          #Defining a luck variable for each night and using the
                                                #random choice function to pick between good and bad luck

if luck1 == "good":
    winnings = random.uniform(0.8 * buy_in, 4.0 * buy_in)
    balance += winnings
    good_nights += 1
    print("\nNight 1: Good luck! Won $" + str(round(winnings, 2)))
else:
    bad_nights += 1
    print("\nNight 1: Bad luck. Lost buy-in.")

print("Balance after Night 1: $" + str(round(balance, 2)))

    #Using an if statement to check if the night was good, then 
    #calculating the winnings of the night with the random uniform
    #function to choose a random float between two values. 
    #Modifying the balance and the number of good nights and 
    #printing the results.  *or*
    #Using an else statement to modify the number of bad nights 
    #and printing the results plus the final balance after the night.
    #Repeated for each following night.


#Night 2
balance -= buy_in
luck2 = random.choice(["good", "bad"])

if luck2 == "good":
    winnings = random.uniform(0.8 * buy_in, 4.0 * buy_in)
    balance += winnings
    good_nights += 1
    print("\nNight 2: Good luck! Won $" + str(round(winnings, 2)))
else:
    bad_nights += 1
    print("\nNight 2: Bad luck. Lost buy-in.")

print("Balance after Night 2: $" + str(round(balance, 2)))


#Night 3
balance -= buy_in
luck3 = random.choice(["good", "bad"])

if luck3 == "good":
    winnings = random.uniform(0.8 * buy_in, 4.0 * buy_in)
    balance += winnings
    good_nights += 1
    print("\nNight 3: Good luck! Won $" + str(round(winnings, 2)))
else:
    bad_nights += 1
    print("\nNight 3: Bad luck. Lost buy-in.")

print("Balance after Night 3: $" + str(round(balance, 2)))


#Night 4
balance -= buy_in
luck4 = random.choice(["good", "bad"])

if luck4 == "good":
    winnings = random.uniform(0.8 * buy_in, 4.0 * buy_in)
    balance += winnings
    good_nights += 1
    print("\nNight 4: Good luck! Won $" + str(round(winnings, 2)))
else:
    bad_nights += 1
    print("\nNight 4: Bad luck. Lost buy-in.")

print("Balance after Night 4: $" + str(round(balance, 2)))


#Night 5
balance -= buy_in
luck5 = random.choice(["good", "bad"])

if luck5 == "good":
    winnings = random.uniform(0.8 * buy_in, 4.0 * buy_in)
    balance += winnings
    good_nights += 1
    print("\nNight 5: Good luck! Won $" + str(round(winnings, 2)))
else:
    bad_nights += 1
    print("\nNight 5: Bad luck. Lost buy-in.")

print("Balance after Night 5: $" + str(round(balance, 2)))


#Final Results
print("\nFinal balance: $" + str(round(balance, 2)))

if balance > 500:
    print("Overall result: Lucky (Made Money)")
elif balance < 500:
    print("Overall result: Unlucky (Lost Money)")
else:
    print("Overall result: Broke even")

print("Good nights:", good_nights)
print("Bad nights:", bad_nights)

#Printing the final results and stating if the player lost 
#or gained money with if, elif, and else statements.
#Printing the final number of good and bad nights.