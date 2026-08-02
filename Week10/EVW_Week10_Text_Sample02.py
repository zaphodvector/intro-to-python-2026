"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week10_Text_Sample02
    Author:	Ed Weber
    Language:	Python
    Date:	2025-01-06
    Purpose:	The purpose of this program is to show how one program can import, reference
                and use the code developed in another program.  Some of this material will be
                covered in a future week.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2025-01-06	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import types            # needed to test if a name found is a function name or not
from EVW_Week10_Text_Sample01 import *    #  adding in all of the definitions from the first file
strMsg = 'This function (fncPauseAndReflect) is defined in the other file but is being used here!'
fncPauseAndReflect(strMsg)
print('Now, we will use the dir() command to show all of the objects defined in the current space.')
print(dir())
strMsg = 'Now, let\'s explore how the help built-in function will show us the '
strMsg += 'documentation from each function if the function is properly structured.'
fncPauseAndReflect(strMsg)
lstMyFunctionNames = [strName for strName in dir() if
    strName.startswith('fnc') and isinstance(globals().get(strName), types.FunctionType)]
blnStayHere = True
strMsg = 'The global variables have been parsed and a new list containing only our own\n'
strMsg += 'functions names (beginning with fnc) has been extracted.\n\n'
strMsg += 'Does this help to reinforce some value in having consistent function and variable names?'
fncPauseAndReflect(strMsg)
while blnStayHere: 
    strUserPrompt = 'Please select which function to get help about...'
    strFncChosen = fncCreateMenuOptions(lstMyFunctionNames,strUserPrompt)
    if strFncChosen == 'Invalid':
        fncPauseAndReflect('The entry you made was invalid.')
        blnStayHere = True
    elif strFncChosen != 'Cancel':   # valid option selected
        blnStayHereForOption = False
        print('-' * 80)
        print(f'You requested to see the help for the function ({strFncChosen}).')
        print(help(globals()[strFncChosen]))
        fncPauseAndReflect()
        blnStayHere = True
    else:            # strUpdateOptionChosen == 'Cancel'
        blnStayHere = False

strMsg = 'This program showed how modules call and reference each other.\n'
strMsg += 'This information will be covered in greater detail in an upcoming week.'
fncPauseAndReflect(strMsg)