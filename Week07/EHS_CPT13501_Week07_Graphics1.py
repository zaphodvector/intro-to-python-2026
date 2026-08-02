"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week07_Graphics1
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-03-07
    Purpose:	The purpose of this program is to draw a window with 20 horizontal lines of different 
                widths and colors.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-03-07	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *
import random

WIN_W = 600
WIN_H = 500
NUM_LINES = 20
LINE_WIDTH = 3
MARGIN = 20

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return color_rgb(r, g, b)

def main():
    win = GraphWin("Random Lines", WIN_W, WIN_H)
    win.setBackground("white")

    spacing = (WIN_H - MARGIN * 2) // (NUM_LINES - 1)

    for i in range(NUM_LINES):
        y = MARGIN + i * spacing
        length = random.randint(50, WIN_W - MARGIN)

        line = Line(Point(0, y), Point(length, y))
        line.setWidth(LINE_WIDTH)
        line.setFill(random_color())
        line.draw(win)

    win.getMouse()
    win.close()

main()


#I had a busy week, and i do not have the time before the deadline to make comments on this program.