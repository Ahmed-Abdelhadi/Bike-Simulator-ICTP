#!/usr/bin/env python
# module Terrain for for group 4
#import numpy as np
def _check(x1,y1,x2,y2,x0,y0):
#    print x1,y1,x2,y2,x0,y0
    v1 = (x0-x1,y0-y1)

    tau = (x2-x1,y2-y1)
    tau_length =(tau[0]*tau[0]+tau[1]*tau[1])**0.5 
    tau = (tau[0]/tau_length,tau[1]/tau_length)

    v1_proj=(v1[0]*tau[0]+v1[1]*tau[1])
    if v1_proj > tau_length:
	return
    if v1_proj < 0:
	return
    norm = (v1[0]-v1_proj*tau[0],v1[1]-v1_proj*tau[1])
    norm_length = (norm[0]*norm[0]+norm[1]*norm[1])**0.5
    norm = (norm[0]/norm_length,norm[1]/norm_length)
    return list((norm,norm_length,tau))
#=================================================================
class Terrain():

    def __init__(self,length = 100, angle=0., rand =0.):
	from random import random
	self.x = [i*10 for i in range(int(length/10))]
	self.y = [i*angle+rand*random()  for i in self.x]

    def get_terrain(self):
	return self.x, self.y

    def check(self, x0,y0,r=0):
	#find nearest
        x=self.x
        y=self.y
	result=[]
	dist,n = min([(abs(xi-x0),i) for i,xi in enumerate(x)])
	# n is nearest
	dist = _check(x[n-1],y[n-1],x[n],y[n],x0,y0)
	if dist <> None:
#	    print dist
	    if dist[0][1]<0:
		print 'bike under terrain!!!'
		dist[1] *=-1
            result.append(dist) 

	dist = _check(x[n],y[n],x[n+1],y[n+1],x0,y0)
	if dist <> None:
#	    print dist
	    if dist[0][1]<0:
	        print 'bike under terrain!!!'
		dist[1] *=-1
	    result.append(dist) 

	if result==[]:  	# vertex of terrain
	    norm = (x0-x[n],y0-y[n])
            norm_length=(norm[0]*norm[0]+norm[1]*norm[1])**0.5
            norm = (norm[0]/norm_length, norm[1]/norm_length)
	    if norm[1]<>0:
       	        tau = (1.,norm[0]/norm[1])
	    else:
		tau = (0.,1.)
            tau_length=(tau[0]*tau[0]+tau[1]*tau[1])**0.5
            tau = (tau[0]/tau_length, tau[1]/tau_length)

    	    if norm[1]<0:
	        print 'bike under terrain!!!'
		norm_length *=-1

	    result.append((norm,norm_length,tau))
	return result


if __name__=='__main__':	#run as a program 
    import pylab as py 
    from random import random
    import matplotlib.patches as mpatches

    #test the module 
    a=Terrain(length =100, angle =0.5)
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
