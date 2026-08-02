"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPY13501_Graphics03
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-03-28
    Purpose:	The purpose of this program is to draw twenty randomly sized and placed circles, then
                coloring in the ones overlapping green, and the others black.
                Two circles touching will not become green, only overlapping ones.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-03-28	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *
import random
import math

WIN_WIDTH = 600
WIN_HEIGHT = 600
NUM_CIRCLES = 20
MIN_RADIUS = 15
MAX_RADIUS = 50

#Defining the window variables now so that I can make sure that the circles do not 
#exit the window's boundaries.

win = GraphWin("Overlapping Circles", WIN_WIDTH, WIN_HEIGHT)
win.setBackground("white")

circles = []

#Creating a list to store the dictionary for each circle.

for _ in range(NUM_CIRCLES):
    radius = random.randint(MIN_RADIUS, MAX_RADIUS)
    center_x = random.randint(radius, WIN_WIDTH - radius)
    center_y = random.randint(radius, WIN_HEIGHT - radius)

#This for loop iterated through the circles and assigns a random radius within the min and max, and
#assures that it will not exceed the window boundaries.

    overlapping = False
    for existing in circles:
        distance_x = center_x - existing["center_x"]
        distance_y = center_y - existing["center_y"]
        distance = math.sqrt(distance_x**2 + distance_y**2)
                     #c^2   =    a^2       +      b^2
        if distance < radius + existing["radius"]:
            overlapping = True
            existing["object"].setFill("pale green")

#This checks to see if the circles are overlapping. The for loop goes through each circle and 
#finds the distance between the centers of each circle with the pythagorean theorem.
#If the distance is less than the combined radii then overlapping is set to true and the 
#circle will be green.
#Each circle created is checked against each existing circle every time a circle is created.

    color = "pale green" if overlapping else "black"

    circle = Circle(Point(center_x, center_y), radius)
    circle.setFill(color)
    circle.setOutline("black")
    circle.draw(win)

    #Drawing the circles and coloring appropriately.

    circles.append({"center_x": center_x, "center_y": center_y, "radius": radius, "object": circle})

    #Stores each circle's information as a dictionary in the list created earlier so that it can be 
    #referenced when creating and doing the math on every other circle.

win.getMouse()
win.close()