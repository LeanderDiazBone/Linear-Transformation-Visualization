import numpy as np 
import tkinter as tk 
from tkinter import *
import math

    

class VectorTr:

    def __init__(self, gl, helper):
        self.Widgets = []
        self.Places = []
        self.gl = gl
        self.transvectors = []
        self.helper = helper
        self.trans = False
        self.animate = False
        self.vectors = [] 
        labModVTW = Label(master = gl.canvas, text = "Vector Transformation") 
        labModVTW.place(x = gl.hei+gl.hei/6-75, y = 300, width = 150, height = 50)
        self.Places.append([gl.hei+gl.hei/6-75, 300, 150, 50])
        self.Widgets.append(labModVTW)

        labVec = Label(master = gl.canvas, text = "Enter a real 2x1 vector:")
        labVec.place(x = gl.hei+gl.hei/6-75, y = 400, width = 150, height = 50) 
        self.Places.append([gl.hei+gl.hei/6-75, 400, 150, 50])
        self.Widgets.append(labVec)

        entryV1 = Entry(master = gl.canvas, bg = "white") 
        entryV1.place(x = gl.hei+gl.hei/6-75, y = 450, width = 100, height = 50) 
        self.Places.append([gl.hei+gl.hei/6-75, 450, 100, 50])
        self.Widgets.append(entryV1)
        self.e1 = entryV1

        entryV2 = Entry(master = gl.canvas, bg = "white") 
        entryV2.place(x = gl.hei+gl.hei/6-75, y = 500, width = 100, height = 50)
        self.Places.append([gl.hei+gl.hei/6-75, 500, 100, 50])
        self.Widgets.append(entryV2)
        self.e2 = entryV2

        addBut = Button(master = gl.canvas, text = "Add Vector", command = self.addVec) 
        addBut.place(x = gl.hei+gl.hei/6+50, y = 450, width = 100, height = 50) 
        self.Places.append([gl.hei+gl.hei/6+50, 450, 100, 50])
        self.Widgets.append(addBut)

        transBut = Button(master = gl.canvas, text = "Transform", command = self.tranformVectors) 
        transBut.place(x = gl.hei+gl.hei/6-75, y = 550, width = 100, height = 50) 
        self.Places.append([gl.hei+gl.hei/6-75, 550, 100, 50])
        self.Widgets.append(transBut)

    #adds the input vector
    def addVec(self):
        try: 
            v1 = float(self.e1.get())
            v2 = float(self.e2.get())
            vec = np.array([v1,v2])
            if abs(v1) > self.gl.maxV: self.gl.maxV = abs(v1)
            if abs(v2) > self.gl.maxV: self.gl.maxV = abs(v2)
            self.vectors.append(vec)
        except Exception:
            pass

    def tranformVectors(self):
        if self.trans: self.trans = False
        else: self.trans = True
    
    
    
    #calculates the list of transformed vectors using the vector list
    def addtransVec(self):
        self.transvectors = []
        for v in self.vectors:
            tv = self.helper.transformVec(v)
            if abs(tv[0]) > self.gl.maxV: self.gl.maxV = abs(tv[0]); 
            if abs(tv[1]) > self.gl.maxV: self.gl.maxV = abs(tv[1]); 
            self.transvectors.append(tv)

    def drawVectors(self, vecs, color):
        for v in vecs:
            self.helper.drawVec(v, color)

    def resetMaxV(self):
        max = 10
        for v in self.vectors:
            if v[0] > max: max = v[0]
            if v[1] > max: max = v[1]

        if self.trans:
            for v in self.transvectors:
                if v[0] > max: max = v[0]
                if v[1] > max: max = v[1]

        self.gl.maxV = max
    
    def open(self):
        i = 0
        for wid in self.Widgets:
            l = self.Places[i]
            wid.place(x = l[0], y = l[1], width = l[2], height = l[3])
            self.gl.OpenWidgets.append(wid)
            i += 1  
    
    def animateVecTrans(self):
        pass

    def main(self):
        if self.animate:
            pass
        else:
            self.addtransVec()
            self.drawVectors(self.vectors, "white")
            if self.trans: self.drawVectors(self.transvectors, "blue")
            self.resetMaxV()

    def reset(self):
        self.vectors = []
        pass

    def toStr(self):
        return "Vector Transformation Class"
