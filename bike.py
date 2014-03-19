import math
import random

class bike_class(object):
    def __init__(self):
	self._position = [[4., 4.], [9., 4.], [9., 9.], [4., 9.]]
	self._radius = [1., 1., 0., 0.]
	self._mass = [10., 10., 1., 1.]
	self._angle = [0. for i in xrange (4)]
	self._velocity = [[0. for i in xrange (2)] for i in xrange(4)]
	self._ang_velocity = [0. for i in xrange (4)]
	self._acceleration = [[0. for i in xrange (2)] for i in xrange(4)]
	self._ang_acceleration = [0. for i in xrange (4)]#[ang_a1,ang_a2,ang_a3,ang_a4]
	self._spring_const = [[0. for i in xrange (4)] for i in xrange(4)]
	self._spring_length = [[0. for i in xrange (4)] for i in xrange(4)]
	
	for i in xrange (4):
	    for j in xrange(4):
		self.spring_const[i][j] = 1000.
		dx=self.position[j][0]-self.position[i][0]
		dy=self.position[j][1]-self.position[i][1]
		dr = math.sqrt(dx*dx + dy*dy)
		self._spring_length[i][j]=dr
		

    @property
    def position(self):
	return self._position
    
    @property
    def velocity(self):
	return self._velocity
	
    @property
    def acceleration(self):
	return self._acceleration

    @property
    def angle(self):
	return self._angle
	
    @property
    def ang_velocity(self):
	return self._ang_velocity

    @property
    def ang_acceleration(self):
	return self._ang_acceleration	
    
    @property
    def radius(self):
	return self._radius
	
    @property
    def mass(self):
	return self._mass
	
    @property
    def spring_const(self):
	return self._spring_const
	
    @property
    def spring_length(self):
	return self._spring_length
	

    @position.setter
    def position(self, position):
	self._position = position
 
    @velocity.setter
    def velocity(self, velocity):
	self._velocity = velocity
	
    @acceleration.setter
    def acceleration(self, acceleration):
	self._acceleration = acceleration
 
    @angle.setter
    def angle(self, angle):
	self._angle = angle
	
    @ang_velocity.setter
    def ang_velocity(self, ang_velocity):
	self._ang_velocity = ang_velocity

    @ang_acceleration.setter
    def ang_acceleration(self, ang_acceleration):
	self._ang_acceleration = ang_acceleration	
    
    @radius.setter
    def radius(self, radius):
	self._radius = radius
	
    @mass.setter
    def mass(self, mass):
	self._mass = mass
	
    @spring_const.setter
    def spring_const(self, spring_const):
	self._spring_const = spring_const
	
    @spring_length.setter
    def spring_length(self, spring_length):
	self._spring_length = spring_length
	

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
		self._spring_length[i][j]=dr
	return

    def set_result(self,result):
	self.result=result
    

    def get_result(self):
	try: 
	    return self.res
	except:
	    return 1.
#------------- end by Alex-------------------

if __name__=="__main__":
    #pass
    H=bike_class()
    print H.position
    print H.radius
    
