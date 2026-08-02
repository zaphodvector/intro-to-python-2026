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
message.draw(win)                                   #Drawing the string iin the window.


instruction = Text(Point(width/2, height/2 - 40), "Enter radius and click to resize")
instruction.draw(win)

win.getMouse()  # Wait for user to click after typing

text_value = entry.getText().strip()

try:
    new_radius = float(text_value)
    if 1 <= new_radius <= max_radius:
        circle.undraw()
        circle = Circle(center, new_radius)  # Reuse 'circle' variable
        circle.setFill("lightblue")
        circle.draw(win)
    else:
        message.setText(f"Must be 1–{int(max_radius)}")
except ValueError:
    message.setText("Please enter a valid number")

win.getMouse()  # Final click to close
win.close()