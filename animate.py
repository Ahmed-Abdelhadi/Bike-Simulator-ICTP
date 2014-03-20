import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from  matplotlib.patches import Circle


class animate_class(object):
    def __init__(self, bike, terrain, mask = [True]):
	if hasattr(bike, '__iter__'):
	    self.bike = bike
	else:
	    self.bike = [bike]
	self.bike_num = len(bike)
	self.mask = mask
	self.terrain = terrain
	self.circles = [[None for _ in xrange(4)] for _ in xrange(self.bike_num)]
	self.lines = [[[None for _ in xrange(4)] for _ in xrange(4)] for _ in xrange(self.bike_num)]
	plt.ion()
	#self.figure = plt.figure()
        self.fig,self.ax=plt.subplots()
        plt.axis('equal')
	#self.axes = self.fig.add_subplot('111',aspect='equal')
	self.ax.set_xlim(0.,50.)
	self.ax.set_ylim(0.,30.)
	plt.plot(terrain.x,terrain.y,'r',lw=2.0)


	for b in xrange(self.bike_num):
	    for i in xrange(2):
		self.circles[b][i] = plt.Circle((bike[b].position[i][0],bike[b].position[i][1]),bike[b].radius[i],linewidth=2,color="#00bb00")
		self.ax.add_patch(self.circles[b][i])
	    for i in xrange(2,4):
		self.circles[b][i] = plt.Circle((bike[b].position[i][0],bike[b].position[i][1]),0.05,linewidth=2,color="#00bb00")
		self.ax.add_patch(self.circles[b][i])
	    for i in xrange(4):
		for j in xrange(i+1,4):
		    self.lines[b][i][j] = plt.Line2D([bike[b].position[i][0],bike[b].position[j][0]], [bike[b].position[i][1],bike[b].position[j][1]])
		    self.ax.add_line(self.lines[b][i][j])
		
   
    def draw(self,gen):
        self.gen=gen
        self.string='Generation %d'%self.gen
        self.ax.text(0.05,0.9,self.string,fontsize=20.0,transform=self.ax.transAxes)
        self.xmin,self.xmax=self.ax.get_xlim()
        self.ymin,self.ymax=self.ax.get_ylim()
        for b in xrange(self.bike_num):
	    if self.mask[b]:
		for i in xrange(4):
		    self.circles[b][i].center = (self.bike[b].position[i][0], self.bike[b].position[i][1])
		for i in xrange(4):
		    if(self.bike[b].position[i][0]>self.xmax-5):
			self.ax.set_xlim((25+self.xmin),(25+self.xmax))
			self.ax.figure.canvas.draw()
		    if(self.bike[b].position[i][1]<self.ymin+5):
			self.ax.set_ylim((self.ymin-5),(self.ymax-5))
			self.ax.figure.canvas.draw()
		    if(self.bike[b].position[i][1]>self.ymax-5):
			self.ax.set_ylim((self.ymin+5),(self.ymax+5))
			self.ax.figure.canvas.draw()
		    for j in xrange(i+1,4):
			self.lines[b][i][j].set_data([self.bike[b].position[i][0], self.bike[b].position[j][0]], [self.bike[b].position[i][1], self.bike[b].position[j][1]])
        
	plt.draw()
    
    def remove(self, b):
	for i in xrange(4):
	    self.circles[b][i].set_visible(False)
	    for j in xrange(i+1,4):
		self.lines[b][i][j].set_visible(False)
    
    def show(self):
	plt.ioff()
	plt.show()
    
    def close(self):
	plt.close()
    
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
	bx=self._column(bike.position,0)
	by=self._column(bike.position,1)
	plt.fill(bx,by)
	plt.draw()
	# Drawing the Wheel with corresponding radius
	bx=self._column(bike.position,0)
	by=self._column(bike.position,1)
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
