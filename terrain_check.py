#!/usr/bin/env python
# module Terrain_check for for group 4


class Terrain_Check():

    def __init__(terrain):
	self.terrain = terrain

    def check(self, x0,y0,r=0):
	#find nearest
	n,dist = [x-x0 for x in self.x]
	n,dist = min([(abs(x-x0),i) for i,x in enumerate(self.x)])
	self.x
        

    def constrain(self):
	pass
