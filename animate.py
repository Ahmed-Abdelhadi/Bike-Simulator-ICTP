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
	#self.figure = plt.figure()
        self.fig,self.ax=plt.subplots()
        plt.axis('equal')
	#self.axes = self.fig.add_subplot('111',aspect='equal')
	self.ax.set_xlim(0.,50.)
	self.ax.set_ylim(0.,10.)
	plt.plot(terrain.x,terrain.y,'r',lw=2.0)
	for i in xrange(2):
	    self.circles.append(plt.Circle((bike.position[i][0],bike.position[i][1]),bike.radius[i],linewidth=2,color="#00bb00"))
	    self.ax.add_patch(self.circles[i])
	for i in xrange(2,4):
	    self.circles.append(plt.Circle((bike.position[i][0],bike.position[i][1]),0.05,linewidth=2,color="#00bb00"))
	    self.ax.add_patch(self.circles[i])
	for i in xrange(4):
	    for j in xrange(i+1,4):
		self.lines[i][j] = plt.Line2D([bike.position[i][0],bike.position[j][0]], [bike.position[i][1],bike.position[j][1]])
		self.ax.add_line(self.lines[i][j])
		
   
    def draw(self):
        self.xmin,self.xmax=self.ax.get_xlim()
        self.ymin,self.ymax=self.ax.get_ylim()
	for i in xrange(4):
	    self.circles[i].center = (self.bike.position[i][0], self.bike.position[i][1])
	for i in xrange(4):
            if(self.bike.position[i][0]>self.xmax-5):
                self.ax.set_xlim((25+self.xmin),(25+self.xmax))
                self.ax.figure.canvas.draw()
            if(self.bike.position[i][1]<self.ymin+3):
                self.ax.set_ylim((self.ymin-3),(self.ymax-3))
                self.ax.figure.canvas.draw()
	    for j in xrange(i+1,4):
		self.lines[i][j].set_data([self.bike.position[i][0], self.bike.position[j][0]], [self.bike.position[i][1], self.bike.position[j][1]])
        
	plt.draw()
	
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
