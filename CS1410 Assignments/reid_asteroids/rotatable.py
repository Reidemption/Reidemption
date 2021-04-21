import movable
import math

#All works
#No changes parte 2
class Rotatable(movable.Movable):
    
    ##
    def __init__(self, x,y,dx,dy,rotation, world_width,world_height):
        super().__init__(x,y,dx,dy,world_width,world_height)
        self.mRotation = rotation
    ##   
    def getRotation(self):
        return self.mRotation
    
    ##
    def rotate(self, delta_rotation):
        self.mRotation = (self.mRotation + delta_rotation) % 360
    
    def splitDeltaVIntoXAndY(self, rotation, delta_velocity):
        # x = cos
        # y = sin
        x = math.cos(math.radians(rotation)) * delta_velocity
        y = math.sin(math.radians(rotation)) * delta_velocity
        return (x,y)
    
    def accelerate(self, delta_velocity):
        dx, dy = self.splitDeltaVIntoXAndY(self.mRotation, delta_velocity)
        self.mDX += dx
        self.mDY += dy
    
    def rotatePoint(self, x, y):
        angle = math.atan2(y, x)
        new_angle = angle + math.radians(self.mRotation)
        d = math.sqrt(y**2+x**2)
        newx = d * math.cos(new_angle)
        newy = d * math.sin(new_angle)
        return newx, newy
    
    def translatePoint(self, x, y):
        x += self.mX
        y += self.mY
        return x,y
    
    def rotateAndTranslatePoint(self, x, y):
        newx, newy = self.rotatePoint(x,y)
        newx, newy = self.translatePoint(newx, newy)
        return newx, newy
    
    def rotateAndTranslatePointList(self, point_list):
        new_points = []
        for point in point_list:
            newpoint = self.rotateAndTranslatePoint(point[0], point[1])
            new_points.append(newpoint)
        return new_points
        