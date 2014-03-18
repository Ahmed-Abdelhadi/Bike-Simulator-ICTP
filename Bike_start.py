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
	pass
	 
    #print object.pos
    #pass
    
    
    
    #pass
#-------------- by Alex-----------
  def randomize(self):
    self.check()
    return

  def check(self):
    for i in xrange (4):
      for j in xrange(4):
	dx=self.pos[j][0]-self.pos[i][0]
	dy=self.pos[j][1]-self.pos[i][1]
	dr = math.sqrt(dx*dx + dy*dy)
	self.l[i][j]=dr
    return

  def set_result(self,l):
    self.res=l
    

  def get_result(self):
    try: 
        return self.res
    except:
	return 1.
#------------- end by Alex-------------------

  def GenerateRadius():
    pass

  def GenerateMass():
    pass

  def GenerateSpring():
    pass
  
def column(matrix, i):
    return [row[i] for row in matrix]
#H=Bike()    
#print random.randint(4, 10)
#print column(H.pos,1)

#H.GeneratePts(H,4,100,100)


