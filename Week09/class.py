"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week09_Text_Sample01
    Author:	Ed Weber
    Language:	Python
    Date:	2025-01-06
    Purpose:	The purpose of this program is to show some examples of working with individual
                lists including using some of the methods and functions such as len, append, extend
                index, and list comprehension for just a few.
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
    print('First, let\'s observe simple list manipulations...')
    lstFruitStand = ['Apples','Oranges','Bananas','Pears']
    lstFruitItemCount = [10,5,11,0]
    print('Original Fruit Stand Items and Counts')
    for i in range(len(lstFruitStand)):
        print(lstFruitStand[i],"-",lstFruitItemCount[i])
    PauseAndReflect()
    print('*' * 80)
    print('Next, we will restock our fruit stand with items from our vendor...')
    lstFruitStand.append('Melons')  # append a single item
    lstFruitStand.append('Plums')   # append a single item
    lstFruitItemCount.extend([4,5]) # extend by adding multiple items
    print('Added melons and plums....')
    print(lstFruitStand,'\n',lstFruitItemCount)
    print('Added 10 more apples and 7 more bananas...')
    intWhichFruitIsApple = lstFruitStand.index('Apples')
    lstFruitItemCount[intWhichFruitIsApple] += 10
    intWhichFruitIsBanana = lstFruitStand.index('Bananas')
    lstFruitItemCount[intWhichFruitIsBanana] += 7
    print('Updated Fruit Stand Items and Counts')
    for i in range(len(lstFruitStand)):
        print(lstFruitStand[i],"-",lstFruitItemCount[i])
    PauseAndReflect()
    print('*' * 80)
    print('Now, we will sell some random fruits...')
    for i in range(3):
        strWhichFruitSold = random.choice(lstFruitStand)
        intFruitIndex = lstFruitStand.index(strWhichFruitSold)
        intNumberAvailable = lstFruitItemCount[intFruitIndex]
        if intNumberAvailable > 0:
            intHowManySold = random.randrange(1, lstFruitItemCount[intFruitIndex]+1)
            lstFruitItemCount[intFruitIndex] -= intHowManySold
            print(f'  Sold {intHowManySold} {strWhichFruitSold}...')
        else:
            print(f'  Sorry, we are currently out of {strWhichFruitSold}...')
    print('Updated Fruit Stand Items and Counts')
    for i in range(len(lstFruitStand)):
        print(lstFruitStand[i],"-",lstFruitItemCount[i])
    PauseAndReflect()
    print('*' * 80)
    
    print('Now we will donate all fruits with counts less than 5 ')
    print('  to the food pantry...')
    print('  For this step, we will use list comprehension...')
    lstDonateNames = [lstFruitStand[i] for i in range(len(lstFruitItemCount)) if lstFruitItemCount[i] < 5]
    lstDonatedCount = [lstFruitItemCount[i] for i in range(len(lstFruitItemCount)) if lstFruitItemCount[i] < 5]
    lstFruitStand = [lstFruitStand[i] for i in range(len(lstFruitItemCount)) if lstFruitItemCount[i] >= 5]
    lstFruitItemCount = [lstFruitItemCount[i] for i in range(len(lstFruitItemCount)) if lstFruitItemCount[i] >= 5]
    intFruitIndex = 0
    for intSingleDonatedCount in lstDonatedCount:
        if intSingleDonatedCount > 0:
            print(f'  Donated {intSingleDonatedCount} {lstDonateNames[intFruitIndex]}.')
        else:
            print(f'  Removed empty {lstDonateNames[intFruitIndex]} container.')
        intFruitIndex += 1
    print('Updated Fruit Stand Items and Counts')
    for i in range(len(lstFruitStand)):
        print(lstFruitStand[i],"-",lstFruitItemCount[i])
    PauseAndReflect()
    print('*' * 80)
    print("Working with single lists is relatively easy having many functions")
    print("  to help with inserting, appending, popping, removing and iterating")
    print("  through the lists.  But working with {related} lists is a bit more complicated.")
    print("In the next program, we will see that working with dictionaries helps with")
    print("  the need to keep ordered pairs of related objects properly in sync.")

def PauseAndReflect():
    print("-" * 80)
    input("Hit the Enter Key to continue...")

main()