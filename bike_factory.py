#!/usr/bin/env python
# Bike factory class for group 4
#=================================================================
class Bike_factory(object):
#    from Bike_start import Bike
    
    def __init__(self, size = 100):
        from Bike_start import Bike
	self.bikes = [Bike() for i in range(size) ]
	[i.randomize() for i in self.bikes ]
	self.mutation_ratio = 0.01

    def __iter__(self):
	for i in self.bikes:
	    yield i
	return

#-----------------------------------------------------
    def make_new_generation(self):
	old_bikes  =  self.bikes
	self.bikes = []
	total_distance = sum([i.get_result() for i in old_bikes])
	probab = [i.get_result()/total_distance for i in old_bikes]
	for i in range(len(old_bikes)):
	    bike1 = old_bikes[choose_one(probab)]
	    bike2 = old_bikes[choose_one(probab)]
	    new_bike = self._crossover(bike1,bike2)
	    new_bike = self._mutation(new_bike)
	    self.bikes.append(new_bike)
	return  True
#-----------------------------------------------------
    def _choose_one(self,a):
        return 1
#-----------------------------------------------------
    def  _crossover(self, bike1,bike2):
	def _cross(a,b):
	    if a.has_attr('__itera__'):
		res=[]
		for i,j in zip(a,b):
		    if i.has_attr('__itera__'):
			ii = [(i1-j1)*(1.5*random()-0.25)+i1 for i1,j1 in zip(i,j)]
		    else:
			ii=(i1-j1)*(1.5*random()-0.25)+i1
		    res.append(ii)
	        return res
	    else:
	        return (b-a)*(1.5*random()-0.25)+a

        son = Bike()
        son.P = self._cross(bike1.P,bike2.P)
	son.check()
# some properties of bikes
#    self.P=[[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
#    self.r=[r1,r2,r3,r4]
#    self.m=[m1,m2,m3,m4]
#    self.k=[k1,k2,k3,k4,k5,k6]

        return son
#----------------------------------------------------
    def  _mutation(self,bike):
	if random() < self.mutation_ratio:
            return bike.randomize()
	else:
	    return bike
################################################################3

if __name__=='__main__':	#run as a program 
    b=Bike_factory(10)
    for i in b:
	print i
    b.make_new_generation()