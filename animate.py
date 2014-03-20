import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from  matplotlib.patches import Circle


class animate_class(object):
    """ 
    Animate class for visualization
    blah blah
    """

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
	plt.plot(terrain.x,terrain.y,'r',lw=2.0, color="#000000")


	for b in xrange(self.bike_num):
	    self.circles[b][0] = plt.Circle((bike[b].position[0][0],bike[b].position[0][1]),bike[b].radius[0],linewidth=2,color="#ff0000")
	    self.circles[b][1] = plt.Circle((bike[b].position[1][0],bike[b].position[1][1]),bike[b].radius[1],linewidth=2,color="#00bb00")
	    for i in xrange(2):
		self.ax.add_patch(self.circles[b][i])
	    for i in xrange(2,4):
		self.circles[b][i] = plt.Circle((bike[b].position[i][0],bike[b].position[i][1]),0.05,linewidth=2,color="#00bb00")
		self.ax.add_patch(self.circles[b][i])
	    for i in xrange(4):
		for j in xrange(i+1,4):
		    self.lines[b][i][j] = plt.Line2D([bike[b].position[i][0],bike[b].position[j][0]], [bike[b].position[i][1],bike[b].position[j][1]])
		    self.ax.add_line(self.lines[b][i][j])
		
   
    def draw(self,gen):
        """
        Draw lines connecting vertices of the bike and draw radius.

        Changes the window as the bike moves.
        """
        bike = self.bike
        mask = self.mask
        circles = self.circles
        lines = self.lines
        self.string='Generation %d'%gen
        self.ax.text(0.05,0.9,self.string,fontsize=20.0,transform=self.ax.transAxes)
        xmin, xmax=self.ax.get_xlim()
        ymin, ymax=self.ax.get_ylim()
        for b in xrange(self.bike_num):
	    if mask[b]:
		for i in xrange(4):
		    circles[b][i].center = (bike[b].position[i][0], bike[b].position[i][1])
		for i in xrange(4):
		    if(bike[b].position[i][0]>xmax-5):
			self.ax.set_xlim((25+xmin),(25+xmax))
			self.ax.figure.canvas.draw()
		    if(bike[b].position[i][1]<ymin+5):
			self.ax.set_ylim((ymin-5),(ymax-5))
			self.ax.figure.canvas.draw()
		    if(bike[b].position[i][1]>ymax-5):
			self.ax.set_ylim((ymin+5),(ymax+5))
			self.ax.figure.canvas.draw()
		    for j in xrange(i+1,4):
			lines[b][i][j].set_data([bike[b].position[i][0], bike[b].position[j][0]], [bike[b].position[i][1], bike[b].position[j][1]])
        
	plt.draw()
    
    def remove(self, b):
	if self.mask[b]:
	    for i in xrange(4):
		self.circles[b][i].set_visible(False)
		for j in xrange(i+1,4):
		    self.lines[b][i][j].set_visible(False)
	self.mask[b] = False
    
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
