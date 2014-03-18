#!/usr/bin/env python
# module Terrain for for group 4
def check(x1,y1,x2,y2,x0,y0):
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

    def __init__(self):
	self.x = [i*10 for i in range(10)]
	self.y = [0.  for i in self.x]

    def check(self, x0,y0,r=0):
	#find nearest
        x=self.x
        y=self.y
	result=[]
	dist,n = min([(abs(xi-x0),i) for i,xi in enumerate(x)])
	# n is nearest
	dist = check(x[n-1],y[n-1],x[n],y[n],x0,y0)
	if dist <> None:
#	    print dist
	    if dist[0][1]<0:
		print 'bike under terrain!!!'
		dist[1] *=-1
            result.append(dist) 

	dist = check(x[n],y[n],x[n+1],y[n+1],x0,y0)
	if dist <> None:
#	    print dist
	    if dist[0][1]<0:
	        print 'bike under terrain!!!'
		dist[1] *=-1
	    result.append(dist) 

	if result==[]:  	# vertex of terrain
	    norm = (x0-x[n],y0-y[n])
            norm_length=(norm[0]*norm[0]+norm[1]*norm[1])**0.5
            norm = (norm[0]/norm_length, norm[1]/norm_lenth)
	    if norm[1]<>0:
       	        tau = (1.,norm[0]/norm[1])
	    else:
		tau = (0.,1.)
            tau_length=(tau[0]*tau[0]+tau[1]*tau[1])**0.5
            tau = (tau[0]/tau_length, tau[1]/tau_lenth)

    	    if norm[1]<0:
	        print 'bike under terrain!!!'
		norm_lenth *=-1

	    result.append((norm,norm_lenth,tau))
	return result


if __name__=='__main__':	#run as a program 
    import pylab as py 
    from random import random
    #test the module 
    a=Terrain()
    for i in range(10):
	py.plot(a.x,a.y)
	b=(40+random(),3.*random(),2.)
	print a.check(*b)
	py.scatter(b[0], b[1], s=(4*b[2])**2*3.14151, alpha=0.5)
#        py.Circle((40, 0), 10, fc="g", ec="r", lw=5)
	py.show()
