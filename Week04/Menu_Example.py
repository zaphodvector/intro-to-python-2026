"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week04_Text_Sample
    Author:	Ed Weber
    Language:	Python
    Date:	2024-12-29
    Purpose:	The purpose of this program is to provide examples of the strings, lists, and
                basic dictionary functions.  It will review some previously learned code and
                take a peek at some up-coming concepts as well.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2024-12-29	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
def main():                             # define a function called 'main'
    print("This program will provide examples of programming concepts") 
    print("  that were previously covered or covered this week in class.")
    print("\nThis first section will exhibit some string manipulations...")
    fncSeparateAndPause()               # call a function defined below

    strFullName = input('Please enter your full name:\n')   # prompt for user's full name
    intFoundSpace = strFullName.find(' ')   # find the first space in the full name
    strFirstName = strFullName[:intFoundSpace]  # get just the first name
    print('Hello there,', strFirstName + ', and welcome to CPT-135!')  # review , vs. +
    print('The length of your full name is',str(len(strFullName)), 
          'characters long.')                   # str conversion
    print('Your last name in all uppercase is', 
          strFullName[intFoundSpace + 1:].upper()) # slicing and upper function
    fncSeparateAndPause()                       # call function defined below
    
    print('This next section shows working with a List.')
    lstMixedValues = [10,13,'Some Text',41,3,False]  # notice ints, text and booleans all together
    print('The original list looks like this:',lstMixedValues)
    print('The value at index 0 is', lstMixedValues[0]) # notice index starts at 0
    print('The value at index 2 is', lstMixedValues[2]) # referencing specific items
    print('The last value is', lstMixedValues[len(lstMixedValues) - 1]) # notice the len function
    lstMixedValues.append(297)        # appends a value to the end of the list
    print('The list after appending a new value',lstMixedValues)
    lstMixedValues.pop(2)               # pops (deletes) an item from the specified index
    print('The list after \'pop\'-ing the value at index position 2', lstMixedValues)
    lstMixedValues.remove(False)   # removes (deletes) the first matching item found in the list
    print('The list after removing a found value', lstMixedValues)
    print('If a list contains only numeric values, then the sum, min, and max')
    print('  functions can be used on the list...')
    print(f'The sum, min, and max of the list are '
          f'{sum(lstMixedValues)}, {min(lstMixedValues)}, {max(lstMixedValues)}',
          'respectively.')      # notice split formatting.  Also, only works on all numbers
    fncSeparateAndPause()

    print('This next section will explore some Dictionary basics...')
    dictMenu = {}
    print('The menu is currently:', dictMenu)
    dictMenu = {"pizza": 12.99, "salad": 8.99, "veggie burger": 9.18, "soft drink": 3.99}
    print('The updated menu:', dictMenu)
    print('A veggie burger costs:',dictMenu['veggie burger'])
    print('A soft drink costs:',dictMenu['soft drink'])
    dictMenu['fries'] = 4.75
    print('After adding a menu item, the menu now looks like:',dictMenu)
    print('The salads aren\'t selling so well...')
    del dictMenu['salad']
    print('The menu after removing the salad item:', dictMenu)
    fncSeparateAndPause()
    print('Finally, let\'s order some food from our menu and make a receipt...')
    print(' We will order 2 pizzas, 2 veggie burgers, 4 soft drinks, and 2 fries.')
    intPizzaQty = 2
    intVegBrgrQty = 2
    intDrinkQty = 4
    intFryQty = 2
    fltPizzaTotal = (intPizzaQty * float(dictMenu["pizza"]))
    fltVegBrgrTotal = (intVegBrgrQty * float(dictMenu["veggie burger"]))
    fltDrinkTotal = (intDrinkQty * float(dictMenu["soft drink"]))
    fltFryTotal = (intFryQty * float(dictMenu['fries']))
    print('-' * 35)
    print('Qty.\tItem\tPrice\tExt. Price')
    print(f' {intPizzaQty}'
          f'\tPizza'
          f'\t{dictMenu["pizza"]:>5}'   # :>5 forces a right-align within 5 characters
          f'\t{fltPizzaTotal:>10.2f}')   # :>10.2f forces right-align within 10 char and 2 places
    print(f' {intVegBrgrQty}'
          f'\tVegBrgr'
          f'\t{dictMenu["veggie burger"]:>5}'
          f'\t{fltVegBrgrTotal:>10.2f}')
    print(f' {intDrinkQty}'
          f'\tDrinks'
          f'\t{dictMenu["soft drink"]:>5}'
          f'\t{fltDrinkTotal:>10.2f}')
    print(f' {intFryQty}'
          f'\tFries'
          f'\t{dictMenu["fries"]:>5}'
          f'\t{fltFryTotal:>10.2f}')
    print(f'TOTAL\t\t\t{(fltPizzaTotal + fltVegBrgrTotal + fltDrinkTotal + fltFryTotal):>10.2f}')

def fncSeparateAndPause():  # defines a callable function (covered in a future week in detail)
    print ('-' * 80)        # prints a repeated line of 80 - characters
    input('Hit the Enter Key to continue...')   # input with no assignment goes nowhere!

main()      # run the defined main function