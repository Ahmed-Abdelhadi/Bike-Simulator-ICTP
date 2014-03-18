#!/usr/bin/env python
# Bike factory class for group 4
#=================================================================
class Bike_factory(Class):
    from Bike import Bike
    
    def __init__(self, size = 100):
	self.bikes = [Bike().randomize() for i in range(size) ]
	self.mutation_ratio = 0.01

    def __iter__(self):
	for i in self.bikes:
	    yield i
	return

#-----------------------------------------------------
    def make_new_generation(self):
	return
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
	    return (b-a)*random()+a

        son = Bike()
        son.x = self._cross(bike1.x,bike2.x)
        return son
#----------------------------------------------------
    def  _mutation(self,bike):
	if random() < self.mutation_ratio:
            return bike.randomize()
	else:
	    return bike
################################################################3

if __name__=='__main__':	#run as a program 
    pass
