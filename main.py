#!/usr/bin/env python
# main program for group 4
from terrain import Terrain
from bike_factory import Bike_factory
from visual import Visual

terrain = Terrain()

for i in xrange(1):
    factory = Bike_factory(20)

#go simulation
    for new_bike in factory():
    
        physics = Physics_class(new_bike,terrain)
        visual  = Visual(new_bike,terrain)

        while physics.make_step(): 
	    visual.plot()		# some visual

# get some data from physics and story the bike result
        new_bike.set_result(physics.get_result())


    factory.make_new_generation()		#make some improovements genetics

