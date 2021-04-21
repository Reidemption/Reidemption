import math
#All passed off
#All passed off parte 2
class Movable:
    def __init__(self, x,y,dx,dy,world_width,world_height):
        self.mX = x
        self.mY = y
        self.mDX = dx
        self.mDY = dy
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mActive = True
        
    def getActive(self):
        return self.mActive
    
    def setActive(self, active):
        self.mActive = active
        
    def hits(self, other):
        distance = math.sqrt((self.getX()-other.getX()) **2
                  + (self.getY()-other.getY())**2)
        r = self.getRadius() + other.getRadius()
        return distance <= r
        
    def getRadius(self):
        raise NotImplementedError
        
    def getX(self):
        return self.mX
    
    def getY(self):
        return self.mY
    
    def getDX(self):
        return self.mDX
    
    def getDY(self):
        return self.mDY
    
    def getWorldWidth(self):
        return self.mWorldWidth
    
    def getWorldHeight(self):
        return self.mWorldHeight
    
    def move(self, dt):
        self.mX += dt * self.mDX
        self.mY += dt * self.mDY
        if self.mX >= self.mWorldWidth:
            #right edge
            self.mX -= self.mWorldWidth
            
        if self.mX < 0:
            #off left edge
            self.mX += self.mWorldWidth
            
        if self.mY >= self.mWorldHeight:
            #bottom edge
            self.mY -= self.mWorldHeight
            
        if self.mY < 0:
            #top edge
            self.mY += self.mWorldHeight
    
    def accelerate(self, delta_velocity):
        raise NotImplementedError
    
    def evolve(self, dt):
        raise NotImplementedError
    
    def draw(self, surface):
        raise NotImplementedError