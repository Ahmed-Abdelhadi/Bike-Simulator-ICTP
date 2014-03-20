#!/usr/bin/env python
# module Terrain for for group 4
#=================================================================
class terrain_class(object):
    """The class for terrain surface manipulation.

        Args:
           length (float): Length of terrain surfase.

           angle (float): Trend coeficient. Make it small.

           rand (float): Random amplitude of surface oscilation.

           improved (boolean): If 'True' - amplitude is increasing for long dictances.
    """

    def __init__(self,length = 1000, angle=0., rand =0., improved=False):
	from random import random
	self.tau = [(0., 0.) for _ in xrange(int(length/10)+1)]
	self.tau_length = [0. for _ in xrange(int(length/10)+1)]
	if not improved:
	    self.x = [i*10-10 for i in range(int(length/10)+1)]
	    self.y = [i*angle+rand*random()  for i in self.x]
	    self.y[0]=self.y[1]=self.y[2]=0.
	else:
	    self.x = [i*10-10 for i in range(int(length/10)+1)]
	    self.y = [0.  for i in self.x]
	    for i in range(1,int(length/10)+1):
		self.delta = i*0.2
		self.y[i] = self.y[i-1] + self.delta*random() - 0.5*self.delta
		self.tau[i] = (self.x[i]-self.x[i-1], self.y[i]-self.y[i-1])
		self.tau_length[i] = (self._dot(self.tau[i], self.tau[i]))**0.5 
		self.tau[i] = (self.tau[i][0]/self.tau_length[i],self.tau[i][1]/self.tau_length[i])

    def get(self):
	"""Return the terrain prifile

	Returns: 
	    ([x],[y]) (lists): Set of x and y coordinates.
	"""
	return self.x, self.y
#------------------------------------------------------
    def out(self,x):
	a = x
	low_bound = (self.x[0]+self.x[1])/2.
	hi_bound = (self.x[-2]+self.x[-1])/2.
	while hasattr(a, '__iter__'):
	    a = a[0]
	if a <= low_bound:
	    return 1
	if a >= hi_bound:
	    return 1
	return 0
#---------------------------------------------------------
    def check(self, x0,y0,r=0):
        """Find the distance to the terrain from the given point.

    Args:
       x0,y0 (float):  Coordinates of the point.

       r (float): Not used.

    Returns:
       (norm_x,norm_y) (float): Normalized normal vector

       distance (float):	Distance to surface (negative if point is below surface)

       (tau_x,tau_y) (float):   Normalized tangent vector
    """
	#find nearest
	x = self.x
	y = self.y
        result=[]
        n=int(round(x0/10.)+1)
	#dist,n = min([(abs(xi-x0),i) for i,xi in enumerate(x)])
	if n == 0 or n == len(x)-1:
	    print 'bike out of  terrain!!!'

	# n is nearest
	dist = self._check(n,x0,y0)
	if dist <> None:
#	    print dist
	    if dist[0][1]<0:
#		print 'bike under terrain!!!'
		dist[1] *=-1
            result.append(dist) 

	dist = self._check(n+1,x0,y0)
	if dist <> None:
#	    print dist
	    if dist[0][1]<0:
#	        print 'bike under terrain!!!'
		dist[1] *=-1
	    result.append(dist) 

	if result==[]:  	# vertex of terrain
	    norm = (x0-x[n],y0-y[n])
            norm_length=(norm[0]*norm[0]+norm[1]*norm[1])**0.5
            norm = (norm[0]/norm_length, norm[1]/norm_length)
            tau = (norm[1],-norm[0])
    	    if norm[1]<0:
		tau = (-norm[1],norm[0])
#	        print 'bike under terrain!!!'
		norm_length *=-1
	    result.append((norm,norm_length,tau))
	return result

    def save_json(self, path='terrain.sav'):
        """Write terrain surface in file.
    """
	import json
	a = {'x':self.x,'y':self.y}
	x=json.dumps(a, sort_keys=True, indent=4)
	with open(path, 'wb') as fp:
	    fp.write(x)

    def load_json(self, path='terrain.sav'):
        """Read terrain surface from file.
    """
	import json
	with open(path, 'rb') as fp:
	    a = json.load(fp)
	self.x=a['x']
	self.y=a['y']
	return

    def _check(self, n, x0, y0):
    #    print x1,y1,x2,y2,x0,y0
	x=self.x
        y=self.y
	v1 = (x0-x[n-1],y0-y[n-1])

	tau = self.tau[n]
	tau_length = self.tau_length[n]
	
	v1_proj=(v1[0]*tau[0]+v1[1]*tau[1])
	if v1_proj > tau_length:
	    return
	if v1_proj < 0:
	    return
	norm = (v1[0]-v1_proj*tau[0],v1[1]-v1_proj*tau[1])
	norm_length = (norm[0]*norm[0]+norm[1]*norm[1])**0.5
	norm = (norm[0]/norm_length,norm[1]/norm_length)
	return list((norm,norm_length,tau))
    
    def _dot(self, a, b):
	return a[0]*b[0] + a[1]*b[1]
    
if __name__=='__main__':	#run as a program 
    import pylab as py 
    from random import random
    import matplotlib.patches as mpatches


    #test the module 
    a=terrain_class(length =100, angle =0.5)

    a.save_json()
    a.load_json()
    print a.x,a.y


    for i in range(10):
	py.plot(a.x,a.y)
	b=(45.+random(),20+10.*random(),2.)
	print a.check(*b)
#	py.scatter(b[0], b[1], s=(4*b[2])**2*3.14151, alpha=0.5)
#        py.Circle((40, 0), 10, fc="g", ec="r", lw=5)
        ax = py.subplot(111)
        c = mpatches.Circle((b[0], b[1]), b[2], fc="g", ec="r", lw=3)
        ax.add_patch(c)
        py.show()
