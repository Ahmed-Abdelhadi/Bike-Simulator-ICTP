import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from  matplotlib.patches import Circle
from  terrain import Terrain
import math
from Bike_start import Bike

# Returning elements of the tuple 
def  column (matrix,i):
      return [row[i] for row in matrix]

t=Terrain()
tx=t.x
ty=t.y
ty1=ty
#Canvas
plt.ylim([(min(ty)-5),(max(tx)/2.0)])
plt.xlim([min(tx),max(tx)])

plt.plot(tx,ty,'r')
#plt.fill_between(tx,ty,-1,'r')
# Plotting Bike
bk=Bike()
bx=column(bk.pos,0)
by=column(bk.pos,1)
wr=bk.r
plt.fill(bx,by)

# Plotting Wheel
for i in xrange(0,4):
  circle=plt.Circle((bx[i],by[i]),wr[i],color="#ccaa00")
  fig=plt.gcf()
  fig.gca().add_artist(circle)

plt.show()
