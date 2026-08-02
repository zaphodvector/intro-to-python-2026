"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week04_Graphics_Project5
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-14
    Purpose:	The purpose of this program is to create a graphical application that displays a window
                with a randomly colored rectangle and titles the window as the RGB value of the rectangle.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-14	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *              #Importing the graphics library.
import random                       #Importing the random module.

red = random.randint(0, 255)        #Defining three values and equating them to a
green = random.randint(0, 255)      #random number in the correct range for a rgb value.
blue = random.randint(0, 255)

win = GraphWin(f"RGB Color: ({red}, {green}, {blue})", 400, 200)    

#Creating a window and using an f string to pull the variables I created into the window title.

randrect = Rectangle(Point(50, 50), Point(350, 150))                
randrect.setFill(color_rgb(red, green, blue))
randrect.draw(win)

#Creating a rectangle and using setFill with the rgb variables to randomize the color each time.

win.getMouse()
win.close()

#Waiting for user input to close the window.