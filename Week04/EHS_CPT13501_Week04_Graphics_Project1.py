"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week04_Graphics_Project1
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-14
    Purpose:	The purpose of this program is to create a graphical program that displays the 
                Olympics logo
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-14	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *

#importing the graphics library

win = GraphWin("Olymics Logo", 600, 300)            #Creating a window with a title.
bluecircle = Circle(Point(150, 120), 60)            #Defining a variable equal to a circle. Then  
bluecircle.setOutline('blue')                       #defining the location,size, color, and width.
bluecircle.setWidth(8)
bluecircle.draw(win)                                #Drawing the circle
blackcircle = Circle(Point(300, 120), 60)           #Repeat for each color
blackcircle.setOutline('black')
blackcircle.setWidth(8)
blackcircle.draw(win)
redcircle = Circle(Point(450, 120), 60)
redcircle.setOutline('red')
redcircle.setWidth(8)
redcircle.draw(win)
yellowcircle = Circle(Point(225, 170), 60)
yellowcircle.setOutline('yellow')
yellowcircle.setWidth(8)
yellowcircle.draw(win)
greencircle = Circle(Point(375, 170), 60)
greencircle.setOutline('green')
greencircle.setWidth(8)
greencircle.draw(win)

win.getMouse()                                      #Waiting for userinput to close the window
win.close()