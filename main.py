#!/usr/bin/env python
# main program for group 4
from terrain import Terrain
from bike_factory import Bike_factory
from animateobj import animatebike
from physics import physics

terrain = Terrain()

for i in xrange(1):
    factory = Bike_factory(20)

#go simulation
    for new_bike in factory:
    
        physic = physics(new_bike,terrain)
        animate  = animatebike(new_bike,terrain)

        for time in xrange(10000):
	    physic.step()
	    if not time%10:
		animate.draw()
		pass
	    if physic.stuck():
		break
	animate.show()

# get some data from physics and story the bike result
        new_bike.set_result(physics.get_result())


    factory.make_new_generation()		#make some improovements genetics

