"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week04_Graphics_Sample
    Author:	Ed Weber
    Language:	Python
    Date:	2024-12-29
    Purpose:	The purpose of this program is to use the Zelle Graphics library to explore the
                basic concepts of creating a GUI (non-text-based) program in Python.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2024-12-29	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *      # the graphics.py library must be installed first!
                            # only import the things you use!
def main():                 # create a main function
    win = GraphWin("First Graphics Examples", 400, 400)     # create a window object
    txtGreetings = Text(Point(200,30),"Greetings in Graphics in Python!")   # a text object
    txtGreetings.setFace("courier")                         # setting text properties (font)
    txtGreetings.setSize(15)
    txtGreetings.setTextColor(color_rgb(50,0,0))
    txtGreetings.draw(win)                                  # draw the text in the window
    linMyLine = Line(Point(2,45),Point(398,45))             # create a line object
    linMyLine.setFill("orange")                             # set properties
    linMyLine.setWidth(5)
    linMyLine.draw(win)                                     # draw
    cirMyCircle = Circle(Point(200,200),140)                # now a circle
    cirMyCircle.setWidth(3)
    cirMyCircle.setFill("BlanchedAlmond")
    cirMyCircle.draw(win)
    rectMyRectangle = Rectangle(Point(130,130),Point(270,270)) # now a rectangle
    rectMyRectangle.setWidth(2)
    rectMyRectangle.setFill("Cyan")
    rectMyRectangle.draw(win)
    txtInstructions = Text(Point(200,360),"(Click anywhere in the window to close...)")
    txtInstructions.draw(win)
    win.getMouse()  # pause for click in window
    win.close()     # close the window
main()              # run the main function