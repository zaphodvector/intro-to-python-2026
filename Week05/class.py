"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week05_Text_Sample
    Author:	Ed Weber
    Language:	Python
    Date:	2024-12-30
    Purpose:	The purpose of this program is to show examples of conditional logic 
                i.e. if-then-else and to explore comparison and membership operators.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2024-12-30	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
def main():
    print('Who\'s Hungry?!?!') # introduce the program
    dictMenu = {'pizza':12.25, 'veggie burger':7.50,    # create a dictionary for our menu
            'salad': 6.75, 'fries': 3.50,
            'drink': 2.75}
    print('Here is the menu and prices:\n',dictMenu)
    fltMoney = float(input('How much $ did you bring? ')) # get user input for$ did you bring? ')) # get user input for $
    if (fltMoney < min(dictMenu.values())):             # test $$$ compared to min price
        print('I\'m sorry, but you do not have enough money to spend!')  # if not enough $$$
        print('  Please come back when you have more funds!')
        exit()                                      # leave and process no more!

    BreakAndPause()                             # a repeatable function
   
    print ('Which menu item would you like? ')      # prompt the user for their selection
    strUserChoice = input()                         # get an answer
    if strUserChoice not in dictMenu:               # uses the membership operator 'in' and 'not'
        print(f'I\'m sorry, but we don\'t have any {strUserChoice}...')
        print('You have to make a valid menu selection only or we can\'t serve you!')
        exit()
    print(f'You requested {strUserChoice} which costs {dictMenu[strUserChoice]}...')
    print("  Let's see if this fits in your budget of available funds...")
    BreakAndPause()                             # a repeatable function
    if(dictMenu[strUserChoice] <= fltMoney):     # test if there is enough $$$
        print(f'Here is your {strUserChoice}!')
        print(f' Thank you for your payment of {dictMenu[strUserChoice]}.')
        print(f' You now have ${fltMoney - dictMenu[strUserChoice]:.2f} left.')
        exit()
    else:                        # only runs if the user doesn't have enough $ for that item
        print(f"You can't afford {strUserChoice}!")
        print("  Let me show you what you can afford right now...")
        if(dictMenu['pizza'] <= fltMoney):
            print('  ... you can afford a pizza.')
        if(dictMenu['veggie burger'] <= fltMoney):
            print('  ... you can afford a veggie burger.')
        if(dictMenu['salad'] <= fltMoney):
            print('  ... you can afford a salad.')
        if(dictMenu['fries'] <= fltMoney):
            print('  ... you can afford an order of fries.')
        if(dictMenu['drink'] <= fltMoney):
            print('  ... you can afford a drink.')
        # because we haven't learned looping and iteration yet, we need to end early
        print('Please return when you can make a better decision!') 
        exit()

def BreakAndPause():
    print('-' * 80)
    input('Press the Enter Key to continue...')
main()