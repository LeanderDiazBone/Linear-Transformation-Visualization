import numpy as np 
import tkinter as tk 
import math
from tkinter import *


class GridTr:
    
    def __init__(self, gl, helper):
        self.Widgets = []
        self.Places = []
        self.gl = gl
        self.helper = helper
        labModGTW = Label(master = gl.canvas, text = "Grid Transformation") 
        self.Places.append([gl.hei+gl.hei/6-75, 300, 150, 50])
        self.Widgets.append(labModGTW)
    
    def open(self):
        i = 0
        for wid in self.Widgets:
            l = self.Places[i]
            wid.place(x = l[0], y = l[1], width = l[2], height = l[3])
            self.gl.OpenWidgets.append(wid)
            i += 1  

    def main(self):
        pass

    def reset(self):
        pass
        
    def toStr(self):
        return "Grid Transformation Class"

"""
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
            canvas.create_oval(c[0]-2, c[1]+2, c[0]+2, c[1]-2, fill = "red")
"""