#Test file for algorithmic "art"
#Uncomment functions at bottom of code to change modes
#WORK IN PROGRESS


import cv2
import math
import numpy as np
import random
from PIL import Image
import turtle
t = turtle.Turtle()
t.ht()
def curve(dist, direc, width,leftright):
    if leftright <0:
        leftright = -1
    else:
        leftright = 1
    radius = (((dist*dist+4*width*width)/(8*width)))
    theta = 2*math.degrees(math.acos(1 - width/radius))
    t.seth(direc-theta/2*leftright)
    t.circle(leftright*radius,theta)
    
class Point:
  def __init__(self, x,y,connections):
    self.x = x
    self.y = y
    self.connections = connections



im = cv2.imread("dawg.jpg")
print(type(im))
imbw = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY);
#cv2.imshow("daaaawg",imbw)

thresh = 50
jitterLow = -50
jitterHigh = 100


point = []
randJit = random.randint(jitterLow,jitterHigh)
pointArray = np.zeros([500,500])
for i in range(0,500): 
    for j in range(0,500): 
        x = 6#random.randint(2,5)
        if i%x ==0 and j%x==0 :
            pointArray[i][j] = round(abs(imbw[i,j]+thresh)/256,0)#            pointArray[i][j] = round(abs(imbw[i,j]+thresh+randJit)/256,0)
            point.append(Point(i,j,0))
        else:
            pointArray[i][j] = 1
        
#im = Image.fromarray(pointArray * 255)            
#im.show()


def lineDraw2(point):
    for tur in range(int(len(point)/10)):
        print(point[tur].x,point[tur].y,point[tur].connections)


#lineDraw2(point)
def lineDraw1(Array):
    wn = turtle.Screen()
    wn.tracer(0)


    s = turtle.Screen()
    s.setup(len(Array),len(Array))
    origin = -len(Array)/2
    for i in range(10,490): 
        for j in range(10,490): 
            if Array[i][j] == 0:
                t.pu()
                t.goto(origin+j,-(origin+i))
                for d in range(-10,10):
                    if Array[i+d][j] == 0:
                        t.pd()
                        t.goto(origin+j,-(origin+i+d))
                        t.goto(origin+j,-(origin+i))
                        t.pu()
                    elif Array[i][j+d] == 0:
                        t.pd()
                        t.goto(origin+j+d,-(origin+i))
                        t.goto(origin+j,-(origin+i))                     
                        t.pu()
#lineDraw1(pointArray)

def curveDraw1(Array):
    wn = turtle.Screen()
    wn.tracer(0)


    s = turtle.Screen()
    s.setup(len(Array),len(Array))
    origin = -len(Array)/2
    for i in range(10,490): 
        for j in range(10,490): 
            if Array[i][j] == 0:
                t.pu()
                t.goto(origin+j,-(origin+i))
                for d in range(-10,10):
                    if Array[i+d][j] == 0:
                        t.pu()
                        t.goto(origin+j,-(origin+i))
                        t.pd()
                        if d <0:
                            curve(d,-90,2,1)
                        else:
                            curve(d,90,2,-1)
                    elif Array[i][j+d] == 0:
                        t.pu()
                        t.goto(origin+j,-(origin+i))
                        t.pd()
                        if d <0:
                            curve(d,180,2,-1)
                        else:
                            curve(d,0,2,1)

def circleDraw(Array):
    wn = turtle.Screen()
    wn.tracer(0)


    s = turtle.Screen()
    s.setup(len(Array),len(Array))
    origin = -len(Array)
    print(origin)
    for i in range(0,int(-origin)):         
        t.pu()
        t.goto(i,0)
        t.pd()
        t.seth(90)
        t.circle(i)

# COMMENT OR UNCOMMENT FUNCTIONS BELOW


lineDraw1(pointArray)
#curveDraw1(pointArray)

