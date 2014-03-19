from math import sqrt

class physics_class(object):
    
    def __init__(self, bike, terrain):
	self.dt = 0.001
	self.g = 10.0
	self.wall_elastic= 100000.0
	self.wall_damp = 10000.0
	self.motor_torque = 100.0
	self.bike = bike
	self.terrain = terrain
	self.xcm0 = self._rcm()[0]
	self.distance = 0.0
	
    
    def stuck(self):
	bike = self.bike
	for i in xrange(2,4):
	    for norm, dist, tan in self.terrain.check(bike.position[i][0], bike.position[i][1], bike.radius[i]):
		if dist<=0.0:
		    return True
	return False
    
    
    def step(self):
	self._velocity()
	self._ang_velocity
	
	self._position()
	self._angle()
	
	self._acceleration()
	self._ang_acceleration()
	
	self._velocity()
	self._ang_velocity()
    
    
    def get_result(self):
	return self._rcm()[0] - self.xcm0
    
    
    def _rcm(self):
	bike = self.bike
	m_total = 0.0
	rcm = [0.0, 0.0]
	for i in xrange(4):
	    m_total += bike.mass[i]
	    for d in xrange(2):
		rcm[d] += bike.mass[i]*bike.position[i][d]
	for d in xrange(2):
	    rcm[d] /= m_total
	return rcm
    
    
    def _wallforce(self, i):
	bike = self.bike
	fxwall = 0.0
	fywall = 0.0
	n = len(self.terrain.check(bike.position[i][0], bike.position[i][1], bike.radius[i]))
	for norm, dist, tan in self.terrain.check(bike.position[i][0], bike.position[i][1], bike.radius[i]):
	    if dist<=bike.radius[i]:
		dr = bike.radius[i] - dist
		elastic_n = self.wall_elastic*dr
		v_n = self._dot(bike.velocity[i], norm)
		damp_n = self.wall_damp*v_n
		fn = elastic_n - damp_n
		ft = 0.0
		tan = self._n2t(norm)
		if i==0:
		    ft = self.motor_torque/bike.radius[i]/n
		fxwall += fn*norm[0] + ft*tan[0]
		fywall += fn*norm[1] + ft*tan[1]
	return fxwall, fywall
    
    
    def _acceleration(self):
	bike = self.bike
	fx = [0.0]*4
	fy = [0.0]*4
	for i in xrange(2):
	    fx[i], fy[i] = self._wallforce(i)
	for i in xrange(4):
	    for j in xrange(i+1,4):
		dx = bike.position[j][0]-bike.position[i][0]
		dy = bike.position[j][1]-bike.position[i][1]
		r = sqrt(dx*dx + dy*dy)
		dfx = bike.spring_const[i][j]*(r-bike.spring_length[i][j])*dx/r
		dfy = bike.spring_const[i][j]*(r-bike.spring_length[i][j])*dy/r
		fx[i] += dfx
		fy[i] += dfy
		fx[j] -= dfx
		fy[j] -= dfy
	for i in xrange(4):
	    bike.acceleration[i][0] = fx[i]/bike.mass[i]
	    bike.acceleration[i][1] = fy[i]/bike.mass[i] - self.g
	#print (fx,fy)
    
    
    def _ang_acceleration(self):
	for i in xrange(4):
	    self.bike.ang_acceleration[i] = 0
    
    
    def _velocity(self):
	for i in xrange(4):
	    for d in xrange(2):
		self.bike.velocity[i][d] += self.bike.acceleration[i][d]*self.dt/2
    
    
    def _ang_velocity(self):
	for i in xrange(2):
	    self.bike.ang_velocity[i] += self.bike.ang_acceleration[i]*self.dt/2
    
    
    def _position(self):
	for i in xrange(4):
	    for d in xrange(2):
		self.bike.position[i][d] += self.bike.velocity[i][d]*self.dt
    
    
    def _angle(self):
	for i in xrange(2):
	    self.bike.angle[i] += self.bike.ang_velocity[i]*self.dt
    
    
    def _dot(self, a, b):
	return a[0]*b[0] + a[1]*b[1]
    
    
    def _n2t(self, a):
	return a[1], -a[0]
    
if __name__=='__main__':
    from Bikestart import Bike
    from terrain import Terrain
    from animateobj import animatebike
    t = Terrain()
    bike = Bike()
    #visual = animatebike(bike, t)
    physics = physics(bike, t)
    f = open('test.xyz','w')
    for time in xrange(10000):
	physics.step()
	f.write("5\n%d\n" % time)
	f.write("1\t%f\t%f\t0.0\n" % (bike.pos[0][0], bike.pos[0][1]))
	f.write("1\t%f\t%f\t0.0\n" % (bike.pos[1][0], bike.pos[1][1]))
	f.write("2\t%f\t%f\t0.0\n" % (bike.pos[2][0], bike.pos[2][1]))
	f.write("2\t%f\t%f\t0.0\n" % (bike.pos[3][0], bike.pos[3][1]))
	f.write("3\t0.0\t0.0\t0.0\n")
	#visual.visualize()
	if physics.stuck():
	    break
    
    
    