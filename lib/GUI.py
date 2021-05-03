import numpy as np 
import tkinter as tk
from tkinter import *
import math
import GridTr
import VectorTr 
import DeterminantAn
import Global
import Helper

root = tk.Tk()
TK_SILENCE_DEPRECATION=1
root.title("Linear Transformation Visualization")
gl = Global.Parameters(10, 800, 1, 400, tk.Canvas(root, height = 800, width = 1200, bg="#ffffff"), np.array([[0, 0],[0, 0]]), [])
helper = Helper.Helper(gl)
vt = VectorTr.VectorTr(gl, helper)
da = DeterminantAn.DeterminantAn(gl, helper)
gt = GridTr.GridTr(gl, helper)

op = vt

#add Entry Fields and Label to window for matrix
lab = Label(gl.canvas, text = "Enter a real 2x2 matrix:"); lab.place(x = gl.hei+gl.hei/6-100, y = 0, width = 200, height = 50)
entryA11 = Entry(master = gl.canvas, bg = "white"); entryA11.place(x = gl.hei+gl.hei/6-75, y = 50, width = 100, height = 50)
entryA12 = Entry(master = gl.canvas, bg = "white"); entryA12.place(x = gl.hei+gl.hei/6+50, y = 50, width = 100, height = 50)
entryA21 = Entry(master = gl.canvas, bg = "white"); entryA21.place(x = gl.hei+gl.hei/6-75, y = 100, width = 100, height = 50)
entryA22 = Entry(master = gl.canvas, bg = "white"); entryA22.place(x = gl.hei+gl.hei/6+50, y = 100, width = 100, height = 50)

#drop Down menu
Optionlist = ["Vector Transformation", "Grid Transformation", "Determinant Animation"]
vt.open()

var = tk.StringVar(gl.canvas)
var.set(Optionlist[0])
opt = tk.OptionMenu(gl.canvas, var, *Optionlist)
opt.place(x = gl.hei+gl.hei/6-75, y = 150, width = 200, height = 50)

def callback(*args):
    forgetAllOpenWidgets()
    #print("IN CALLBACK")
    global op

    if var.get() == "Vector Transformation": op = vt
    if var.get() == "Grid Transformation": op = gt
    if var.get() == "Determinant Animation": op = da

    op.reset()
    op.open()


def forgetAllOpenWidgets():
    for wid in gl.OpenWidgets:
        wid.place_forget()
    gl.OpenWidgets = []

var.trace("w", callback)

def drawcoSys():
    gl.canvas.create_rectangle(0,0, gl.hei, gl.hei, fill="black")
    gl.canvas.create_line(gl.hei/2, 5, gl.hei/2, gl.hei-5, fill="white")
    gl.canvas.create_line(gl.hei/2-5, 10, gl.hei/2, 5, fill="white")
    gl.canvas.create_line(gl.hei/2, 5, gl.hei/2+5, 10, fill="white")
    gl.canvas.create_line(5, gl.hei/2, gl.hei-5, gl.hei/2, fill="white")
    gl.canvas.create_line(gl.hei-10, gl.hei/2-5, gl.hei-5, gl.hei/2, fill="white")
    gl.canvas.create_line(gl.hei-10, gl.hei/2+5, gl.hei-5, gl.hei/2, fill="white")
    for i in range(1, int(gl.maxV/gl.x)+2):
        gl.canvas.create_line(gl.hei/2-2, gl.hei/2-i*gl.a, gl.hei/2+2, gl.hei/2-i*gl.a, fill="white"); gl.canvas.create_text(gl.hei/2-20, gl.hei/2-i*gl.a, text=int(i*gl.x), fill="white")
        gl.canvas.create_line(gl.hei/2-2, gl.hei/2+i*gl.a, gl.hei/2+2, gl.hei/2+i*gl.a, fill="white"); gl.canvas.create_text(gl.hei/2-20, gl.hei/2+i*gl.a, text=int(-i*gl.x), fill="white")
        gl.canvas.create_line(gl.hei/2-i*gl.a, gl.hei/2-2, gl.hei/2-i*gl.a, gl.hei/2+2, fill="white"); gl.canvas.create_text(gl.hei/2-i*gl.a, gl.hei/2+20, text=-int(i*gl.x), fill="white")
        gl.canvas.create_line(gl.hei/2+i*gl.a, gl.hei/2-2, gl.hei/2+i*gl.a, gl.hei/2+2, fill="white"); gl.canvas.create_text(gl.hei/2+i*gl.a, gl.hei/2+20, text=int(i*gl.x), fill="white")

def getMatrix():
    try:
        A11 = float(entryA11.get())
        A12 = float(entryA12.get())
        A21 = float(entryA21.get())
        A22 = float(entryA22.get())
        gl.matrix = np.array([[A11,A12],[A21,A22]])
    except Exception:
        #no suitable values for the matrix
        pass

def loop():
    #draw the coordinate system
    gl.a = gl.hei/20
    gl.x = 1 
    i = 0
    list = [1, 2, 3, 4, 5, 8, 10, 15, 25, 40, 50, 75, 100, 250, 500, 1000, 2500, 5000]
    while ((gl.hei/2-20) * gl.x)/gl.maxV < gl.a: gl.x = list[i]; i += 1
    while (gl.maxV/gl.x)*(gl.a+1) < gl.hei/2-100: gl.a += 1
    drawcoSys()
    #get the matrix
    getMatrix()
    global op
    op.main()
    gl.canvas.pack()
    root.after(500, loop)

root.after(500, loop)
root.mainloop()
