import polygon, bullet

#All passed off
class Ship(polygon.Polygon):
    
    ##
    def __init__(self, x,y,world_width,world_height):
        rotation = 0
        dx = 0
        dy = 0
        super().__init__(x,y,dx,dy,rotation, world_width,world_height)
        self.mRotation = rotation
        self.setPolygon([(0,0),(-15,15),(-15,-15)])
        
    def fire(self):
        x, y = self.rotateAndTranslatePoint(*self.getPolygon()[0])
        
        dx = self.getDX()
        dy = self.getDY()
        rotation = self.getRotation()
        world_width = self.getWorldWidth()
        world_height = self.getWorldHeight()
        b = bullet.Bullet(x,y,dx,dy,rotation,world_width,world_height)
        return b
        
    def evolve(self, dt):
        self.move(dt)
        
    