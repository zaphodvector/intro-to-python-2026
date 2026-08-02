"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week11_Graphics2
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-04-10
    Purpose:	The purpose of this program is to draw a line on a canvas that can be changed to a random
                color and random width between 1 and 3 pixels. Each of these properties will be controlled
                by a button. 

                It took a while to make the line show up on the canvas in the first place, apparently on
                MacOS the default line color doesn't show up as black, or it draws a transparent line. 
                Very weird.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-04-10	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import tkinter as tk
import random
# ^me^

root = tk.Tk()
root.title("Scribble")
root.geometry("800x600")
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)
tk.Button(canvas, text="Clear", command=lambda: canvas.delete("drawing")).place(x=5, y=5)
tk.Button(canvas, text="Quit", command=root.destroy).place(relx=1.0, x=-5, y=5, anchor="ne")
tk.Button(canvas, text="Rnd Color", command=lambda: random_color()).place(relx=0.33, y=5, anchor="n")
# ^me^
tk.Button(canvas, text="Rnd Width", command=lambda: random_width()).place(relx=0.66, y=5, anchor="n")
# ^me^
# Mostly copied the line ai wrote for the clear command. From what I have researched the lambda is a
# anonymous function that expects to call a defined function when the button is pressed so that the
# function is only called when the button is pressed, not when it is created. I'm still a little confused 
# on the specifics but its working so I wont touch it. The final part of the lines I added is placing the
# buttons at 33% and 66% the width of the window horizontally. the anchor part anchors the button to the
# north vertically.
x0, y0 = None, None
line_color = "black"
# ^me^
line_width = 1 
# ^me^
def random_color():
    global line_color
    r = format(random.randint(0,255), '02x')
    g = format(random.randint(0,255), '02x')
    b = format(random.randint(0,255), '02x')
    line_color = "#" + r + g + b
    # ^me^

# Tkinter requires a hexadecimal color code so the randint of 0-255 is converted to base 16 and  
# formats the code to exactly 2 characters long so it can be combined into the 6 character code.
# (x stands for hexadecimal which was confusing for a minute because I thought of the roman numeral
# first) 

def random_width():
    global line_width
    line_width = random.randint(1, 3)
    # ^me^

# Much easier to assign a random width.

def press(e):
    global x0, y0
    x0, y0 = e.x, e.y
def drag(e):
    global x0, y0
    if x0 is not None:
        canvas.create_line(x0, y0, e.x, e.y, width=line_width, fill=line_color, tags="drawing")
        x0, y0 = e.x, e.y
# fill added after finding default renders invisible on Mac; width and fill now use globals - AI
def release(e):
    global x0, y0
    x0, y0 = None, None
canvas.bind("<Button-1>", press)
canvas.bind("<B1-Motion>", drag)
canvas.bind("<ButtonRelease-1>", release)
root.mainloop()