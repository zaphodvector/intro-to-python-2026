"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPY_13501_Week06_Graphics2
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-28
    Purpose:	The purpose of this program is to display a traffic light that a user can control.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-28	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *

def make_button(win, x, y, w, h, label, color="lightgray"):
    btn = Rectangle(Point(x - w/2, y - h/2), Point(x + w/2, y + h/2))
    btn.setFill(color)
    btn.setWidth(2)
    btn.draw(win)
    Text(Point(x, y), label).draw(win)
    return btn

        #Defining a function to be called on later and given parameters to makes each button.

def clicked(rect, pt):
    p1, p2 = rect.getP1(), rect.getP2()
    return p1.getX() < pt.getX() < p2.getX() and p1.getY() < pt.getY() < p2.getY()

        #Defining a function to check whether a mouse has clicked inside the 
        #rectangles that are created later.

def make_circle(win, x, y, r, color):
    light = Circle(Point(x, y), r)
    light.setFill(color)
    light.setWidth(2)
    light.draw(win)
    return light

        #Defining a function to make each light.

def set_state(lights, state):
    colors = {"stop": ("red", "darkgoldenrod", "darkgreen"),
              "caution": ("darkred", "yellow", "darkgreen"),
              "go": ("darkred", "darkgoldenrod", "lime green")}
    for light, color in zip(lights, colors[state]):
        light.setFill(color)

        #This function is used to change the color of each light when an option is picked. The 
        #dictionary contains the correct colors for each light option and the name of the button
        #that will be drawn later. Then a for loop takes each object and each color and pairs them 
        #with their counterpart via the zip function. (The colors here and the circles in the 
        #main function.)

def main():
    win = GraphWin("Traffic Light", 400, 560)
    win.setBackground("white")

    Text(Point(200, 25), "Traffic Light Simulator").draw(win)

    #Defining my main function and drawing the window with it's parameters.

    housing = Rectangle(Point(150, 50), Point(250, 350))
    housing.setFill("darkgray")
    housing.setWidth(3)
    housing.draw(win)

    #Drawing the housing for the lights.

    lights = [make_circle(win, 200, y, 40, color)
              for y, color in [(110, "darkred"), (200, "darkgoldenrod"), (290, "darkgreen")]]
    
    #Using the make_circle function created earlier to draw each light inside the housing with a
    #for loop.

    stop_btn    = make_button(win, 200, 390, 100, 35, "Stop",    "salmon")
    caution_btn = make_button(win, 200, 430, 100, 35, "Caution", "lightyellow")
    go_btn      = make_button(win, 200, 470, 100, 35, "Go",      "lightgreen")
    exit_btn    = make_button(win, 200, 520, 100, 35, "Exit",    "lightgray")

    #Using the make_button function to create a button for each action the user can make.

    buttons = [(stop_btn, "stop"), (caution_btn, "caution"), (go_btn, "go")]

    #Defining a list of tuples to be called in the for loop later.

    while True:
        click = win.getMouse()
        if clicked(exit_btn, click):
            break
        for btn, state in buttons:
            if clicked(btn, click):
                set_state(lights, state)

    #Creating a while loop that checks for a click from the mouse until the exit button is clicked.
        #This for loop checks through the state of each button and checks two variables for each,
        #the btn(which button) and the state of the button.
            #An if statement checks for the clicked function created earlier and changes the 
            #state of the buttons.

    win.close()     #Closes the window after the user breaks the loop.

main()              