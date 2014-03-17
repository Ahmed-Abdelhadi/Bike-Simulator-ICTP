class physics(object):
    def __init__(self, bike, terrain):
	self.g = 10.0
	self.wallk = 100.0
	self.wallc = 100.0
	
    def accelaration():
	for i in xrange(4):
	    for j in xrange(i+1,4):
		dx = pos[j][0]-pos[i][0]
		dy = pos[j][1]-pos[i][0]
		r = sqrt(dx*dx + dy*dy)
		dfx = k[i][j]*(dr-l[i][j])*dx/r
		dfy = k[i][j]*(dr-l[i][j])*dy/r
		fx[i][j] += dfx
		fy[i][j] += dfy
		fx[j][i] -= dfx
		fy[j][i] -= dfy