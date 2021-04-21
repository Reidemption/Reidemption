import rotatable, pygame

#All passed off
class Circle(rotatable.Rotatable):
    
    #passed off
    def __init__(self, x, y, dx, dy, rotation, radius, world_width, world_height):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)
        self.mRadius = radius
        self.mColor = (255, 255, 255)
        
    def getRadius(self):
        return self.mRadius
    
    def getColor(self):
        return self.mColor
        
    def setRadius(self, radius):
        if radius > 1:
            if self.mRadius != radius:
                self.mRadius = radius
        
    def setColor(self, color):
        self.mColor = color
        
    def draw(self, surface):
        color = self.mColor
        pygame.draw.circle(surface, (255,255,255), (int(self.mX), int(self.mY)), self.mRadius)