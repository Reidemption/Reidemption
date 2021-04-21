import polygon
import random, math

# All passed off
#no changes parte 2
class Rock(polygon.Polygon):
    
    def __init__(self, x, y, world_width, world_height):
        rotation = random.uniform(0.0, 359.9)
        super().__init__(x,y, 0, 0,rotation, world_width ,world_height)
        self.mSpinRate = random.uniform(-90,90)
        self.accelerate(random.uniform(10,20))
        self.setPolygon(self.createRandomPolygon(25, 10))
        
    def createRandomPolygon(self, radius, number_of_points):
        diffy = 360/number_of_points
        angle = 0
        points = []
        for i in range(number_of_points):
            new_r = random.uniform(.7, 1.3) * radius
            x = math.cos(math.radians(angle)) * new_r
            y = math.sin(math.radians(angle)) * new_r
            points.append((x,y))
            angle += diffy
        return points
            
    
    def getSpinRate(self):
        return self.mSpinRate
    
    def setSpinRate(self, spin_rate):
        self.mSpinRate = spin_rate
        
    def evolve(self, dt):
        self.rotate(self.mSpinRate * dt)
        self.move(dt)
    