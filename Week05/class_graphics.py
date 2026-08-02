"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week05_Graphics_Sample
    Author:	Ed Weber
    Language:	Python
    Date:	2024-12-30
    Purpose:	The purpose of this program is to introduce image graphics and UI controls
                and explore some additional functions of these objects.  Also, this will combine
                conditional logic to control branching while working with graphics.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2024-12-30	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *              # import the Zelle graphics library
def main():                         # define the main function to run
    win = GraphWin("Graphics with Image and GUI", 400, 400)
    txtGreetings = Text(Point(200,30),"Greetings in Graphics in Python!")   # create greeting
    txtGreetings.setFace("courier")
    txtGreetings.setSize(15)
    txtGreetings.setTextColor(color_rgb(50,0,0))
    txtGreetings.draw(win)
    txtInstructions = Text(Point(200,370),'(Click anywhere in the window to continue...)')
    txtInstructions.setFace("courier")
    txtInstructions.setTextColor("black")
    txtInstructions.setSize(10)
    txtInstructions.draw(win)
    win.getMouse() # pause for click in window

    linMyLine = Line(Point(2,45),Point(398,45))             # create and format line
    linMyLine.setFill("orange")
    linMyLine.setWidth(5)
    linMyLine.draw(win)
    txtInstructions.setText('A line has been created, formatted, and drawn...')
    win.getMouse() # pause for click in window

    cirMyCircle = Circle(Point(200,200),140)                # create and format circle
    cirMyCircle.setWidth(3)
    cirMyCircle.setFill("BlanchedAlmond")
    cirMyCircle.draw(win)
    txtInstructions.setText('A circle has been created, formatted, and drawn...')
    win.getMouse() # pause for click in window

    '''
        Attempt to create a reference to a .gif picture file 
        The file I use here is available in Canvas
        You can use your own file but this must be locatable on each machine
        at the time it is needed!
    '''
    strPictureFileName = '.\\media\\LimeCat.gif'          # I have a media folder 
    import os                           # import the os library so I can verify file existence
    if (not os.path.exists(strPictureFileName)):    # test if image can be found
        blnPictureExists = False            # for use later
        txtMissingFile = Text(Point(200,200), "The Image File does not exist!")
        txtMissingFile.draw(win)
        txtInstructions = txtMissingFile.getText()
    else:                               # the image was found...
        blnPictureExists = True         # for use later
        imgCat = Image(Point(200,200),strPictureFileName)  # place the image
        imgCat.draw(win)
        txtInstructions.setText('How would you caption this picture?')

    win.getMouse() # pause for click in window

    if (blnPictureExists):          # you don't have to say '... == True'
        imgCat.undraw()             # remove image from window
        cirMyCircle.undraw()        # remove the circle from window
        txtLabelForInput = Text(Point(150,150),"Enter your caption here:")
        txtLabelForInput.draw(win)
        inputBox = Entry(Point(200,200),30)
        inputBox.setTextColor("Yellow")
        inputBox.draw(win)
        txtInstructions.setText("Type your caption then click anywhere...")
        win.getMouse() # pause for click in window
        strUserCaption = inputBox.getText()
        inputBox.undraw()
        imgCat.draw(win)
        txtInstructions.setText(strUserCaption)
        txtGreetings.setText('Thanks for Visiting!')
        win.getMouse() # pause for click in window

    win.close()

main() 