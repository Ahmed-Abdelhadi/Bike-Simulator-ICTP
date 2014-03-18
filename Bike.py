import math

class Bike(object):
  #def CalcDist(self,x1,y1,x2,y2):
   # distance=((x2-x1)**2+(y2-y1)**2)**0.5
   # return distance

  def __init__(self,x1,x2,x3,x4,y1,y2,y3,y4,r1,r2,r3,r4,m1,m2,m3,m4,vx1,vx2,vx3,vx4,vy1,vy2,vy3,vy4,ang_v1,ang_v2,ang_v3,ang_v4,a1,a2,a3,a4,ang_a1,ang_a2,ang_a3,ang_a4,k1,k2,k3,k4,k5,k6):
    self.x=[x1,x2,x3,x4]
    self.y=[y1,y2,y3,y4]
    self.r=[r1,r2,r3,r4]
    self.m=[m1,m2,m3,m4]
    self.vx=[vx1,vx2,vx3,vx4]
    self.vy=[vy1,vy2,vy3,vy4]
    self.ang_v=[ang_v1,ang_v2,ang_v3,ang_v4]
    self.a=[a1,a2,a3,a4]
    self.ang_a=[ang_a1,ang_a2,ang_a3,ang_a4]
    self.SpringDist=[self.CalcDist(x1,y1,x2,y2),self.CalcDist(x1,y1,x3,y3),self.CalcDist(x1,y1,x4,y4),self.CalcDist(x2,y2,x3,y3),self.CalcDist(x2,y2,x4,y4),self.CalcDist(x3,y3,x4,y4)]
    self.k=[k1,k2,k3,k4,k5,k6]
  
  def CalcDist(self,x1,y1,x2,y2):
    distance=((x2-x1)**2+(y2-y1)**2)**0.5
    return distance
  
  def GenerateBike():
    GeneratePts()
    GenerateRadius()
    GenerateMass()
    GenerateSpring()    

  def GeneratePts():
    pass

  def GenerateRadius():
    pass

  def GenerateMass():
    pass

  def GenerateSpring():
    pass

 
Bike1= Bike(4,8,9,3,4,5,5,8,1,3,5,6,3,4,1,8,9,3,4,5,3,5,6,3,4,8,5,1,2,4,2,8,9,3,4,7,5,3,5,6,3,4)


print"x=",Bike1.x  
print"y=",Bike1.y
print"r=",Bike1.r
print"m=",Bike1.m
print"vx=",Bike1.vy
print"vy=",Bike1.vy
print"ang_v=",Bike1.ang_v
print"a=",Bike1.a
print"ang_a=",Bike1.ang_a
print "SpringDist=",Bike1.SpringDist
print "K=",Bike1.k
#D12=math.sqrt(4)
D12=Bike1.CalcDist(9,12,3,4)
print D12

