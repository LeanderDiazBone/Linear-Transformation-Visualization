import numpy as np 
import tkinter as tk 
from tkinter import *
import math

maxV = 10
x = 1; a = 1
def addVec(): 
    try: 
        v1 = float(entryV1.get())
        v2 = float(entryV2.get())
        vec = np.array([v1,v2])
        global maxV
        if abs(v1) > maxV: maxV = abs(v1)
        if abs(v2) > maxV: maxV = abs(v2)

        vectors.append(vec)
    except Exception:
        v = 1

def tranformVectors():
    print("In trasformVectors")
    global trans
    trans = True

root = tk.Tk()
TK_SILENCE_DEPRECATION=1
root.title("Linear Transformation Visualization")
hei = 800; wid = hei * 3/2
canvas = tk.Canvas(root, height = hei, width = wid, bg="#ffffff")
#add Entry Fields and Label to window for matrix
lab = Label(canvas, text = "Enter a real 2x2 matrix:"); lab.place(x = hei+hei/6-100, y = 0, width = 200, height = 50)
entryA11 = Entry(master = canvas, bg = "white"); entryA11.place(x = hei+hei/6-75, y = 50, width = 100, height = 50)
entryA12 = Entry(master = canvas, bg = "white"); entryA12.place(x = hei+hei/6+50, y = 50, width = 100, height = 50)
entryA21 = Entry(master = canvas, bg = "white"); entryA21.place(x = hei+hei/6-75, y = 100, width = 100, height = 50)
entryA22 = Entry(master = canvas, bg = "white"); entryA22.place(x = hei+hei/6+50, y = 100, width = 100, height = 50)
transBut = Button(master = canvas, text = "Transform", command = tranformVectors); transBut.place(x = hei+hei/6-75, y = 150, width = 100, height = 50)
#add Entry Fields, Label + Button for adding a Vector
labVec = Label(master = canvas, text = "Enter a real 2x1 vector:"); labVec.place(x = hei+hei/6-75, y = 200, width = 150, height = 50)
entryV1 = Entry(master = canvas, bg = "white"); entryV1.place(x = hei+hei/6-75, y = 250, width = 100, height = 50)
entryV2 = Entry(master = canvas, bg = "white"); entryV2.place(x = hei+hei/6-75, y = 300, width = 100, height = 50)
addBut = Button(master = canvas, text = "Add Vector", command = addVec); addBut.place(x = hei+hei/6+50, y = 250, width = 100, height = 50)
#save the neutral matrix for the matrix value
matrix = np.array([[1,0],[0,1]])
vectors = []
transvectors = []; trans = False

def drawcoSys():
    canvas.create_rectangle(0,0, hei, hei, fill="black")
    canvas.create_line(hei/2, 5, hei/2, hei-5, fill="white")
    canvas.create_line(hei/2-5, 10, hei/2, 5, fill="white")
    canvas.create_line(hei/2, 5, hei/2+5, 10, fill="white")
    canvas.create_line(5, hei/2, hei-5, hei/2, fill="white")
    canvas.create_line(hei-10, hei/2-5, hei-5, hei/2, fill="white")
    canvas.create_line(hei-10, hei/2+5, hei-5, hei/2, fill="white")
    for i in range(1, int((maxV/x))+2):
        canvas.create_line(hei/2-2, hei/2-i*a, hei/2+2, hei/2-i*a, fill="white"); canvas.create_text(hei/2-20, hei/2-i*a, text=int(i*x), fill="white")
        canvas.create_line(hei/2-2, hei/2+i*a, hei/2+2, hei/2+i*a, fill="white"); canvas.create_text(hei/2-20, hei/2+i*a, text=int(-i*x), fill="white")
        canvas.create_line(hei/2-i*a, hei/2-2, hei/2-i*a, hei/2+2, fill="white"); canvas.create_text(hei/2-i*a, hei/2+20, text=-int(i*x), fill="white")
        canvas.create_line(hei/2+i*a, hei/2-2, hei/2+i*a, hei/2+2, fill="white"); canvas.create_text(hei/2+i*a, hei/2+20, text=int(i*x), fill="white")

def getMatrix():
    try:
        A11 = float(entryA11.get())
        A12 = float(entryA12.get())
        A21 = float(entryA21.get())
        A22 = float(entryA22.get())
        global matrix
        matrix = np.array([[A11,A12],[A21,A22]])
        if trans: addtransVec()
    except Exception:
        #no suitable values for the matrix
        v = 0

def drawVectors():
    for v in vectors:
        drawVec(v, "white")

def drawTransVectors():
    for v in transvectors:
        drawVec(v, "blue")

#draws one Vector (np.array with Dimension 2x1)
def drawVec(v = np.array, color = ""):
    c = getCor(v)
    canvas.create_line(hei/2, hei/2, c[0], c[1], fill = color)
    #draw a arrow on top of the vector
    #calculating start point: 1) get unit vector of v, 2) subtract math.squrt(12.5)
    uv = v * (1/math.sqrt(v[0]*v[0]+v[1]*v[1]))
    sp = v - math.sqrt(100)*x/float(a)*uv
    print(v[0], v[1], uv[0], uv[1], sp[0], sp[1])
    #get orthogonal unit vector 1) get an orthogonal vector 2) divide by length
    ov = np.array([1,1])
    try:
        if v[0] == 0 and v[1] == 0: raise Exception
        elif v[0] == 0: ov = np.array([1,0])
        else: ov = np.array([-v[1]/v[0],1])
        uov = ov * (1/math.sqrt(ov[0]*ov[0]+ov[1]*ov[1]))
        cuov = getCor(uov)
        cp = getCor(sp)
        p1 = np.array([sp[0]+(uov[0]*math.sqrt(12.5)*x/float(a)), sp[1]+(uov[1]*math.sqrt(12.5)*x/float(a))])
        p2 = np.array([sp[0]-(uov[0]*math.sqrt(12.5)*x/float(a)), sp[1]-(uov[1]*math.sqrt(12.5)*x/float(a))])
        cp1 = getCor(p1); cp2 = getCor(p2)
        canvas.create_line(cp1[0], cp1[1], c[0], c[1], fill = color)
        canvas.create_line(cp2[0], cp2[1], c[0], c[1], fill = color)
    except Exception:
        donothing = 1

def addtransVec():
    global transvectors
    transvectors = []
    for v in vectors:
        tv = transformVec(v)
        global maxV
        if abs(tv[0]) > maxV: maxV = abs(tv[0]); loop()
        if abs(tv[1]) > maxV: maxV = abs(tv[1]); loop()
        transvectors.append(tv)
    print("In add transVec")
    print(transvectors[0][0], transvectors[0][1])
    
def transformVec(v = np.array):
    tv = matrix.dot(v)
    print(v[0], v[1], tv[0], tv[1])
    return tv

    
def getCor(v = np.array):
    c = []
    c.append(hei/2+v[0]*(a/float(x)))
    c.append(hei/2-v[1]*(a/float(x)))
    #print(v[0], v[1], v[0]*(a/float(x)), v[1]*(a/float(x)), x, a)
    return c

def drawVectorTransformation():
    for v in vectors:
        tv = transformVec(v)
        drawVec(tv)

#grid Transformation
def gridTransformation(m = np.array, x = 1):
    vectors = []
    for i in range(int(max/x)+2):
        for j in range(int(max/x)+2):
            #draw point at h/2(+/-)i*a,h/2(+/-)j*a, 
            canvas.create_oval((hei/2+i*a)-2, (hei/2+j*a)+2, (hei/2+i*a)+2, (hei/2+j*a)-2, fill = "blue"); vectors.append(np.array([i*x,j*x])) 
            canvas.create_oval((hei/2+i*a)-2, (hei/2-j*a)+2, (hei/2+i*a)+2, (hei/2-j*a)-2, fill = "blue"); vectors.append(np.array([i*x,-j*x]))
            canvas.create_oval((hei/2-i*a)-2, (hei/2+j*a)+2, (hei/2-i*a)+2, (hei/2+j*a)-2, fill = "blue"); vectors.append(np.array([-i*x,j*x]))
            canvas.create_oval((hei/2-i*a)-2, (hei/2-j*a)+2, (hei/2-i*a)+2, (hei/2-j*a)-2, fill = "blue"); vectors.append(np.array([-i*x,-j*x]))
    for v in vectors:
            #draw vectors after transformation with matrix m
            tv = transformVec(m,v)  
            c = getCor(tv) 
            #print(tv[0], c[0], tv[1], c[1])
            canvas.create_oval(c[0]-2, c[1]+2, c[0]+2, c[1]-2, fill = "red")



def loop():
    #draw the coordinate system
    global a; a = hei/20
    global x; x = 1 
    i = 0
    list = [1, 2, 3, 4, 5, 8, 10, 15, 25, 40, 50, 75, 100, 250, 500, 1000, 2500, 5000]
    while ((hei/2-20) * x)/maxV < a: x = list[i]; i += 1
    while (maxV/x)*(a+1) < hei/2-100: a += 1
    drawcoSys()
    #changing the matrix
    getMatrix()
    drawVectors()
    if trans: drawTransVectors()
    canvas.pack()
    root.after(1000, loop)

root.after(1000, loop)
root.mainloop()

