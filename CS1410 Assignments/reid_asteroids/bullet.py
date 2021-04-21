import circle, math

#passed off
class Bullet(circle.Circle):
    
    def __init__(self, x,y,dx,dy,rotation,world_width,world_height):
        radius = 3
        super().__init__(x,y,dx,dy,rotation,radius,world_width,world_height)
        self.mAge = 0
        self.accelerate(100)
        self.move(.15)

        
    def getAge(self):
        return self.mAge
    
    def setAge(self, age):
        self.mAge = age
        
    def evolve(self, dt):
        self.move(dt)
        self.mAge += dt
        if self.mAge > 6:
            self.mActive = False