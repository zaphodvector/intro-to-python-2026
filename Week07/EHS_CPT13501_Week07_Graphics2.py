"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week07_Graphics2
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-03-07
    Purpose:	The purpose of this program is to draw a window consisting of an 8x8 checkerboard.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-03-07	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *

WIN_SIZE = 480
SQUARES = 8
SQ_SIZE = WIN_SIZE // SQUARES

def main():
    win = GraphWin("Checkerboard", WIN_SIZE, WIN_SIZE)

    for row in range(SQUARES):
        for col in range(SQUARES):
            x = col * SQ_SIZE
            y = row * SQ_SIZE
            square = Rectangle(Point(x, y), Point(x + SQ_SIZE, y + SQ_SIZE))
            square.setFill("black" if (row + col) % 2 == 0 else "red")
            square.setOutline("")
            square.draw(win)

    win.getMouse()
    win.close()

main()



#I had a busy week, and i do not have the time before the deadline to make comments on this program.