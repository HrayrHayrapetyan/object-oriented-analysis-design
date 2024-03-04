import math
class Polar:
        def __init__(self,radius : int,angle : float):
                self.radius=radius
                self.angle=angle

        def __repr__(self):
                return f'this is a point with a radius {self.radius} and an angle {self.angle}'
        def polar2cart(self):
                x=self.radius*math.cos(self.angle)
                y=self.radius*math.sin(self.angle)
                return x,y

        def cart2polar(self,x,y):
                r=math.sqrt(x**2+y**2)
                if x>0:
                        theta=math.atan(y/x)
                elif x<0 and y>=0:
                        theta=math.atan(y/x)+math.pi
                elif x<0 and y<0:
                        theta=math.atan(y/x)-math.pi
                elif x==0 and y>0:
                        theta=math.pi/2
                elif x==0 and y<0:
                        theta=-math.pi/2
                else:
                        return None
                return r,theta


        def __add__(self,polar):
                x1,y1=polar.polar2cart()
                x2,y2=self.polar2cart()
                return Polar(x1+x2,y1+y2)


point1=Polar(2, math.pi/3)
point2=Polar(5,math.pi/4)

point3=point2.__add__(point1)
print(point3)

