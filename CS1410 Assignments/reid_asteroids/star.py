import circle, random

#all passed off
class Star(circle.Circle):
    
    def __init__(self,x,y,world_width,world_height):
        dx = 0
        dy = 0
        rotation = 0
        radius = 2
        super().__init__(x, y, dx, dy, rotation, radius, world_width, world_height)
        self.brightness = random.randrange(256)
        
    def getBrightness(self):
        return self.brightness
        
    def setBrightness(self, brightness):
        if brightness >= 0 and brightness <= 255:
            self.brightness = brightness
            self.setColor((brightness,brightness,brightness))
        
    def evolve(self, dt):
        changes = [10, -10, 0]
        change = random.randrange(len(changes))
        self.setBrightness(changes[change]*dt+self.brightness)
        