from math import sqrt

class physics(object):
    
    def __init__(self, bike, terrain):
	self.dt = 0.001
	self.g = 10.0
	self.wall_elastic= 10000.0
	self.wall_damp = 100.0
	self.motor_torque = 1.0
	self.bike = bike
	self.terrain = terrain
	
    
    def stuck(self):
	bike = self.bike
	for i in xrange(2,4):
	    for norm, dist, tan in self.terrain.check(bike.pos[i][0], bike.pos[i][1], bike.r[i]):
		if dist<=0.0:
		    return True
	return False
    
    
    def step(self):
	self._velocity()
	self._ang_velocity
	
	self._position()
	self._angle()
	
	self._accelaration()
	self._ang_accelaration()
	
	self._velocity()
	self._ang_velocity()
    
    
    def _wallforce(self, i):
	bike = self.bike
	fxwall = 0.0
	fywall = 0.0
	for norm, dist, tan in self.terrain.check(bike.pos[i][0], bike.pos[i][1], bike.r[i]):
	    if dist<=bike.r[i]:
		dr = bike.r[i] - dist
		elastic_n = self.wall_elastic*dr
		v_n = self._dot(bike.v[i], norm)
		damp_n = self.wall_damp*v_n
		fn = elastic_n - damp_n
		fxwall += fn*norm[0]
		fywall += fn*norm[1]
	return fxwall, fywall
    
    
    def _accelaration(self):
	bike = self.bike
	fx = [0.0]*4
	fy = [0.0]*4
	for i in xrange(2):
	    fx[i], fy[i] = self._wallforce(i)
	for i in xrange(4):
	    for j in xrange(i+1,4):
		dx = bike.pos[j][0]-bike.pos[i][0]
		dy = bike.pos[j][1]-bike.pos[i][1]
		r = sqrt(dx*dx + dy*dy)
		dfx = bike.k[i][j]*(r-bike.l[i][j])*dx/r
		dfy = bike.k[i][j]*(r-bike.l[i][j])*dy/r
		fx[i] += dfx
		fy[i] += dfy
		fx[j] -= dfx
		fy[j] -= dfy
	for i in xrange(4):
	    bike.a[i][0] = fx[i]/bike.m[i]
	    bike.a[i][1] = fy[i]/bike.m[i] - self.g
	#print (fx,fy)
    
    
    def _ang_accelaration(self):
	for i in xrange(4):
	    self.bike.ang_a[i] = 0
    
    
    def _velocity(self):
	for i in xrange(4):
	    for d in xrange(2):
		self.bike.v[i][d] += self.bike.a[i][d]*self.dt/2
    
    
    def _ang_velocity(self):
	for i in xrange(2):
	    self.bike.w[i] += self.bike.ang_a[i]*self.dt/2
    
    
    def _position(self):
	for i in xrange(4):
	    for d in xrange(2):
		self.bike.pos[i][d] += self.bike.v[i][d]*self.dt
    
    
    def _angle(self):
	for i in xrange(2):
	    self.bike.angle[i] += self.bike.w[i]*self.dt
    
    
    def _dot(self, a, b):
	return a[0]*b[0] + a[1]*b[1]
    
    
if __name__=='__main__':
    from Bikestart import Bike
    from terrain import Terrain
    t = Terrain()
    bike = Bike()
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
	if physics.stuck():
	    break
    
    
    