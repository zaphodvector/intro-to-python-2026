"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week11_Graphics_Sample
    Author:	Ed Weber
    Language:	Python
    Date:	2025-01-07
    Purpose:	The purpose of this program is to demonstrate the creation of a Triangle
                graphics class that builds on the basic Zelle graphics library.  This base
                class is then used to create some triangle examples in a window.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2025-01-07	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *
import random

class Triangle(Polygon):
    def __init__(self, point1, point2, point3):
        '''Constructor that creates a solid triangle using three points.
        This constructor calls the init from the Polygon class using super().
        '''
        super().__init__(point1, point2, point3)
        
# Example usage of the Triangle class
def main():
    # Create the window
    win = GraphWin("Triangle Class Example", 600, 600)
        
    # Define three points for the triangle (example coordinates)
    point1 = Point(100, 100)
    point2 = Point(200, 100)
    point3 = Point(150, 200)
    
    # Create a triangle with these points
    triMyTriangle = Triangle(point1, point2, point3)

    # Set the fill color of the triangle
    triMyTriangle.setFill("salmon")
    triMyTriangle.setOutline("black")  
    triMyTriangle.setWidth(2)
    triMyTriangle.draw(win)
    win.getMouse()

    fncDraw20RandomTriangles(win)

    win.getMouse()
    win.close()

def fncDraw20RandomTriangles(win):
    '''This function will draw 20 random triangles in the window received as a parameter.
    This function calls the fncGetRandomPointInWindow three times for each triangle to set
    the triangles points.  It also randomly colors each triangle.
    '''
    for int20Triangles in range(20):
        pts3Points = []
        for int3Points in range(3):
            pts3Points.append(fncGetRandomPointInWindow(win))
        triThisTriangle = Triangle(pts3Points[0],pts3Points[1],pts3Points[2])
        triThisTriangle.setFill(color_rgb(random.randint(0,255),
                                          random.randint(0,255),
                                          random.randint(0,255)))
        triThisTriangle.setOutline('black')
        triThisTriangle.setWidth(2)
        triThisTriangle.draw(win)
        

def fncGetRandomPointInWindow(win):
    '''This function receives a window parameter and returns a random point within its boundaries
    '''
    intMaxX = win.getWidth()
    intMaxY = win.getHeight()
    intThisX = random.randint(0,intMaxX)
    intThisY = random.randint(0,intMaxY)
    return Point(intThisX,intThisY)


# Run the program
if __name__ == '__main__':
    main()