"""
----------------------------------------------------------------------------------------------------------
    Name:		cube_test_AI
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-02-11
    Purpose:	The purpose of this program is to spin a cube
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-02-11	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
from graphics import *
import math

WIDTH, HEIGHT = 800, 600
win = GraphWin("Keyboard Cube", WIDTH, HEIGHT, autoflush=False)
win.setBackground("black")

size = 120

vertices = [
    [-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],
    [-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]
]

faces = [
    (0,1,2,3,"yellow"),   # bottom
    (4,5,6,7,"white"),    # top
    (0,1,5,4,"blue"),
    (1,2,6,5,"red"),
    (2,3,7,6,"green"),
    (3,0,4,7,"orange"),
]

angleX = angleY = angleZ = 0

def rotateX(p,a):
    x,y,z = p
    return [x,
            y*math.cos(a)-z*math.sin(a),
            y*math.sin(a)+z*math.cos(a)]

def rotateY(p,a):
    x,y,z = p
    return [x*math.cos(a)+z*math.sin(a),
            y,
            -x*math.sin(a)+z*math.cos(a)]

def rotateZ(p,a):
    x,y,z = p
    return [x*math.cos(a)-y*math.sin(a),
            x*math.sin(a)+y*math.cos(a),
            z]

def project(p):
    x,y,z = p
    d = 4
    f = d/(d-z)
    return Point(x*f*size + WIDTH/2,
                 -y*f*size + HEIGHT/2)

while True:
    key = win.checkKey()
    if key == "w": angleX += 0.05
    if key == "s": angleX -= 0.05
    if key == "a": angleY += 0.05
    if key == "d": angleY -= 0.05
    if key == "q": angleZ += 0.05
    if key == "e": angleZ -= 0.05

    if win.checkMouse():
        break

    rotated = []
    for v in vertices:
        r = rotateX(v,angleX)
        r = rotateY(r,angleY)
        r = rotateZ(r,angleZ)
        rotated.append(r)

    face_data = []
    for f in faces:
        idx,color = f[:4],f[4]
        z_avg = sum(rotated[i][2] for i in idx)/4
        face_data.append((z_avg,idx,color))

    face_data.sort(reverse=True)

    # Clear screen
    win.delete("all")

    for _,idx,color in face_data:
        poly = Polygon([project(rotated[i]) for i in idx])
        poly.setFill(color)
        poly.setOutline("black")
        poly.draw(win)

    update()

win.close()