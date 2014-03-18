import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from  matplotlib.patches import Circle


class animatebike(object):
   def __init__(self,bike,terrain):
       self.bike=bike
       self.terrain=terrain
       plt.ion()
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
