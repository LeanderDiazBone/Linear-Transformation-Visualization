import math
import numpy as np

class Helper:

    def __init__(self, gl):
        self.gl = gl

    #calculates the coordinates on the coordinate system using the paramters in gl
    def getCor(self, v = np.array):
        c = []
        c.append(self.gl.hei/2+v[0]*(self.gl.a/float(self.gl.x)))
        c.append(self.gl.hei/2-v[1]*(self.gl.a/float(self.gl.x)))
        return c
    
    #draws one Vector (np.array with Dimension 2x1)
    def drawVec(self, v = np.array, color = ""):
        if (v[0] == 0 and v[1] == 0) or (v[0] > self.gl.maxV or v[1] > self.gl.maxV): return 
        #print(v[0]); print(v[1]); print(self.gl.maxV); print()
        c = self.getCor(v)
        self.gl.canvas.create_line(self.gl.hei/2, self.gl.hei/2, c[0], c[1], fill = color)
        #draw a arrow on top of the vector
        #calculating start point: 1) get unit vector of v, 2) subtract math.squrt(12.5)
        uv = v * (1/math.sqrt(v[0]*v[0]+v[1]*v[1]))
        sp = v - math.sqrt(100)*self.gl.x/float(self.gl.a)*uv
        #print(v[0], v[1], uv[0], uv[1], sp[0], sp[1])
        #get orthogonal unit vector 1) get an orthogonal vector 2) divide by length
        ov = np.array([1,1])
        try:
            if v[0] == 0 and v[1] == 0: raise Exception
            elif v[0] == 0: ov = np.array([1,0])
            else: ov = np.array([-v[1]/v[0],1])
            uov = ov * (1/math.sqrt(ov[0]*ov[0]+ov[1]*ov[1]))
            cuov = self.getCor(uov)
            cp = self.getCor(sp)
            p1 = np.array([sp[0]+(uov[0]*math.sqrt(12.5)*self.gl.x/float(self.gl.a)), sp[1]+(uov[1]*math.sqrt(12.5)*self.gl.x/float(self.gl.a))])
            p2 = np.array([sp[0]-(uov[0]*math.sqrt(12.5)*self.gl.x/float(self.gl.a)), sp[1]-(uov[1]*math.sqrt(12.5)*self.gl.x/float(self.gl.a))])
            cp1 = self.getCor(p1); cp2 = self.getCor(p2)
            self.gl.canvas.create_line(cp1[0], cp1[1], c[0], c[1], fill = color)
            self.gl.canvas.create_line(cp2[0], cp2[1], c[0], c[1], fill = color)
        except Exception:
            pass

    #transforms the vector v given as a parameter
    def transformVec(self, v = np.array):
        tv = self.gl.matrix.dot(v)
        return tv
