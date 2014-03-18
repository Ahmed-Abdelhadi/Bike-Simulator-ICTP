import math
import random

class Bike(object):
  #def CalcDist(self,x1,y1,x2,y2):
   # distance=((x2-x1)**2+(y2-y1)**2)**0.5
   # return distance

  def __init__(self):
    #self.x=[x1,x2,x3,x4]
    #self.y=[y1,y2,y3,y4]
    self.pos=[[4., 4.], [9., 4.], [4., 9.], [9., 9.]]
    self.angle=[0.]*4
    self.r=[1., 1., 0., 0.]
    self.m=[1., 1., 1., 1.]
    #self.vx=[vx1,vx2,vx3,vx4]
    #self.vy=[vy1,vy2,vy3,vy4]
    self.v=[[0., 0.]]*4
    self.w=[0.]*4
    self.a=[[0., 0.]]*4
    self.ang_a=[0.]*4#[ang_a1,ang_a2,ang_a3,ang_a4]
    self.k=[[0.]*4]*4
    self.l=[[0.]*4]*4
    
    #self.SpringDist=[self.CalcDist(x1,y1,x2,y2),self.CalcDist(x1,y1,x3,y3),self.CalcDist(x1,y1,x4,y4),self.CalcDist(x2,y2,x3,y3),self.CalcDist(x2,y2,x4,y4),self.CalcDist(x3,y3,x4,y4)]
    #self.k=[1,1,1,1,1,1]
    for i in xrange (4):
      for j in xrange(4):
	self.k[i][j]=1
	dx=self.p[j][0]-self.p[i][0]
	dy=self.p[j][1]-self.p[i][1]
	dr = math.sqrt(dx*dx + dy*dy)
	self.l[i][j]=dr
    
  def GenerateBike():
    #GeneratePts()
    GenerateRadius()
    GenerateMass()
    GenerateSpring()    

  def GeneratePts(self,r,MaxLength,MaxWidth):
    pass
    
    
    
    #pass

  def GenerateRadius():
    pass

  def GenerateMass():
    pass

  def GenerateSpring():
    pass
    
H=Bike()    
#print random.random()
