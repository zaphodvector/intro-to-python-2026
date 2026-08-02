"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week05_Graphics02
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-21
    Purpose:	The purpose of this program is to make a graphical window with a rectangle button. 
                The Button will have the instructions for the program labeled inside it. If the 
                user clicks inside the rectangle it will show a random number from 1 to 100. If they 
                click outside the rectangle the window closes.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-21	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *              #Importing the graphics library
import random                       #importing the random module

win = GraphWin("Random Number Button", 400, 300)            #Defining the window with its title and size.

rect = Rectangle(Point(100, 120), Point(300, 180))          #Defining the rectangle's location/size in the 
rect.setFill("lightyellow")                                 #window and color.
rect.draw(win)                                              #Drawing the rectangle in the window.

tutorial = Text(Point(200, 150),                            #Defining the text's position inside the 
    "Click here to generate a\nrandom number (1–100)")      #rectangle and drawing it in.
tutorial.draw(win)

click = win.getMouse()                                      #Defining a variable to check for a click.
x = click.getX()                                            #Grabbing the x and y value of the mouse's 
y = click.getY()                                            #position after a click and assigning them to 
                                                            #separate variables.

if 100 <= x <= 300 and 120 <= y <= 180:                     #Using an if statement on x and y to check if
    number = random.randint(1, 100)                         #the mouse's position is inside the rectangle.
    tutorial.setText(f"Random number: {number}")            #If it is inside the values a random number is 
    win.getMouse()                                          #generated and set to replace the tutorial text.
else:                                                           
    win.close()                                             #Using an else function to close the window if 
                                                            #the cursor is clicked outside the rectangle                                             