"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week07_Text_Sample
    Author:	Ed Weber
    Language:	Python
    Date:	2025-01-03
    Purpose:	The purpose of this program is to explore various string functions using a
                menu of options for the user to choose from.  Besides showing examples of the
                string functions themselves, this also shows a preview of some of the future
                topics to be covered including defining functions, variable scoping, handling
                long lines with continuation across lines and more... 
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2025-01-03	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import random
# define the global variables that the rest of the program will use
strWiseWords = '''True growth begins when you challenge your own assumptions, 
embrace learning with humility, and remember that even the 
smallest steps forward can lead to the greatest transformations.'''
lstStringFunctions = ['String length', 'String slicing',
    'Conversion to UPPER, lower, or Title Case',
    'String placement and formatting',
    'String replacement', 'Count substrings',
    'Find substring vs. substring membership',
    'Quit Program']
intLongestMenuItem = max(len(item)for item in lstStringFunctions)

strErrorMessage = ''            # message to user whenever there is an error
intUserMenuChoice = 0           # this will be the user's choice until they quit
blnFormattingMenu = False       # this will update the menu instead of the phrase

def main():
    global intUserMenuChoice, lstStringFunctions
    blnStayHere = True
    while blnStayHere:
        intPossibleChoices = len(lstStringFunctions)
        if intUserMenuChoice == intPossibleChoices:
            blnStayHere = False
        else:
            match intUserMenuChoice:
                case 1:
                    fncLengthFunction()
                case 2:
                    fncStringSlicing()
                case 3:
                    fncUPPERlowerTitleCase()
                case 4:
                    fncStringFormattingAndPlacement()
                case 5:
                    fncStringReplacement()
                case 6:
                    fncCountSubstrings()
                case 7:
                    fncFindVsIn()
                case _:
                    fncShowMenu()

def fncShowMenu():
    global strErrorMessage, intUserMenuChoice
    print('\n' * 80) # this will print 80 blank lines to 'clear the screen' from pervious output
    print('-' * 80) # this will be the top line for each new task
    print('Please consider these wise words:\n')
    print(strWiseWords)
    print(f'\n{"Option"}{"Function to Explore":^{(max(len(item)for item in lstStringFunctions))}}')
    for intIndex, strFunction in enumerate(lstStringFunctions):
        print(f'{intIndex + 1:^6}{lstStringFunctions[intIndex]}')
    print(f'\n{strErrorMessage}')
    strUserChoice = input('Please enter a menu choice: ')
    strErrorMessage = ''            # reset the error message
    if not (strUserChoice.isdigit()):
        strErrorMessage += 'Menu selection must be between 1 and ' + str(len(lstStringFunctions)) + '.'
        intUserMenuChoice = 0
    elif (int(strUserChoice) <= 0) or (int(strUserChoice ) > len(lstStringFunctions)):
        strErrorMessage += 'Menu selection must be between 1 and ' + str(len(lstStringFunctions)) + '.'
        intUserMenuChoice = 0
    else:
        intUserMenuChoice = int(strUserChoice)

def PauseAndReflect():
    print ('*' * 80)
    input('Please hit the Enter Key when ready to continue...')

def fncLengthFunction():
    global strWiseWords, intUserMenuChoice
    print('\n' * 80) # this will print 80 blank lines to 'clear the screen' from pervious output
    print('-' * 80) # this will be the top line for each new task
    print(f'{"Displaying the String Length Function":^60}')
    print(f'{"-------------------------------------":^60}')
    print(f'{"Original Phrase (strWiseWords)":^60}')
    print(strWiseWords)
    print('-' * 80)
    print(f"Function used:  len(strWiseWords)")
    print(f"This string has an original length of {str(len(strWiseWords))}.")
    print(f'Note that the length function for strings counts character (including)')
    print(f'  white spaces, punctuation, carriage returns and everything else!')
    print(f'Also note that the length function returns an integer, so it must be')
    print(f'  converted to a string in order to be printed.')
    PauseAndReflect()
    intUserMenuChoice = 0               # reset this for next user selection

def fncStringSlicing():
    global strWiseWords, intUserMenuChoice
    print('\n' * 80) # this will print 80 blank lines to 'clear the screen' from pervious output
    print('-' * 80) # this will be the top line for each new task
    print(f'{"Displaying the String Slicing Concept":^60}')
    print(f'{"-------------------------------------":^60}')
    print(f'{"Original Phrase (strWiseWords)":^60}')
    print(strWiseWords)
    print('-' * 80)
    print(f'{"String Slice Used":^30}{"Resulting String":^30}')
    print(f'{"strWiseWords[:30]":<30}{strWiseWords[:30]:<30}')
    print(f'{"strWiseWords[-30:]":<30}{strWiseWords[-30:]:<30}')
    print(f'{"strWiseWords[75:105]":<30}{strWiseWords[75:105]:<30}')
    print(f'{"strWiseWords[int(len(strWiseWords)/2)-15:int(len(strWiseWords)/2)+15]":<30}')
    print(f'{' ':<30}{strWiseWords[int(len(strWiseWords)/2)-15:int(len(strWiseWords)/2)+15]:<30}')
    PauseAndReflect()
    intUserMenuChoice = 0               # reset this for next user selection

def fncUPPERlowerTitleCase():
    global strWiseWords, intUserMenuChoice
    print('\n' * 80) # this will print 80 blank lines to 'clear the screen' from pervious output
    print('-' * 80) # this will be the top line for each new task
    print(f'{"Displaying the UPPER, lower, and Title Case Functions":^60}')
    print(f'{"-----------------------------------------------------":^60}')
    print(f'{"Original Phrase (strWiseWords)":^60}')
    print(strWiseWords)
    print('-' * 80)
    strWhichFunction = random.choice(['UPPER','lower','TitleCase'])
    print(f'{"Random choice between, \"UPPER|lower|TitleCase\" was "}{strWhichFunction}{"."}')
    print(f'{"Function being shown:":^60}')
    match strWhichFunction:
        case 'UPPER':
            print(f'{"strWiseWords.upper()":^60}')
            print(f'{strWiseWords.upper()}')
        case 'lower':
            print(f'{"strWiseWords.lower()":^60}')
            print(f'{strWiseWords.lower()}')
        case 'TitleCase':
            print(f'{"strWiseWords.title()":^60}')
            print(f'{strWiseWords.title()}')
        case '-':
            print('SERIOUS ERROR - Random Choice Failure!')
            exit()
    PauseAndReflect()
    intUserMenuChoice = 0               # reset this for next user selection

def fncStringFormattingAndPlacement():
    global lstStringFunctions, intUserMenuChoice
    print('\n' * 80) # this will print 80 blank lines to 'clear the screen' from pervious output
    print('-' * 80) # this will be the top line for each new task
    print(f'{"Displaying Formatting and Placement using the Menu":^60}')
    print(f'{"--------------------------------------------------":^60}')
    strWhichAlignment = random.choice(['Left','Right','Center'])
    print(f'{"Random choice between \"Left|Right|Center\" was "}{strWhichAlignment}{"."}')
    print(f'{"Option":^10}{"Function to Explore":^{(max(len(item)for item in lstStringFunctions))}}')
    match strWhichAlignment:
        case 'Left':
            print(f'{"{intIndex + 1:<10}":^10}',end = '')
            print(f'{"{lstSTringFunctions[intIndex]}":^50}')
            for intIndex, strFunction in enumerate(lstStringFunctions):
                print(f'{intIndex + 1:<10}{lstStringFunctions[intIndex]}')
        case 'Right':
            print(f'{"{intIndex + 1:>10}":^10}',end = '')
            print(f'{"{lstSTringFunctions[intIndex]}:>50":^50}')
            for intIndex, strFunction in enumerate(lstStringFunctions):
                print(f'{intIndex + 1:>10}{lstStringFunctions[intIndex]:>50}')
        case 'Center':
            print(f'{"{intIndex + 1:^10}":^10}',end = '')
            print(f'{"{lstSTringFunctions[intIndex]}:^50":^50}')
            for intIndex, strFunction in enumerate(lstStringFunctions):
                print(f'{intIndex + 1:^10}{lstStringFunctions[intIndex]:^50}')
        case '-':
            print('SERIOUS ERROR - Random Choice Failure!')
            exit()
    PauseAndReflect()
    intUserMenuChoice = 0               # reset this for next user selection

def fncStringReplacement():
    global strWiseWords, intUserMenuChoice
    print('\n' * 80) # this will print 80 blank lines to 'clear the screen' from pervious output
    print('-' * 80) # this will be the top line for each new task
    print(f'{"Displaying String Replacements":^60}')
    print(f'{"------------------------------":^60}')
    print(f'{"Original Phrase (strWiseWords)":^60}')
    print(strWiseWords)
    print('-' * 80)
    print('Replacing some key words with capitalized version for emphasis.')
    print('  Note: Working with a copy of the original so as not to corrupt original.')
    print(f'{"Command used:":^60}')
    print(f'{"strTempWords = strWiseWords"}')
    print(f'{"for strSpecialWord in ['begins', 'embrace learning', 'greatest transformations']:"}')
    print(f'{"    strTempWords = strTempWords.replace(strSpecialWord,strSpecialWord.upper())"}')
    print('-' * 80)
    strTempWords = strWiseWords
    for strSpecialWord in ['begins', 'embrace learning', 'greatest transformations']:
        strTempWords = strTempWords.replace(strSpecialWord,strSpecialWord.upper())
    print(strTempWords)
    print('-' * 80)
    PauseAndReflect()
    intUserMenuChoice = 0               # reset this for next user selection

def fncCountSubstrings():
    global strWiseWords, intUserMenuChoice
    print('\n' * 80) # this will print 80 blank lines to 'clear the screen' from pervious output
    print('-' * 80) # this will be the top line for each new task
    print(f'{"Displaying and Using Substring Counts":^60}')
    print(f'{"-------------------------------------":^60}')
    print(f'{"Original Phrase (strWiseWords)":^60}')
    print(strWiseWords)
    print('-' * 80)
    print(f'{"Length of original string:":<30}{str(len(strWiseWords)):>4}')
    print(f'{"Command used:":^60}')
    print('''    intCountOfVowels = 0
    for vowel in ['a','e','i','o','u']:
        intCountOfVowels += strWiseWords.lower().count(vowel)''')
    intCountOfVowels = 0
    for vowel in ['a','e','i','o','u']:
        intCountOfVowels += strWiseWords.lower().count(vowel)
    print(f'{"Count of vowels in string: "}{str(intCountOfVowels)}')
    print(f'{"Count of non-vowels (i.e. consonants, punctuations, spaces, etc.): "}', end='')
    print(f'{str(len(strWiseWords) - intCountOfVowels)}')
    PauseAndReflect()
    intUserMenuChoice = 0               # reset this for next user selection

def fncFindVsIn():
    global strWiseWords, intUserMenuChoice
    print('\n' * 80) # this will print 80 blank lines to 'clear the screen' from pervious output
    print('-' * 80) # this will be the top line for each new task
    print(f'{"Displaying Find Function vs. In Operator":^60}')
    print(f'{"----------------------------------------":^60}')
    print(f'{"Original Phrase (strWiseWords)":^60}')
    print(strWiseWords)
    print('-' * 80)
    print('strSearched.find(strSubstring):  Find finds the location of the found substring.')
    print("Command used: strWiseWords.lower().find('the ')")
    print(" finds the location of the first time the word the is found.")
    print(" Note: See the trailing space in the sought word?  Discuss why!")
    print(f"The word 'the' was found at position: {strWiseWords.lower().find('the ')}.")
    print('-' * 80)
    print('strSubstring in strSearched:  Returns a boolean (t/f) if the substring exists.')
    print("Command used: 'the ' in strWiseWords)")
    print(" returns a boolean (True or False) if the phrase exists in the string.")
    print(" Note: See the trailing space in the sought word?  Discuss why!")
    print(f"Is the word 'the' found in the Wise Words? {'the ' in strWiseWords}")
    PauseAndReflect()
    intUserMenuChoice = 0               # reset this for next user selection

main()