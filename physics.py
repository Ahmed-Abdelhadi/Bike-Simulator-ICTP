from math import sqrt

class physics(object):
    
    def __init__(self, bike, terrain):
	self.g = 10.0
	self.wall_elastic= 100.0
	self.wall_damp = 100.0
	self.pos = bike.pos
	self.angle = bike.angle
	self.v = bike.v
	self.w = bike.w
	self.a = bike.a
	self.ang_a = bike.ang_a
	self.r = bike.r
	self.m = bike.m
	self.k = bike.k
	self.l = bike.l
	self.terrain = terrain
	self.fx = [0.0]*4
	self.fy = [0.0]*4

    
    def stuck(self):
	for i in xrange(2,4):
	    for p in self.terrain.check(self.pos[i][0], self.pos[i][1], self.r[i]):
		if p[1]<=0.0:
		    return True
	return False
    
    
    def step(self):
	_velocity()
	_ang_velocity
	
	_position()
	_angle()
	
	_accelaration()
	_ang_accelaration()
	
	_velocity()
	_ang_velocity()
    
    
    def _wallforce(self, i):
	self.fx = 0.0
	self.fy = 0.0
	for p in self.terrain.check(self.pos[i][0], self.pos[i][1], self.r[i]):
	    if p[1]<=self.r[i]:
		self.dr = self.r[i]-p[i]
		self.elastic_n = self.wall_elastic*dr
		self.v_n = _dot(self.v[i], p[0])
		self.damp_n = self.wall_damp*v_n
		self.fx += self.elastic_n*p[0][0] - self.damp_n*p[0][0]
		self.fy += self.elastic_n*p[0][1] - self.damp_n*p[0][1]
	return fx, fy
    
    
    def _accelaration(self):
	for i in xrange(2):
	    self.fx[i], self.fy[i] = _wallforce(i)
	for i in xrange(4):
	    for j in xrange(i+1,4):
		self.dx = self.pos[j][0]-self.pos[i][0]
		self.dy = self.pos[j][1]-self.pos[i][0]
		self.r = sqrt(self.dx*self.dx + self.dy*self.dy)
		self.dfx = self.k[i][j]*(self.l[i][j]-self.r)*self.dx/self.r
		self.dfy = self.k[i][j]*(self.l[i][j]-self.r)*self.dy/self.r
		self.fx[i] += self.dfx
		self.fy[i] += self.dfy
		self.fx[j] -= self.dfx
		self.fy[j] -= self.dfy
	for i in xrange(4):
	    self.a[i][0] = self.fx[i]/self.m[i]
	    self.a[i][1] = self.fy[i]/self.m[i] - self.g
    
    
    def _ang_accelaration(self):
	for i in xrange(4):
	    self.ang_a[i] = 0
    
    
    def _velocity(self):
	for i in xrange(4):
	    for d in xrange(2):
		self.v[i][d] += self.a[i][d]*self.dt/2
    
    
    def _ang_velocity(self):
	for i in xrange(2):
	    self.w[i] += self.ang_a[i]*self.dt/2
    
    
    def _position(self):
	for i in xrange(4):
	    for d in xrange(2):
		self.pos([i][d] += self.v[i]*self.dt)
    
    
    def _angle(self):
	for i in xrange(2):
	    self.angle[i] += self.w[i]*self.dt
    
    
    def _dot(self, a, b):
	return a[0]*b[0] + a[1]*b[1]
    