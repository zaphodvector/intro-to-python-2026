import tkinter as tk
import random  # added for random color and width features

root = tk.Tk()
root.title("Scribble")
root.geometry("800x600")
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)
tk.Button(canvas, text="Clear", command=lambda: canvas.delete("drawing")).place(x=5, y=5)
tk.Button(canvas, text="Quit", command=root.destroy).place(relx=1.0, x=-5, y=5, anchor="ne")
tk.Button(canvas, text="Rnd Color", command=lambda: random_color()).place(relx=0.33, y=5, anchor="n")  # added
tk.Button(canvas, text="Rnd Width", command=lambda: random_width()).place(relx=0.66, y=5, anchor="n")  # added
x0, y0 = None, None
line_color = "black"  # added
line_width = 1  # added
def random_color():  # added
    global line_color
    line_color = f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}"
def random_width():  # added
    global line_width
    line_width = random.randint(1, 3)
def press(e):
    global x0, y0
    x0, y0 = e.x, e.y
def drag(e):
    global x0, y0
    if x0 is not None:
        canvas.create_line(x0, y0, e.x, e.y, width=line_width, fill=line_color, tags="drawing")  # fill added after finding default renders invisible on Mac; width and fill now use globals
        x0, y0 = e.x, e.y
def release(e):
    global x0, y0
    x0, y0 = None, None
canvas.bind("<Button-1>", press)
canvas.bind("<B1-Motion>", drag)
canvas.bind("<ButtonRelease-1>", release)
root.mainloop()