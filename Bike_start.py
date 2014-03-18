import math
import random

class Bike(object):
  
  def __init__(self):
    self.pos=[[4., 4.], [9., 4.], [9., 9.], [4., 9.]]
    self.angle=[0. for i in xrange (4)]
    self.r=[1., 1., 0., 0.]
    self.m=[1., 1., 1., 1.]
    self.v=[[0. for i in xrange (2)] for i in xrange(4)]
    self.w=[0. for i in xrange (4)]
    self.a=[[0. for i in xrange (2)] for i in xrange(4)]
    self.ang_a=[0. for i in xrange (4)]#[ang_a1,ang_a2,ang_a3,ang_a4]
    self.k=[[0. for i in xrange (4)] for i in xrange(4)]
    self.l=[[0. for i in xrange (4)] for i in xrange(4)]
    
    for i in xrange (4):
      for j in xrange(4):
	self.k[i][j]=1
	dx=self.pos[j][0]-self.pos[i][0]
	dy=self.pos[j][1]-self.pos[i][1]
	dr = math.sqrt(dx*dx + dy*dy)
	self.l[i][j]=dr
 