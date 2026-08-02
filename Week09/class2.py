"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week09_Text_Sample02
    Author:	Ed Weber
    Language:	Python
    Date:	2025-01-06
    Purpose:	The purpose of this program is to show examples of using dictionaries and
                how working with dictionaries is much easier when one needs to manipulate
                key->value pairs.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2025-01-06	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import random
def main():
    print('*' * 80)
    print('First, let\'s create and observe simple dictionary manipulations...')
    dictFruitStand = {'Apples': 10,'Oranges': 5,'Bananas': 11,'Pears': 0}
    print('Original Fruit Stand Items and Counts (from Dictionary)')
    for strFruit, intQty in dictFruitStand.items():
        print(f'{strFruit} - {str(intQty)}')
    PauseAndReflect()
    print('*' * 80)
    print('Next, we will restock our fruitstand with items from our vendor...')
    dictFruitStand['Melons'] = 4    # append a single dictionary key and value
    dictFruitStand['Plums'] = 5     # append a single dictionary key and value
    print('Added melons and plums....')
    print(dictFruitStand)
    print('Added 10 more apples and 7 more bananas...')
    dictFruitStand['Apples'] += 10
    dictFruitStand['Bananas'] += 7
    print('Updated Fruit Stand Items and Counts')
    for strFruit, intQty in dictFruitStand.items():
        print(f'{strFruit} - {str(intQty)}')
    PauseAndReflect()
    print('*' * 80)
    print('Now, we will sell some random fruits...')
    for i in range(3):
        strWhichFruitSold = random.choice(list(dictFruitStand.keys()))
        intNumberAvailable = dictFruitStand[strWhichFruitSold]
        if intNumberAvailable > 0:
            intHowManySold = random.randrange(1, intNumberAvailable + 1)
            dictFruitStand[strWhichFruitSold] -= intHowManySold
            print(f'  Sold {intHowManySold} {strWhichFruitSold}...')
        else:
            print(f'  Sorry, we are currently out of {strWhichFruitSold}...')
    print('Updated Fruit Stand Items and Counts')
    for strFruit, intQty in dictFruitStand.items():
        print(f'{strFruit} - {str(intQty)}')
    PauseAndReflect()
    print('*' * 80)
    
    print('Now we will donate all fruits with counts less than 5 ')
    print('  to the food pantry...')
    for strFruitName in list(dictFruitStand.keys()):
        intFruitQty = dictFruitStand[strFruitName]
        if intFruitQty < 5:
            if intFruitQty > 0:
                print(f'  Donated {intFruitQty} {strFruitName}.')
            else:
                print(f'  Removed empty {strFruitName} container.')
            dictFruitStand.pop(strFruitName)
    print('Updated Fruit Stand Items and Counts')
    for strFruit, intQty in dictFruitStand.items():
        print(f'{strFruit} - {str(intQty)}')
    PauseAndReflect()
    print('*' * 80)
    print("As we can see, dictionaries make it *MUCH* easier for working with")
    print("  key->value pairs!")

def PauseAndReflect():
    print("-" * 80)
    input("Hit the Enter Key to continue...")

main()