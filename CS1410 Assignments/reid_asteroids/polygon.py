import rotatable, math, pygame

#All passed off
#Passed off parte 2
class Polygon(rotatable.Rotatable):
    
    ##
    def __init__(self, x,y,dx,dy,rotation, world_width,world_height):
        super().__init__(x,y,dx,dy,rotation, world_width,world_height)
        self.mOriginalPolygon = []
        self.mColor = (255,255,255)
    ##
    def getPolygon(self):
        return self.mOriginalPolygon
    ##
    def getColor(self):
        return self.mColor
    
    ##
    def setPolygon(self, point_list):
        self.mOriginalPolygon = point_list
    ##    
    def setColor(self, color):
        self.mColor = color
        
    def draw(self, surface):
        points = self.rotateAndTranslatePointList(self.mOriginalPolygon)
        pygame.draw.polygon(surface, self.mColor, points, 5)
        
    def getRadius(self):
        length = len(self.mOriginalPolygon)
        if length == 0:
            return 0
        total = 0
        for x,y in self.mOriginalPolygon:
            d = math.sqrt(y**2+x**2)
            total += d
        return total/length
            
            
            
            