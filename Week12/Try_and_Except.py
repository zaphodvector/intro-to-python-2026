"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week12_Text_Sample
    Author:	Ed Weber
    Language:	Python
    Date:	2025-01-08
    Purpose:	The purpose of this program is to demonstrate writing and using the try/catch
                blocks to control error handling.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2025-01-08	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
blnCatchALLErrors = True
def main():
    strMsg = 'The purpose of this program is to explore what happens to programs during\n'
    strMsg += '  runtime errors by allowing the user to control how and when certain types\n'
    strMsg += '  of errors will be handled by Python vs. when they will be handled by the\n'
    strMsg += '  programmer themselves.\n\n'
    strMsg += "To kick things off, we're going to implement a generic 'Handler-of-all-Errors'\n"
    strMsg += "  and temporarily turn on this 'global' error handling."
    
    global blnCatchALLErrors    # set up a reference to the global variable (with global scope)
    blnCatchALLErrors = True    # turn off system catching and turn ours on
    fncPauseAndReflect(strMsg)

    intLoopCount = 0        # set up a counter to see how many times we stay in the loop
    while True:             # place this block in an infinite loop that must be 'broken' out of
        intLoopCount += 1
        strAgain = ''
        if(intLoopCount > 1):
            strAgain = '... again...'
        strMsg = f"Now, let's try to break the program{strAgain}!\n"
        strMsg += "  I am going to prompt you to answer a question with either a 1 or a 2 only.\n"
        strMsg += "  (... you'd be surprised how many users don't read and don't follow directions!)\n"
        strMsg += f"    (BTW, you have now been in this loop {intLoopCount} times...)\n\n"
        strMsg += "Here comes your prompt:"
        print(strMsg)   # need to print the message without waiting...
        blnUserAnsweredValidly = fncTurnErrorHandlerONorOFF()
        if blnUserAnsweredValidly:  # only is set true if the user gave valid input
            break       # get out of the infinite loop.

    # if we've made it this far, the global handler has been set and we can test some more
    # Now let's force an index out of range error
    strMsg = 'To continue, we will try to force some other runtime errors to\n'
    strMsg += '  see how both PYTHON and our own error handler deals with the errors.\n'
    lstFav_Colors = ['Blue', 'Green', 'Red', 'Purple', 'Yellow', 'Pink', 'Orange']
    strMsg += '\nConsider this list of favorite colors named \'lstFav_Colors\':\n'
    strMsg += str(lstFav_Colors)
    strMsg += '\nA common error is trying to reference a list using an invalid index.\n'
    strMsg += '  This often happens when new programmers forget that the index starts at 0!\n'
    strMsg += '  A typical runtime error can occur when coding a statement like:\n'
    strMsg += '       print(lstFav_Colors[len(lstFav_Colors)])'
    fncPauseAndReflect(strMsg)

    if blnCatchALLErrors:
        # our error handler will handle this error!
        try:
            print(lstFav_Colors[len(lstFav_Colors)])
        except Exception as thisExceptionEvent:
                fncHandlerOfAllErrors(thisExceptionEvent)
    else:
        # Python will crash without a program-defined error handler!
        print(lstFav_Colors[len(lstFav_Colors)])
    fncPauseAndReflect()

    # Now let's re-ask the user if they want to set the state of the error handler
    # we need to do this so we can handle some and not handle others...
    print('\nPlease reselect the state of the Error Handling...\n')
    while True:
        blnUserAnsweredValidly = fncTurnErrorHandlerONorOFF()
        if blnUserAnsweredValidly:
            break
    # Now let's force a name error
    strMsg = f'\nStill using the list named \'lstFav_Colors\':\n'
    strMsg += str(lstFav_Colors)
    strMsg += '\nAnother common error is trying to reference a variable (or function or Class)\n'
    strMsg += '  using an incorrect name.  This happens more often in weakly typed languages\n'
    strMsg += '  such as Python.  This error can occur when coding a statement like:\n'
    strMsg += '       print(lstFav_Colors[len(lstFav_Color)])\n'
    strMsg += '  (Note: a GOOD IDE can catch many of these while you are coding!)'
    fncPauseAndReflect(strMsg)
    if blnCatchALLErrors:
        # our error handler will handle this error!
        try:
            print(lstFav_Colors[len(lstFav_Color)]) # type: ignore
        except Exception as thisExceptionEvent:
                fncHandlerOfAllErrors(thisExceptionEvent)
    else:
        # Python will crash without a program-defined error handler!
        print(lstFav_Colors[len(lstFav_Color)]) # type: ignore

    # Now let's re-ask the user if they want to set the state of the error handler
    # we need to do this so we can handle some and not handle others...
    print('\nPlease reselect the state of the Error Handling...\n')
    while True:
        blnUserAnsweredValidly = fncTurnErrorHandlerONorOFF()
        if blnUserAnsweredValidly:
            break
    # Now let's force a key error
    dictFruits = {'apples':10,'bananas':7,'organges':0}
    strMsg = f'\nFinally, using the dictionary named {dictFruits}:\n'
    strMsg += str(dictFruits)
    strMsg += '\nAnother common error is trying to reference a non-existent key in \n'
    strMsg += '  a dictionary.  This can happen when a program tries to pop or del (remove)\n'
    strMsg += '  a dictionary entry by name but the key name is not in the dictionary.\n'
    strMsg += '  This error can occur when coding a statement like:\n'
    strMsg += "       strDeletedItem = dictFruits.pop('pears')\n"
    strMsg += '  (Note:  This is very hard to catch when the key to be popped is not a literal\n'
    strMsg += '          but rather a value stored in a variable!)'
    fncPauseAndReflect(strMsg)
    if blnCatchALLErrors:
        # our error handler will handle this error!
        try:
            strDeletedItem = dictFruits.pop('pears')
        except Exception as thisExceptionEvent:
                fncHandlerOfAllErrors(thisExceptionEvent)
    else:
        # Python will crash without a program-defined error handler!
        strDeletedItem = dictFruits.pop('pears')
    fncPauseAndReflect("The program has ended.\nPlease run again using different answers!")

def fncTurnErrorHandlerONorOFF():
    '''This function turns the blnCatchALLErrors ON or OFF and
    returns True if successfully executed or returns False
    if failed due to some input error.
    '''
    global blnCatchALLErrors
    strPrompt = '  Please enter a 1 to turn ON the generic error handler\n'
    strPrompt += '    or enter a 2 to turn OFF the generic error handler:  '
    try:
        intWhichChoice = int(input(strPrompt))
        # if wrong type is entered, a TypeError will be raised
        if(intWhichChoice == 1):
            blnCatchALLErrors = True
            print('#' * 80)
            print('You have turned the global error handler ON!')
            print('  The program will handle any runtime errors!')
            print('#' * 80)
            return True
        elif(intWhichChoice == 2):
            blnCatchALLErrors = False
            print('#' * 80)
            print('You have turned the global error handler OFF!')
            print('  PYTHON will resume control to handle any runtime errors!')
            print('#' * 80)
            return True
        else:
            # the type is correct (i.e. an int), but the value is not in my required range
            raise ValueError('Invalid integer entered - (Not 1 or 2 only!)')
    except Exception as thisExceptionEvent:
        fncHandlerOfAllErrors(thisExceptionEvent)
 

def fncStatusOfErrorHandler():
    '''This function returns the status of the global Error Handler boolean'''
    global blnCatchALLErrors
    strStatus = 'OFF'
    if (blnCatchALLErrors):
        strStatus = 'ON'
    return f'The global error handler is turned: ' + strStatus + '\n'

def fncHandlerOfAllErrors(ErrorEvent):
    print('=' * 80)
    print(f'Error Type Thrown: {type(ErrorEvent).__name__}\n  Details: {ErrorEvent}')
    print(f'I got it handled... No worries!')
    print('=' * 80)

def fncPauseAndReflect(strMsg = '',sep='-',rpt=80):
    '''Function to allow a message to be displayed after a configurable separator line.
    Then, waits for the user to press the enter key before returning.
    '''
    print(sep * rpt)
    print(strMsg)
    input('Press the Enter Key when ready to continue...')

if (__name__) == '__main__':
    main()