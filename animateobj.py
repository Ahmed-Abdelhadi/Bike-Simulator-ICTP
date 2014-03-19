import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from  matplotlib.patches import Circle


class animate_class(object):
    def __init__(self,bike,terrain):
	self.bike=bike
	self.terrain=terrain
	self.circles=[]
	self.lines=[[None for _ in range(4)] for _ in range(4)]
	plt.ion()
	self.figure = plt.figure()
	self.axes = self.figure.add_subplot('111',aspect='equal')
	self.axes.set_xlim(-1.,10.)
	self.axes.set_ylim(-1.,10.)
	plt.plot(terrain.x,terrain.y,'r',lw=2.0)
	for i in xrange(2):
	    self.circles.append(plt.Circle((bike.pos[i][0],bike.pos[i][1]),bike.r[i],linewidth=2,color="#00bb00"))
	    self.axes.add_patch(self.circles[i])
	for i in xrange(2,4):
	    self.circles.append(plt.Circle((bike.pos[i][0],bike.pos[i][1]),0.05,linewidth=2,color="#00bb00"))
	    self.axes.add_patch(self.circles[i])
	for i in xrange(4):
	    for j in xrange(i+1,4):
		self.lines[i][j] = plt.Line2D([bike.pos[i][0],bike.pos[j][0]], [bike.pos[i][1],bike.pos[j][1]])
		self.axes.add_line(self.lines[i][j])
		
   
    def draw(self):
	for i in xrange(4):
	    self.circles[i].center = (self.bike.pos[i][0], self.bike.pos[i][1])
	for i in xrange(4):
	    for j in xrange(i+1,4):
		self.lines[i][j].set_data([self.bike.pos[i][0], self.bike.pos[j][0]], [self.bike.pos[i][1], self.bike.pos[j][1]])
	plt.draw()
	
    def show(self):
	plt.ioff()
	plt.show()
    
    # Setting up Canvas and plot the terrain
    def visualize(self):
	terrain=self.terrain
	tx=terrain.x
	ty=terrain.y
	plt.ylim([(min(ty)-5),(max(tx)/2.0)])
	plt.xlim([min(tx),max(tx)])
	plt.plot(tx,ty,'r',lw=2.0)
	
	# Filling the bicycle body
	bike=self.bike
	bx=self._column(bike.pos,0)
	by=self._column(bike.pos,1)
	plt.fill(bx,by)
	plt.draw()
	# Drawing the Wheel with corresponding radius
	bx=self._column(bike.pos,0)
	by=self._column(bike.pos,1)
	wr=self.bike.r
	for i in xrange(0,4):
	    circle=plt.Circle((bx[i],by[i]),wr[i],color="#00bb00")
	    fig=plt.gcf()
	    fig.gca().add_artist(circle)
	    
    # Returning elements of the tuple 
    def  _column(self,matrix,i):
	return [row[i] for row in matrix]
    
if __name__=='__main__':
    from Bike_start import Bike
    from terrain import Terrain
    t = Terrain()
    bike = Bike()
    animatebike =animatebike(bike, t)
    animatebike.visualize()
    plt.ioff()
    plt.show()
