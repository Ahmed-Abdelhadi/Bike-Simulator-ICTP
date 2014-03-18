import math
import random

class Bike(object):
  #def CalcDist(self,x1,y1,x2,y2):
   # distance=((x2-x1)**2+(y2-y1)**2)**0.5
   # return distance

  def __init__(self):
    #self.x=[x1,x2,x3,x4]
    #self.y=[y1,y2,y3,y4]
    self.pos=[[4., 4.], [9., 4.], [9., 9.], [4., 9.]]
    self.angle=[0. for i in xrange (4)]
    self.r=[1., 1., 0., 0.]
    self.m=[1., 1., 1., 1.]
    #self.vx=[vx1,vx2,vx3,vx4]
    #self.vy=[vy1,vy2,vy3,vy4]
    self.v=[[0. for i in xrange (2)] for i in xrange(4)]
    self.w=[0. for i in xrange (4)]
    self.a=[[0. for i in xrange (2)] for i in xrange(4)]
    self.ang_a=[0. for i in xrange (4)]#[ang_a1,ang_a2,ang_a3,ang_a4]
    self.k=[[0. for i in xrange (4)] for i in xrange(4)]
    self.l=[[0. for i in xrange (4)] for i in xrange(4)]
    
    #self.SpringDist=[self.CalcDist(x1,y1,x2,y2),self.CalcDist(x1,y1,x3,y3),self.CalcDist(x1,y1,x4,y4),self.CalcDist(x2,y2,x3,y3),self.CalcDist(x2,y2,x4,y4),self.CalcDist(x3,y3,x4,y4)]
    #self.k=[1,1,1,1,1,1]
    for i in xrange (4):
      for j in xrange(4):
	self.k[i][j]=1
	dx=self.pos[j][0]-self.pos[i][0]
	dy=self.pos[j][1]-self.pos[i][1]
	dr = math.sqrt(dx*dx + dy*dy)
	self.l[i][j]=dr
    
  def GenerateBike():
    #GeneratePts()
    GenerateRadius()
    GenerateMass()
    GenerateSpring()    

  def GeneratePts(self, object,r, MaxWidth, MaxHeigth):
    for i in xrange(4):
      if i==0:
	xCoordinateL=r
	xCoordinateU=MaxWidth-r
	yCoordinateL=r
	yCoordinateU=MaxHeigth-r
	object.pos[i]=[random.randint(xCoordinateL, xCoordinateU), random.randint(yCoordinateL, yCoordinateU)]
      if i==1:
	xCoordinateL=r
	xCoordinateU=MaxWidth-r
	yCoordinateL=r
	yCoordinateU=MaxHeigth-r
	while True:
	  object.pos[i]=[random.randint(xCoordinateL, xCoordinateU), random.randint(yCoordinateL, yCoordinateU)]
	  D1=math.sqrt((object.pos[i][0]-object.pos[0][0])**2 + (object.pos[i][1]-object.pos[0][1])**2)
	  if D1>2*r:
	    break;

      if i==2:
	pass
      
      if i==3:
	pass
    

  def GenerateRadius(self,object):
    object.r=[3,3,0,0]
    #pass

  def GenerateMass(self,object):
    object.m=[10,10,10,10]
    #pass

  def GenerateSpring(self,object):
    for i in xrange (4):
      for j in xrange(4):
	object.k[i][j]=1
	dx=object.pos[j][0]-object.pos[i][0]
	dy=object.pos[j][1]-object.pos[i][1]
	dr = math.sqrt(dx*dx + dy*dy)
	object.l[i][j]=dr
  
  def RandomBike():
    pass
  
  def UniformBike():
    pass
  
def column(matrix, i):
    return [row[i] for row in matrix]
H=Bike()    
#print random.randint(4, 10)
#print column(H.pos,1)
print H.pos
H.GeneratePts(H,4,30,30)
print H.pos

print H.m
H.GenerateMass(H)
print H.m

print H.r
H.GenerateRadius(H)
print H.r

print H.l
print H.k
H.GenerateSpring(H)
print H.l
print H.k

