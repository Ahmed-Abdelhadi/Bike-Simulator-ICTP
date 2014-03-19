import math
import random

class bike_class(object):
  
  def __init__(self):
    self.position=[[4., 4.], [9., 4.], [9., 9.], [4., 9.]]
    self.angle=[0. for i in xrange (4)]
    self.radius=[1., 1., 0., 0.]
    self.mass=[1., 1., 1., 1.]
    self.velocity=[[0. for i in xrange (2)] for i in xrange(4)]
    self.angular_velocity=[0. for i in xrange (4)]
    self.acceleration=[[0. for i in xrange (2)] for i in xrange(4)]
    self.angular_acceleration=[0. for i in xrange (4)]#[ang_a1,ang_a2,ang_a3,ang_a4]
    self.spring_constant=[[0. for i in xrange (4)] for i in xrange(4)]
    self.length=[[0. for i in xrange (4)] for i in xrange(4)]
    
    for i in xrange (4):
      for j in xrange(4):
	self.spring_constant[i][j]=1
	dx=self.position[j][0]-self.position[i][0]
	dy=self.position[j][1]-self.position[i][1]
	dr = math.sqrt(dx*dx + dy*dy)
	self.length[i][j]=dr

#-------------- by Alex-----------
  def randomize(self):
    self.check()
    return

  def check(self):
    for i in xrange (4):
      for j in xrange(4):
	dx=self.position[j][0]-self.position[i][0]
	dy=self.position[j][1]-self.position[i][1]
	dr = math.sqrt(dx*dx + dy*dy)
	self.length[i][j]=dr
    return

  def set_result(self,length):
    self.res=length
    

  def get_result(self):
    try: 
        return self.res
    except:
	return 1.
#------------- end by Alex-------------------

H=bike()
print H.position
