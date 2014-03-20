#!/usr/bin/env python
# main program for group 4
from terrain  import terrain_class
from bike_factory import bike_factory_class
from animate import animate_class
from physics import physics_class

terrain = terrain_class(rand=5, improved=True)

n_bike = 3
factory = bike_factory_class(n_bike)

for i in xrange(100):
    print "Generation %i, try %i bikes"%(factory.generation,factory.size)
#go simulation
    bike_mask = [True for bike in factory.bikes]
    animate  = animate_class(factory.bikes, bike_mask, terrain)
    physics = [physics_class(bike,terrain) for bike in factory.bikes]
    time = 0

    while any(bike_mask):
	for b in xrange(n_bike):
	    if bike_mask[b]:
		physics[b].step()
	    if physics[b].stuck():
		bike_mask[b] = False
		animate.remove(b)
	time+=1
	if not time%100:
	    animate.draw()
    
    animate.close()
	
# get some data from physics and story the bike result
    #rr = physics.get_result()
    #print "result = ", rr
    #new_bike.result = rr

    factory.make_new_generation()		#make some improovements genetics

#---------------------------------------------------
for i in xrange(5):
    print "Generation %i, try %i bikes"%(factory.generation,factory.size)
#go simulation
    for new_bike in factory.bikes:
    
        physics = physics_class(new_bike,terrain)
        animate  = animate_class(new_bike,terrain)

        for time in xrange(100000):
	    physics.step()

	    if not time%100:
		animate.draw()

	    if physics.stuck():
		break
	animate.close()
	
# get some data from physics and story the bike result
	rr = physics.get_result()
	print "result = ", rr
        new_bike.result = rr

    factory.make_new_generation()		#make some improovements genetics

