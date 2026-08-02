"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week10_Text_Sample01
    Author:	Ed Weber
    Language:	Python
    Date:	2025-01-06
    Purpose:	The purpose of this program is to demonstrate various functions including:
                 - defining function names with and without parameter lists
                 - defining function bodies which use parameters
                 - defining function which access values within its own scope local as well
                   as globally defined items
                 - returning values from called functions back to the calling code
                 - ... other function definition and usage items.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2025-01-06	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import random   # this is done at the global level so that it is available anywhere needed
def main():     # define the main function for this script with no parameters
    print("Hello World!")   
    fncPauseAndReflect()        # calls the function named fncPauseAndReflect with no parameters
    fncSeeWhoIsHere()           # calls the function named fncSeeWhoIsHere with no parameters
    dictTheMenu = fncSetMenu()  # calls the function named fncSetMenu() and returns a dictionary
    print('The final Menu is now as follows:')
    fncShowCurrentMenu(dictTheMenu)
    fncPauseAndReflect("There is more to do with this program... but we'll stop here now.")

def fncSetMenu():
    '''This function fncSetMenu() creates the default menu items for the cafeteria.
    The return value is a dictionary in the structure of {meal_type:{item:price}}
    where meal_type is one of 'Breakfast', 'Lunch', 'Dinner', 'Sides' and 'Drinks' 
    and where item:price is a dictionary of items and their prices within each meal_type.
    
    Also in this function is the ability to add or remove menu items.
    
    '''
    dictMenu = {}
    dictBreakfast = {'Pancakes':3.39, 'Scrambled Eggs':2.99, 'French Toast': 2.49}
    dictMenu['Breakfast'] =(dictBreakfast)
    dictLunch = {'Pizza':7.99, 'Veggie Burger':6.99, 'Garden Salad': 5.59}
    dictMenu['Lunch'] =(dictLunch)
    dictDinner = {'Taco Bar':7.99, 'Vegetable Fried Rice':5.99, 'Pasta Con Broccoli': 7.49}
    dictMenu['Dinner'] =(dictDinner)
    dictSides = {'Tater Tots':4.49, 'Steamed Veggies':5.29, 'Soup du Jour': 3.89}
    dictMenu['Sides'] =(dictSides)
    dictDrinks = {'Soft Drink':2.99, 'Fruit Juice':3.99, 'Coffee': 2.79}
    dictMenu['Drinks'] =(dictDrinks)
    blnStayHere = True
    while blnStayHere:
        fncShowCurrentMenu(dictMenu)    # call the function passing the menu dictionary
        blnStayHere = fncAreMoreMenuChangesNeeded()
        if blnStayHere:
            strWhichMealType = fncShowMealTypeSelector()    # get meal type or 'Cancel'
            # change meal type items or 'Cancel'
            blnMenuChangesWereMade = False  # assume no changes will be made
            blnMenuChangesWereMade = fncShowAndChangeMealTypeItems(dictMenu, strWhichMealType)
            if blnMenuChangesWereMade:
                blnStayHere = True
            else:
                blnStayHere = False
    return dictMenu

def fncShowAndChangeMealTypeItems(dictMenu, strPreviousOptionSelected):
    '''This function receives the current Menu (as a dictionary) and the
    previous option selected by the user.  If the previous option was 'Cancel'
    the user is attempting to abandon this action.  If the user isn't trying
    to Cancel out of this function, then the previous option will be the
    menu meal type that the user wants to see and update.

    The function will then prompt the user to either add/update or delete
    an existing menu item or Cancel out of this function.

    '''
    if strPreviousOptionSelected == 'Cancel':
        return False
    lstUpdateOptions = ['Add/Update Item','Delete Item']
    blnStayHereForOption = True
    while blnStayHereForOption: 
        strUpdateOptionChosen = fncCreateMenuOptions(lstUpdateOptions, 
            'Please choose what type of update you need to make.')
        if strUpdateOptionChosen == 'Invalid':
            blnStayHereForOption = True
        else:   # valid option selected
            blnStayHereForOption = False
    if strUpdateOptionChosen == 'Cancel':
        return False    # user doesn't want to continue with this
    print('-' * 80)
    print(f'Here are the current menu items in {strPreviousOptionSelected}.')
    dictCurrentMenuItems = dictMenu[strPreviousOptionSelected].items()
    for strItemName, fltItemPrice in dictCurrentMenuItems:
        print(f'{strItemName:>20} {fltItemPrice:>5}') 
    strUpdateItemName = input('\nPlease enter the Item Name that you need to add/update/delete. ')
    if strUpdateOptionChosen == 'Delete Item':  # attempt to delete the key supplied
        delItem = dictMenu[strPreviousOptionSelected].pop(strUpdateItemName, 'Invalid Key')
        if delItem == 'Invalid Key':  # user had a typo
            strError = f'The item you entered ({strUpdateItemName}) does not exist in the menu'
            strError += 'so it could not be deleted.  No menu changes were made.'
        else:     # the item was removed - now see if there are any left
            strError = f'The item you entered ({strUpdateItemName}) was "popped" from the menu.'
            if (len(dictMenu[strPreviousOptionSelected].keys()) == 0):
                strError += f'The menu for the meal type of {strPreviousOptionSelected} has no items.'
    else:   # user wants to add/update the menu item
        fltUpdateItemPrice = input(f'\nPlease enter the updated price for the item {strUpdateItemName}: ')
        fltUpdateItemPrice = fltUpdateItemPrice.strip() # remove any extra spaces
        strError = ''       # empty out the error message.
        if(fltUpdateItemPrice.count('.') >=0 and fltUpdateItemPrice.count('.') < 2):
            # make sure this float has either 0 or 1 period
            strRestOfUpdateItemPrice = fltUpdateItemPrice.replace('.','') # remove the period 
            if(strRestOfUpdateItemPrice.isdigit()):
                fltUpdateItemPrice = round(float(fltUpdateItemPrice),2)  # we have a valid float
                if fltUpdateItemPrice <= 0.01:
                    strError = f'The updated price cannot be less than 0.01!'
            else:
                strError = f'The updated price you entered ({fltUpdateItemPrice}) is '
                strError += f'NOT a valid price.  A valid price must be a positive numeric '
                strError += f'value with at most one decimal point.'
        else:
            strError = f'The updated price you entered ({fltUpdateItemPrice}) is '
            strError += f'NOT a valid price.'
        if strError != '':      # Some error condition exits
            fncPauseAndReflect(strError)
        else:
            dictMenu[strPreviousOptionSelected][strUpdateItemName] = float(fltUpdateItemPrice) 
            strError = f'The item you entered ({strUpdateItemName}) was added/updated with a price of '
            strError += f'{fltUpdateItemPrice}.'
    fncPauseAndReflect(strError)
    return True

def fncShowMealTypeSelector():
    '''This function shows the possible meal types for the menu and
    asks the user to select which meal type they need to change.

    '''
    blnStayHere = True
    lstMealTypes = ['Breakfast','Lunch','Dinner','Sides','Drinks']
    while blnStayHere:
        strOptionChosen = fncCreateMenuOptions(lstMealTypes, 
            'Please choose the Menu Type to update.')
        if strOptionChosen == 'Invalid':
            blnStayHere = True
        else:
            blnStayHere = False
    return strOptionChosen

def fncCreateMenuOptions(lstOptionList, strMenuOptionPrompt):
    '''This function accepts an option list and a user prompt
    and then creates a serialized menu from 1 to n where n is
    the length of items in the menu list.  The function then
    appends a 0 entry to signify the user wants to cancel
    and choose none of the entries.

    '''
    print(strMenuOptionPrompt)
    for intSelection, strOption in enumerate(lstOptionList,start = 1):
        print(f'{intSelection:>3}  {strOption}')
    print(f'{0:>3}  Cancel Request')
    strUserInput = input('Please select a valid option: ')
    if strUserInput.isdecimal():
        if int(strUserInput) == 0:
            return 'Cancel'
        elif 0 < int(strUserInput) <= len(lstOptionList):
            return lstOptionList[int(strUserInput) - 1]
        else:
            return 'Invalid'
    else:       # not a decimal entered
        return 'Invalid'


def fncAreMoreMenuChangesNeeded():
    '''This is a small looping function to ask the user if any 
    additional menu changes are needed.  Returns True or False
    '''
    strUserAnswer = input(f"Are any more menu changes needed (y/n)? ")
    if(strUserAnswer.lower().strip() == 'y'):
        return True     # we will loop again
    else:
        return False    # we are done building the menu
    

def fncShowCurrentMenu(dictMenu):
    '''This function shows the current cafeteria menu broken out by
    meal type and having the menu items and their prices printed individually.
    '''
    print('*' * 80)             # print a separator line
    print('Here is the current full menu:')
    for strMealType, dictMenuItems in dictMenu.items():
        print(f' {strMealType}')     # print each meal type
        print('=' * 30)
        for dictItem, dictPrice in dictMenuItems.items():    # for each dict of items/prices
            print(f'{dictItem:>20} {dictPrice:>5.2f}')    # print each item/price
    fncPauseAndReflect()

def fncSeeWhoIsHere():
    '''This function prompts for the user names (separated by commas) for
    the folx who are here running the program.  It then runs some nested functions
    including: PauseAndReflect, GreetFolx, and ShouldIRepeatThisFunction
    It stays looping in this function for as long as the user says that the program
    should repeat this function.

    '''
    blnStayHere = True      # set a loop sentinel
    while blnStayHere:      # repeat this loop until the bln goes False
        strPrompt = "Who is running this program? (Please enter names separated with commas):\n"
        strWhoIsRunning = input(strPrompt)
        strMessage = 'When the Enter key was pressed the input string returned was\n'
        strMessage += f'  {strWhoIsRunning}\n'
        strMessage += f'  When this input is processed, any comma-separated values\n'
        strMessage += f'  will get parsed as individual arbitrary arguments to the fncGreetFolx().'
        fncPauseAndReflect(strMessage)   # this function call is nested
        fncGreetFolx(strWhoIsRunning)                       # this function call is nested
        strError = 'Notice how the output of the function depends on the function call!'
        fncPauseAndReflect(strError,'^',80)
        fncWhichFunctionName = fncSeeWhoIsHere # create a variable pointing to the function itself
        blnStayHere = fncShouldIRepeatThisFunction(fncWhichFunctionName)

def fncGreetFolx(*args):  # define a function that takes 0 to many optional arguments
    '''This function demonstrates how the same function can handle and process
    and indeterminate (arbitrary) list of potential parameters.

    '''
    print('Hello ',end = '')
    if len(args) > 0 and args[0] != "":     #test for 1 or more args with the first one not empty
        for strOnePerson in args:
            print(strOnePerson, end=', ')
        print('and anyone else I may have missed!')
    else:
        print('Visitor!')

def fncShouldIRepeatThisFunction(fncFunctionToRepeat = None):
    '''This function determines whether or not the user want the function name 
    that was passed in as a parameter to be repeated.  The function 
    returns true or false to update the sentinel for the calling loop.
    
    '''
    # 
    if fncFunctionToRepeat == None:
        # this should NEVER happen because this function should only be called with a parameter
        strError = 'ERROR! This function should NEVER be called without a valid parameter!'
        strError += '\nAssuming a bad function call and returning False to break this loop.'
        fncPauseAndReflect(strError,'%',80,)
        return False
    #in the next line, the __name__ variable is a reserved variable name for every function
    strUserAnswer = input(f"Should I repeat the function {fncFunctionToRepeat.__name__} (y/n)? ")
    if(strUserAnswer.lower().strip() == 'y'):
        return True
    else:
        return False

def fncPauseAndReflect(strExtraMsg = '', strRptChar = "-",intNum2Rpt = 80):
    '''This function prints a separator line and any message passed into this
    function and then pauses until the user hits the enter key.

    '''
    # function is defined with three parameters with default values set
    print(strRptChar * intNum2Rpt)  # print the repeat character the specified number of times
    if(strExtraMsg != ''):
        print(strExtraMsg)
    input('Hit the Enter key to continue...')
    # returns nothing - a void function

if __name__ == '__main__':  # the only statement that directly executes in the script
    main()      # call the main() function with  no parameters