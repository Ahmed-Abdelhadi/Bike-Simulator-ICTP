#!/usr/bin/env python
# Bike factory class for group 4

from random import random

def _cross(a,b):
    """ Make crossover of two equal datasets from a-25% to b+25%"""
    if hasattr(a, '__iter__'):
	res=[]
	for i,j in zip(a,b):
	    res.append(_cross(i,j))
        return res
    else:
        return (b-a)*(1.5*random()-0.25)+a

#---------------------------------------------------
def _choose_one(probab):
    """ Choose one position according probability function 
        probab: list of increasing numbers steps are proportional to probabilitis"""
    x = random()
    for i,p in enumerate(probab):
        if x < p:
	    return i
    return i


#=================================================================
class bike_factory_class(object):
    """ bike factory class has set of bikes and produce new set of bikes
	bikes: 		set of bikes
	mutation_ratio:	ratio of mutation in new population """
#    from Bike_start import Bike
    
    def __init__(self, size = 100):
	"""Make set of random bikes, make mutation ratio (quality of production)"""
        from bike import bike_class
	self.bikes = [bike_class() for i in range(size) ]
	for b in self.bikes:
	    b.randomize()
	self.mutation_ratio = 0.01
	self.size = size

    def __iter__(self):
	"""Send bike for testing """
	for i in self.bikes:
	    yield i
	return

#-----------------------------------------------------
    def make_new_generation(self):
	""" Produce new generation of bikes"""
	old_bikes  =  self.bikes
	self.bikes = []
	# make ranking 
	results=[]
	for i in range(self.size):
	    print i
	    if old_bikes[i].result > 0:
		results.append(old_bikes[i].result)
	    else:
		results.append(0)
	
	total_distance = sum(results)
	if total_distance == 0:
	    print "send bikes to test laboratory!!!!"
	    exit(1)
	probab = []
	s = 0.
	for i in range(self.size):
 	    s += results[i]/total_distance
	    probab.append(s)
#	print probab 

	for i in range(self.size):
	    bike1 = old_bikes[_choose_one(probab)]
	    bike2 = old_bikes[_choose_one(probab)]
	    new_bike = self._crossover(bike1,bike2)
	    new_bike = self._mutation(new_bike)
	    self.bikes.append(new_bike)
	return  True
#-----------------------------------------------------
#-----------------------------------------------------
# crossover some properties of bikes
    def  _crossover(self, bike1,bike2):
	""" Mix two bikes. Now only position and radius are upgrated"""
        from bike import bike_class
        son = bike_class()
        son.position = _cross(bike1.position,bike2.position)
        son.radius = _cross(bike1.radius,bike2.radius)
	son.check()
        return son
#----------------------------------------------------
    def  _mutation(self,bike):
	"""Make mutation.
	    If random number is low then mutation_ratio make random bike"""
	if random() < self.mutation_ratio:
            return bike.randomize()
	else:
	    return bike
################################################################3

if __name__=='__main__':	#run as a program 
    import pylab as py
    from random import random
    import matplotlib.patches as mpatches

#------- test byke_factory_class -------------
    b=bike_factory_class(2)
    for  j in range(2):
        for i in b:
	    print i.position
	    print i.radius
	    i.result = 1
        b.make_new_generation()
# ---- test _cross function -----------------
    print _cross(1.,2.)
    print _cross([1.,1.],[2,2])
    print _cross([[1.,1],[1.,1]],[[2,2],[2,2]])

    prob = [_cross(1.,2.) for i in range(10000)]
    py.hist(prob, 50, normed=1, facecolor='green', alpha=0.5)
    py.show()
#------- test _choose_one function -------------
    prob = [_choose_one([0.5,0.6,0.7,1.]) for i in range(10000)]
    py.hist(prob, 50, normed=1, facecolor='green', alpha=0.5)
    py.show()

