"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week11_Text1
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-04-10
    Purpose:	The purpose of this program is to build a class of Coins, containing all valid current 
                coins, flipping between 5 to 10 coins and using the attributes assigned to the objects
                in the class to give some results from the flips.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-04-10	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import random

class Coin:
    dict_coins = {
        "penny": 0.01,
        "nickel": 0.05,
        "dime": 0.10,
        "quarter": 0.25,
        "half dollar": 0.50,
        "dollar": 1.00
    }

# Creating the Coin class and immediately defining a dictionary of valid coins.

    def __init__(self, name):
        name = name.lower()
        self.name = name
        self.value = Coin.dict_coins[name]
        self.face = None

    # Initializing each object from the dictionary by assigning it a name, a value, and a currently absent
    # spot for the flipped face to go.

    def flip(self):
        self.face = random.choice(["Heads", "Tails"])
        return self.face

    # Creating a flip function with self as the parameter.

def main():
    coin_names = list(Coin.dict_coins.keys())
    count = random.randint(5, 10)
    coins = [Coin(random.choice(coin_names)) for _ in range(count)]

    total = 0.0
    headsct = 0
    tailsct = 0
    for coin in coins:
        result = coin.flip()
        print(f"{coin.name.capitalize()}: {result} (${coin.value:.2f})")
        total += coin.value
        if result == "Heads":
            headsct += 1
        else:
            tailsct += 1

# The main function demonstrates the contents of the class by flipping a number of coins, then 
# reporting the final outcomes calculated by the attributed of each object.

    print(f"\nTotal coins: {count}")
    print(f"Total Heads: {headsct}")
    print(f"Total Tails: {tailsct}")
    print(f"Total value: ${total:.2f}")

main()