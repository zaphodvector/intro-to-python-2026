"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week06_Text_Sample
    Author:	Ed Weber
    Language:	Python
    Date:	2024-12-31
    Purpose:	The purpose of this program is to create examples of different kinds of looping
                including using sentinels or other loop controls.  Also an infinite loop will
                be shown with examples of breaking out of an infinite loop.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2024-12-31	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import random                   # will be used in several examples

def main():
    #WhileLoop_SentinelIsMissing()
    #ForLoopWithRangeAndBreak()
    #NestLoopsForMultipleChoice()
    BooleanSentinelLoop()

def WhileLoop_SentinelIsMissing():
    # looping using a while loop waiting for a sentinel to exist
    # Is in an infinite loop until the sentinel exists
    print('This loop iterates infinitely until a sentinel exists.')
    print('The sentinel will be simply 5 consecutive x\'s (xxxxx).')
    print('Please type anything at all and hit enter.  Type "xxxxx" when you are done.')
    sentinel = ''       # create an empty sentinel value
    intInputCount = 0
    while sentinel.lower() != 'xxxxx':   # handle the user typing in different cases...
        sentinel = input()
        intInputCount += 1              # count this input
        print(f'{intInputCount}: {sentinel}')
    print('+' * 70 + '\nThe sentinel (regardless of case sensitivity) was typed...')
    print(f'You input {intInputCount} total entries.')
    PauseToReflect()


def ForLoopWithRangeAndBreak():
    #  looping using a for loop with a range for iteration
    print('This loop iterates through up to 100 random numbers (i.e. range(100))')
    print('If a 0 or a 100 is randomly picked as the random number, then the ')
    print('{break} command will be issued to break out of the loop.')
    print('But if a 0 or a 100 is never picked, then the loop will end when')
    print('the full 100 random numbers have been chosen.')
    print('(Remember that ranges with only one value start at 0 and end before the last number!)')
    
    for myval in range(100):
        x = random.randint(0,100)       # get a new random #
        print(x,end = ', ')             # prints the number with a ', ' after words
        if((myval + 1) % 15 == 0):      # remember that iterations start at 0 with ranges
            print('')                   # forces a new line in the output
        if x in [0,100]:                # test for specifically a 0 or a 100
            break                       # breaks out of the active loop
    print(f'\nTotal loops: {myval + 1}')  # final message (remember + 1 because range starts at 0)
    PauseToReflect()

def BooleanSentinelLoop():
    print('''
This loop will flip a coin and keep looping infinitely
    until HEADS is flipped 10 times in a row.
To keep the user entertained, the output will show an * 
    for every 50 flips.
          ''')
    bln10Heads = False       # set up the sentinel
    intCountOfHeads = 0
    intTotalFlips = 0
    while not bln10Heads:
        intTotalFlips += 1          # always count the current flip
        if intTotalFlips % 50 == 0: # print an * for every 50 flips
            print('*', end = '')
        if intTotalFlips % 1000 == 0:    # print a new line for every 20 *s
            print()
        if(random.choice(['Heads','Tails']) == 'Heads'):
            intCountOfHeads += 1    # another heads was flipped
        else:
            intCountOfHeads = 0     # a tail resets the heads counter
        if intCountOfHeads >= 10:
            print("\nWHOO-HOO! Ten heads were flipped in a row!")
            print(f'It only took {intTotalFlips} total flips!')
            bln10Heads = True
    PauseToReflect()

def NestLoopsForMultipleChoice():
    print('This section will have nested loops.  In the outer loop, we will')
    print('  loop through 3 quiz questions.  In the inner loop, we will loop')
    print('  through 4 possible answers.')
    lstQuestions = range(1,4)       # create several questions
    lstAnswers = ['a','b','c','d']  # create answers a,b,c, and d
    for intOuterLoopCounter in lstQuestions:
        print(f'Question #{intOuterLoopCounter}: ')
        intAnswerCount = 0
        for intInnerLoopCounter in lstAnswers:
            intAnswerCount += 1
            print(f'\t{lstAnswers[intAnswerCount - 1]}) Possible answer #{intAnswerCount}...')
    PauseToReflect()

def PauseToReflect():
    print('-' * 80)
    print('Pause and reflect... then hit the Enter Key to Continue...')
    input()

main()