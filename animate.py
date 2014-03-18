
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from  terrain import *
import math
y4=np.minimum(tx,ty)
plt.plot(tx,ty,lw=4)
plt.fill_between(tx,ty,color='#aa0000',lw=4)

x=[2.0,8.0,5.0,3.0]
y=[1.0,1.0,4.0,4.0]
wheelx=x[0:2]
wheely=y[0:2]
barx=x
bary=y

plt.fill(x,y,color='#bbefff')
i#plt.plot(barx,bary,'-',linewidth=4.0)
plt.plot(wheelx,wheely,marker='o',markersize=50.0,lw=3.0)
#plt.plot(barx,bary,marker='^',markersize=5.0)
#plt.show()
plt.show()
