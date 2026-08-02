"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week06_Graphics_Sample
    Author:	Ed Weber
    Language:	Python
    Date:	2024-12-31
    Purpose:	The purpose of this program is to demonstrate creating a pseudo-button
                in a Zelle graphics program.  Also, this demonstrates using loops
                to process multiple mouse click events until specific conditions occur.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2024-12-31	Original Version of Code
----------------------------------------------------------------------------------------------------------
""" 
import random
from graphics import *

def ColorPicker():
    blnStayHere = True      # create a sentinel
    blnColorSwatchIsDrawn = False # handle drawing the swatch only one time
    while blnStayHere:
        eventMouseClick = win.getMouse()
        intThisClickX = eventMouseClick.getX()
        intThisClickY = eventMouseClick.getY()
        if((50 <= intThisClickX <= 350) and 
            (365 <= intThisClickY <= 395)):  # click is in pseudo-button location
            blnStayHere = False
        else:
            if not blnPictureExists:
                # tell them it won't work
                txtInstructions.setText("You cannot pick a color from a missing file.")
            else:
                if not blnColorSwatchIsDrawn:
                    rectColorSwatch.draw(win)
                    blnColorSwatchIsDrawn = True
                # find where the click was relative to the image
                if((imgUpperLeftPoint.getX() <= intThisClickX <= imgLowerRightPoint.getX()) and
                    (imgUpperLeftPoint.getY() <= intThisClickY <= imgLowerRightPoint.getY())):
                    # click is in the image
                    intImgClickX = int(intThisClickX - 200 + int(imgCatWidth / 2))
                    intImgClickY = int(intThisClickY - 200 + int(imgCatHeight / 2))
                    # print(intImgClickX, intImgClickY)
                    lstRGB = imgCat.getPixel(intImgClickX,intImgClickY)
                    strPixelRGB = 'R: '+ str(lstRGB[0]) + \
                                ' G: ' + str(lstRGB[1]) + \
                                ' B: ' + str(lstRGB[2])
                    txtInstructions.setText(f'Pixel found was colored: {strPixelRGB}')
                    rectColorSwatch.setFill(color_rgb(lstRGB[0],lstRGB[1],lstRGB[2]))
                
# Create the window and text globally
win = GraphWin("Color Picker From Image", 400, 400)
txtInstructions = Text(Point(200,20),"Pick a color by clicking on the Image.")
txtInstructions.draw(win)
#strPictureFileName = '.\\media\\LimeCat.gif'          # I have a media folder 
strPictureFileName = '.\\media\\LogoSmall.gif'        # I have a media folder 
import os                           # import the os library so I can verify file existence
if (not os.path.exists(strPictureFileName)):    # test if image can be found
    blnPictureExists = False            # for use later
    txtMissingFile = Text(Point(200,200), "The Image File does not exist!")
    txtMissingFile.draw(win)
    txtInstructions.setText(txtMissingFile.getText())
else:                               # the image was found...
    blnPictureExists = True         # for use later
    imgCat = Image(Point(200,200),strPictureFileName)  # place the image
    imgCatWidth = imgCat.getWidth()
    imgCatHeight = imgCat.getHeight()
    imgUpperLeftPoint = Point(200 - (imgCatWidth / 2), 200 - (imgCatHeight /2))
    imgLowerRightPoint = Point(200 + (imgCatWidth / 2), 200 + (imgCatHeight /2))
    imgCat.draw(win)
    rectColorSwatch = Rectangle(Point(150,30),Point(250,50))
    rectColorSwatch.setOutline('black')
    rectColorSwatch.setWidth(3)
    # don't draw the ColorSwatch until later... just define it now!

rectMyButton = Rectangle(Point(50,365),Point(350,395))
rectMyButton.setFill("salmon")
rectMyButton.setOutline('black')
rectMyButton.setWidth(3)
rectMyButton.draw(win)
txtButtonLabel = Text(Point(200,380),"Click this pseudo-button to exit.")
txtButtonLabel.setSize(12)
txtButtonLabel.setStyle('bold')
txtButtonLabel.draw(win)

# now that everything exists globally, run the ColorPicker function for the loop
ColorPicker()