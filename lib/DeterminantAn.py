import numpy as np 
import tkinter as tk 
from tkinter import *
import math


class DeterminantAn:
    

    def __init__(self, gl, helper):
        self.gl = gl
        self.helper = helper
        self.Widgets = []
        self.Places = []
        labModDAW = Label(master = gl.canvas, text = "Determinant Animation") 
        self.Places.append([gl.hei+gl.hei/6-75, 300, 150, 50])
        self.Widgets.append(labModDAW)
        self.stage = 0
        self.maxStage = 10
    
    def getDet(self):
        return self.gl.matrix[0][0] * self.gl.matrix[1][1] - self.gl.matrix[0][1] * self.gl.matrix[1][0]

    def paintStart(self):
        p0 = self.helper.getCor(np.array([0,0]))
        p1 = self.helper.getCor(np.array([1,0]))
        p2 = self.helper.getCor(np.array([1,1]))
        p3 = self.helper.getCor(np.array([0,1]))
        points = [p0[0], p0[1], p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]]
        self.gl.canvas.create_polygon(points, fill = "blue")
        self.helper.drawVec(np.array([1,0]), "blue")
        self.helper.drawVec(np.array([0,1]), "blue")

    def paintEnd(self):
        v1 = self.helper.transformVec(np.array([1,0]))
        v2 = self.helper.transformVec(np.array([0,1]))
        p0 = self.helper.getCor(np.array([0,0]))
        p1 = self.helper.getCor(v2)
        p2 = self.helper.getCor(v1+v2)
        p3 = self.helper.getCor(v1)
        points = [p0[0], p0[1], p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]]
        self.gl.canvas.create_polygon(points, fill = "red")
        self.helper.drawVec(v1, "red")
        self.helper.drawVec(v2, "red")

    def open(self):
        i = 0
        for wid in self.Widgets:
            l = self.Places[i]
            wid.place(x = l[0], y = l[1], width = l[2], height = l[3])
            self.gl.OpenWidgets.append(wid)
            i += 1 

    def main(self):
        if(self.getDet() < 1): 
            self.paintStart()
            self.paintEnd()
        else: 
            self.paintEnd() 
            self.paintStart()
        """self.paintStage()
        if self.stage < self.maxStage:
            self.stage += 1
        if self.stage == self.maxStage:
            self.paintEnd()"""

    def reset(self):
        self.stage = 0
        pass

    def toStr(self):
        return "Determinant Animation Class"