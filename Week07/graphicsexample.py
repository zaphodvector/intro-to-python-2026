"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week07_Graphics_Sample
    Author:	Ed Weber
    Language:	Python
    Date:	2025-01-03
    Purpose:	The purpose of this program is to use graphics to explore more string functions.
                Also included here are some preview items that will be covered in upcoming
                classes.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2025-01-03	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *

# create global variables
intMouseX = 0       # X where the mouse was last clicked
intMouseY = 0       # Y where the mouse was last clicked    
blnKeepRunning = True   # sentinel to keep in main loop until Quit button clicked
intWhichStep = 1    # counter to control what step we are on so what to draw in the window
blnStringButtonsAreDrawn = False    # boolean to control only drawing String Buttons one time
txtUserPhrase = ''  # The user's entered phrase
strErrorMsg = ''    # A string to hold error messages

# Create the window
win = GraphWin("String Manipulation and Future Topics", 500, 500)
txtInstructions = '\n\n\nThis program will let you specify a phrase'
txtInstructions += '\nthen click different buttons to manipulate'
txtInstructions += '\nthe phrase in different ways.  It also'
txtInstructions += '\ndemonstrates a number of future topics as a preview.'
txtInstructions += '\n\n\n\n'
txtDisplayWindow = Text(Point(250,190),txtInstructions)
txtDisplayWindow.draw(win)


# Create the generic button components (Rectangle and Text)
rctButton = Rectangle(Point(0, 0), Point(100, 40))
rctButton.setFill('white')  # Initial color of the original button
rctButton.setWidth(2)
rctButton.setOutline('Black')
txtButtonLabel = Text(Point(50, 18), "Click Me")

# Group the button components into a list
objBlankButton = [rctButton, txtButtonLabel]

# Define the different buttons needed for each real button
btnButtonList = ["Update", "Quit", "Split", "Upper", "Title", "Lower", "Replace"]

# Define the text phrase entry field
txtPhraseEntry = Entry(Point(250,300),50)
txtPhraseEntry.setFill('Yellow')
txtPhraseEntry.setTextColor('black')
txtPhraseEntry.setText('Please enter a phrase here...')

def fncCreateAllButtons(btnGroup, lstAllButtons):   # new concept not covered yet, parameters
    # Create a dictionary of all buttons that will be ButtonName: ButtonGroup
    dictAllButtons = {}
    for key in lstAllButtons:  # Iterate over each button name in lstAllButtons
        # Clone each object in the group (Rectangle and Text)
        clonedButton = [node.clone() for node in btnGroup]
        dictAllButtons[key] = clonedButton  # Store the list of cloned components in the dictionary with corresponding name
    return dictAllButtons       # new concept not covered yet - the return command

# Create clones of the generic button and store them in a dictionary
dictAllButtons = fncCreateAllButtons(objBlankButton, btnButtonList)

def fncUpdateButton(strWhichButton,blnDrawit=True,
    dX=0,dY=0,strNewButtonColor="salmon",strNewTextColor="black",
    strNewText="Click Me!"):
    # using the dictionary of all buttons and which button we are working with...
    #  turn button on or off based on blnDrawIt
    #  move button dX and dY if drawing it or 0,0 otherwise
    #  set color to strColor or white
    #  set text to new text or default
    for node in dictAllButtons[strWhichButton]:
        node.move(0,0)      # reset to home
        node.move(dX,dY)    # move to new location relative to home
    dictAllButtons[strWhichButton][0].setFill(strNewButtonColor)
    dictAllButtons[strWhichButton][1].setTextColor(strNewTextColor)
    dictAllButtons[strWhichButton][1].setText(strNewText)
    if blnDrawit:
        for node in dictAllButtons[strWhichButton]:
            node.draw(win)  # draw it
    else:
        for node in dictAllButtons[strWhichButton]:
            node.undraw()  # draw it

def fncGetMouseClick():
    #  gets the mouse click and set the point where the mouse was clicked
    #  so that now we can check if the click was on a button we care about
    global intMouseX, intMouseY
    ptThisPoint = win.getMouse()
    intMouseX = ptThisPoint.getX()
    intMouseY = ptThisPoint.getY()

def fncQuitClicked():
    # check if this particular click was on the Quit button
    global intMouseX, intMouseY, blnKeepRunning
    if (390 <= intMouseX <= 490) and (450 <= intMouseY <= 490):
        # the QUIT button WAS clicked!
        blnKeepRunning = False

def fncDrawStringButtonsOneTime():
    global blnStringButtonsAreDrawn
    fncUpdateButton("Split",True,50,350,"cyan","black","Split")
    fncUpdateButton("Upper",True,200,350,"greenyellow","black","Upper")
    fncUpdateButton("Title",True,350,350,"navy","yellow","Title")
    fncUpdateButton("Lower",True,125,400,"chocolate","black","Lower")
    fncUpdateButton("Replace",True,275,400,"darkgreen","yellow","Replace")
    dictAllButtons["Update"][1].setText('Update')
    blnStringButtonsAreDrawn = True

def fncUpdateClicked():
    # check if this particular click was on the Update button
    global intMouseX, intMouseY, intWhichStep, \
        blnStringButtonsAreDrawn, txtUserPhrase, strErrorMsg
    if (200 <= intMouseX <= 300) and (450 <= intMouseY <= 490):
        # the UPDATE button WAS clicked!
        strStep1 = 'Please type in a phrase and then click\n'
        strStep1 += 'the Update button.  The phrase should be\n'
        strStep1 += 'a minimum of two words separated by a space.\n'
        strStep1 += 'Also, the phrase will be limited to 50 characters.'
        dictAllButtons["Update"][1].setText('Update')
        strTextOrigPhrase = "Original Phrase:\n" + txtUserPhrase
        match intWhichStep:
            case 1:
                # first time clicking update
                txtPhraseEntry.draw(win)
                txtDisplayWindow.setText(strStep1)
                intWhichStep += 1
            case 2:
                # phrase entered (or not) so validate and stay here or move on...
                txtUserPhrase = txtPhraseEntry.getText().strip()
                if txtUserPhrase.count(' ') < 1:
                    strErrorMsg = "You did not type a phrase of at least two words!\n\n"
                    strErrorMsg += strStep1
                    txtDisplayWindow.setText(strErrorMsg)
                elif len(txtUserPhrase) > 50:
                    strErrorMsg = "Your phrase is greater than 50 characters!"
                    strErrorMsg += "\n (" + str(len(txtUserPhrase)) + ")\n\n"
                    strErrorMsg += strStep1
                    txtDisplayWindow.setText(strErrorMsg)
                else:
                    intWhichStep += 1
                    txtPhraseEntry.undraw()
                    if not blnStringButtonsAreDrawn:
                        fncDrawStringButtonsOneTime()
                    fncUpdateButton("Update",False)
                    strTextOrigPhrase += '\n' + txtUserPhrase + '\n'
                    txtDisplayWindow.setText(f'{strTextOrigPhrase}\n')
            case _:
                print("FAILURE - UNKNONW STEP!")

def fncWhichStringFunction():
    # check if this particular click was on a String Function button
    global intMouseX, intMouseY, txtUserPhrase
    strTextOrigPhrase = "Original Phrase:\n" + txtUserPhrase + '\n\n'
    strFuncDescription = ''
    strManipulateString = ''
    if (50 <= intMouseX <= 150) and (350 <= intMouseY <= 400):
        # the Split button WAS clicked!
        strFuncDescription = 'The split function will split a string using\n'
        strFuncDescription += 'the specified separator (or a space as the default.)\n\n'
        strManipulateString = txtUserPhrase.split()
    if (200 <= intMouseX <= 300) and (350 <= intMouseY <= 400):
        # the Upper button WAS clicked!
        strFuncDescription = 'The upper function will convert a string to\n'
        strFuncDescription += 'all upper case (ignoring punctuation and numbers.)\n\n'
        strManipulateString = txtUserPhrase.upper()
    if (350 <= intMouseX <= 450) and (350 <= intMouseY <= 400):
        # the Title button WAS clicked!
        strFuncDescription = 'The title function will convert a string to\n'
        strFuncDescription += 'Title Case (captializing each new word.)\n\n'
        strManipulateString = txtUserPhrase.title()
    if (125 <= intMouseX <= 225) and (400 <= intMouseY <= 450):
        # the lower button WAS clicked!
        strFuncDescription = 'The lower function will convert a string to\n'
        strFuncDescription += 'lower case (ignoring punctuation and numbers.)\n\n'
        strManipulateString = txtUserPhrase.lower()
    if (275 <= intMouseX <= 375) and (400 <= intMouseY <= 450):
        # the replace button WAS clicked!
        strFuncDescription = 'The replace function will convert a string by\n'
        strFuncDescription += 'replacing every found substring with the specified replacement.\n\n'
        strManipulateString = txtUserPhrase.replace(' ','+')

    strFinalMsg = strTextOrigPhrase + strFuncDescription + 'Results: \n' + str(strManipulateString)
    txtDisplayWindow.setText(strFinalMsg)

fncUpdateButton("Update",True,200,450,"orange","black","Click to Start")
fncUpdateButton("Quit",True,390,450,"darkred","white","Quit")
while (blnKeepRunning):
    fncGetMouseClick()
    fncQuitClicked()
    fncUpdateClicked()
    if intWhichStep > 2:
        fncWhichStringFunction()