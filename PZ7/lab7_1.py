
import math

class Sphere(object):
    radius = 1.0
    x = 0.0
    y = 0.0
    z = 0.0
    
    def __init__(self, radius = 1.0, x = 0.0, y = 0.0, z = 0.0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z
    
    def get_volume(self):
        return (4/float(3)*math.pi*math.pow(self.radius,3))
    
    def get_square(self):
        return (4*math.pi*math.pow(self.radius,2))
    
    def get_radius(self):
        return (self.radius)
    
    def get_center(self):
        return (self.x, self.y, self.z)
    
    def set_radius(self, r):
        self.radius = r
    
    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def is_point_inside(self, x, y, z):
        if math.sqrt(math.pow(self.x - x, 2) \
            + math.pow(self.y - y, 2) \
            + math.pow(self.z - z, 2)) > self.radius:
            return (False)
        else:
            return (True)

my_sphere = Sphere()

print (my_sphere.get_center())
print (my_sphere.get_radius())
print (my_sphere.get_volume())
print (my_sphere.is_point_inside(0, -1.5, 0))
my_sphere.set_radius(1.6)
print (my_sphere.is_point_inside(0, -1.5, 0))
print (my_sphere.get_radius())
'''