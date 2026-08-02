"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week05_Graphics3
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-21
    Purpose:	The purpose of this program is to 
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-21	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *                              #Importing the graphics library

width = 400                                         #Defining a width and heighth variable to use later.
height = 400

win = GraphWin("Resizable Circle", width, height)   #Defining a window, it's name, and it's size with my 
                                                    #previously defined variables.

center = Point(width/2, height/2)                   #Defining a variable at the center of the width and 
max_radius = min(width, height) / 2                 #heighth to place the circle at.
                                                    #Defining the max radius as the smallest value of the 
                                                    #window size divided by two so that the circle cannot
                                                    #exceed the size of the window.


circle = Circle(center, max_radius)                 #Defining a circle and its size and placing it in the
circle.setFill("lightblue")                         #center.
circle.draw(win)                                    #Drawing the circle in the window.


entry = Entry(center, 10)                           #Defining an entry box at the center of the window and
entry.draw(win)                                     #drawing it in the window.


message = Text(Point(width/2, height/2 + 40), "")   #Defining an empty string below the text entry box.
message.draw(win)                                   #Drawing the string in the window.


win.getMouse()                                      #Waiting for a click from the user

text_value = entry.getText().strip()                #Defining a variable equal to the user's entry and 
                                                    #stripping any whitespace.

try:                                                #Using a try function to protect from crashes from an
    new_radius = float(text_value)                  #invalid input. and setting the new circle to the user's
                                                    #entry.
    if 1 <= new_radius <= max_radius:               #If the radius of the circle is within the allowed value
        circle.undraw()                             #the old circle is un-drawn and a new circle at the center 
        circle = Circle(center, new_radius)         #with the new radius.
        circle.setFill("lightblue")
        circle.draw(win)                            #Drawing the circle in the window.

    else:                                           #Using an else function to tell the user the required radius.
        message.setText(f"The radius must be between 1–{int(max_radius)}")
except ValueError:                                  #Using an except function to screen for a non input or text.
    message.setText("Please enter a valid number")  #Changing the text to a warning.

win.getMouse()                                      #Checking for a click from the user and closing the window.
win.close()