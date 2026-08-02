"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week06_Graphics4
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-28
    Purpose:	The purpose of this program is to create a response time game that the user interacts with
                via the mouse. After the user is done their best, worst, and average time is shown, as 
                well as how many targets they clicked.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-28	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *
import random
import time

WIN_W = 600
WIN_H = 500
TARGET_SIZE = 50
MAX_TIME = 30
MAX_CLICKS = 60
COLORS = ["red", "blue", "green", "orange", "purple", "cyan", "magenta", "yellow"]

def make_button(win, x, y, w, h, label, color="lightgray"):
    btn = Rectangle(Point(x - w/2, y - h/2), Point(x + w/2, y + h/2))
    btn.setFill(color)
    btn.setWidth(2)
    btn.draw(win)
    txt = Text(Point(x, y), label)
    txt.setSize(14)
    txt.setStyle("bold")
    txt.draw(win)
    return btn

    #Creating a function that draws a button with text after receiving parameters later.

def clicked(rect, pt):
    p1, p2 = rect.getP1(), rect.getP2()
    return p1.getX() < pt.getX() < p2.getX() and p1.getY() < pt.getY() < p2.getY()

    #Creating a function to check for a click from the user and return the position.

def random_target(win, existing):
    if existing:
        existing.undraw()

    #Undraw old target if it exists

    x = random.randint(TARGET_SIZE, WIN_W - TARGET_SIZE)
    y = random.randint(100 + TARGET_SIZE, WIN_H - TARGET_SIZE)
    color = random.choice(COLORS)

    #Defining three random variables that will be called on for each creation of the target.

    target = Rectangle(Point(x, y), Point(x + TARGET_SIZE, y + TARGET_SIZE))
    target.setFill(color)
    target.setWidth(2)
    target.draw(win)
    return target

    #Drawing a target at a random position in the window.

def show_stats(status_text, times):
    if len(times) == 0:
        status_text.setText("No targets were clicked.")
        return
    avg  = sum(times) / len(times)
    best = min(times)
    worst = max(times)
    status_text.setText(
        "Done!  Targets clicked: " + str(len(times)) +
        "   Avg: "   + str(round(avg,   3)) + "s" +
        "   Best: "  + str(round(best,  3)) + "s" +
        "   Worst: " + str(round(worst, 3)) + "s"
    )

    #Creating a function to display the stats from the users game and including a safety if 
    #the user didn't click any targets.

def main():
    win = GraphWin("Response Time Evaluator", WIN_W, WIN_H)
    win.setBackground("white")

    #Status/instruction text area at the top.
    status_box = Rectangle(Point(10, 10), Point(WIN_W - 10, 70))
    status_box.setFill("lightyellow")
    status_box.setWidth(2)
    status_box.draw(win)

    status_text = Text(Point(WIN_W / 2, 40),
        "Click the START button to begin the response time evaluation.")
    status_text.setSize(11)
    status_text.draw(win)

    #Start button
    start_btn = make_button(win, WIN_W / 2, 85, 120, 30, "Start", "lightgreen")


    while True:
        click = win.getMouse()
        if clicked(start_btn, click):
            break

         #Wait for the user to click the button.

    start_btn.undraw()
    status_text.setText("Click the colored target as fast as you can!")

    #Main evaluation loop
    response_times = []
    target = None
    game_start = time.time()

    #Creating an empty list to store response times in.
    #Setting target to none at first.
    #Grabs the time that the game has begun and stores it.

    while len(response_times) < MAX_CLICKS and (time.time() - game_start) < MAX_TIME:
        target = random_target(win, target)
        t_start = time.time()

        #Update status with progress.
        elapsed = round(time.time() - game_start, 1)
        status_text.setText(
            "Clicks: " + str(len(response_times)) + "/" + str(MAX_CLICKS) +
            "   Time remaining: " + str(round(MAX_TIME - elapsed, 1)) + "s"
        )

        #Creating the while loop that checks to see if the program has either run too long or
        #the user has reached the maximum amount of targets clicked.
        #Creates a target using the random_target function and grabs the time that the target was
        #created to compare it to the time it was clicked.

        #Wait for a click on the target.
        while True:
            click = win.getMouse()
            elapsed = time.time() - game_start
            if elapsed >= MAX_TIME:
                break
            if clicked(target, click):
                response_times.append(round(time.time() - t_start, 3))
                break

        if time.time() - game_start >= MAX_TIME:
            break

            #This while loop checks for a click from the user and creates an elapsed time variable
            #after comparing the time of the creation of the target and the user's click. Also
            #checks if the user has not clicked for the maximum game time and exits the loop.
            #Also stores the response time in the list created earlier.

    #Undraw last target.
    if target:
        target.undraw()

    show_stats(status_text, response_times)

    #Exit button
    make_button(win, WIN_W / 2, WIN_H - 30, 100, 35, "Exit", "lightgray")
    while True:
        click = win.getMouse()
        ex = Rectangle(Point(WIN_W/2 - 50, WIN_H - 47), Point(WIN_W/2 + 50, WIN_H - 13))
        if clicked(ex, click):
            break

        #Draws the exit button at the bottom of the window after the test is finished and
        #uses a while loop to check if the user clicks within the button.

    win.close()

main()