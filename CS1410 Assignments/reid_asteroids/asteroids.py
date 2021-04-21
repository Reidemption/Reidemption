import ship, rock, random, pygame, star, bullet
#bullet, star


class Asteroids(ship.Ship, rock.Rock):
    
    #passed off
    def __init__(self,world_width, world_height):
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mShip = ship.Ship(world_width//2, world_height//2, self.mWorldWidth, self.mWorldHeight)
        self.mBullets = []
        self.mRocks = []
        self.mStars = []
        self.mObjects = [self.mShip]
        
        
        for i in range(10):
            x = random.randrange(0, self.mWorldWidth)
            y = random.randrange(0, self.mWorldHeight)
            r = rock.Rock(x, y, self.mWorldHeight, self.mWorldWidth)
            self.mRocks.append(r)
            

        for i in range(20):
            x = random.randrange(0, self.mWorldWidth)
            y = random.randrange(0, self.mWorldHeight)
            s = star.Star(x,y, self.mWorldHeight, self.mWorldWidth)
            self.mStars.append(s)
            
        self.mObjects += self.mRocks + self.mStars + self.mBullets    
   
    
    #checked off
    def getWorldWidth(self):
        return self.mWorldWidth
    
    #checked off
    def getWorldHeight(self):
        return self.mWorldHeight
    
    #checked off
    def getShip(self):
        return self.mShip
    
    #checked off
    def getRocks(self):
        return self.mRocks
    
    #checked off
    def getBullets(self):
        return self.mBullets
    
    #checked off
    def getStars(self):
        return self.mStars
    
    #checked off
    def getObjects(self):
        return self.mObjects
    
    #
    def turnShipLeft(self, delta_rotation):
        self.mShip.rotate(-delta_rotation)
    
    #
    def turnShipRight(self, delta_rotation):
        self.mShip.rotate(delta_rotation)
    
    #
    def accelerateShip(self, delta_velocity):
        self.mShip.accelerate(delta_velocity)
    
    #
    def fire(self):
        b = self.mShip.fire()
        if len(self.mBullets) >= 3:
            return
        self.mBullets.append(b)
        self.mObjects.append(b)
        
    def collideRocksAndBullets(self):
        for rock in self.mRocks:
            for bullet in self.mBullets:
                if rock.hits(bullet):
                    rock.setActive(False)
                    bullet.setActive(False)
                    
    def collideShipAndBullets(self):
        for bullet in self.mBullets:
            if self.mShip.hits(bullet):
                self.mShip.setActive(False)
                bullet.setActive(False)
    
    def collideShipAndRocks(self):
        for rock in self.mRocks:
            if self.mShip.hits(rock):
                self.mShip.setActive(False)
                rock.setActive(False)
                
                
    def removeInactiveObjects(self):
        for obj in self.mObjects:
            act = obj.getActive()
            if act == False:
                self.mObjects.remove(obj)
                
    def evolveAllObjects(self, dt):
        for obj in self.mObjects:
            if obj.getActive():
                obj.evolve(dt)
                
    #passed off?
    def evolve(self, dt):
        self.evolveAllObjects(dt)
        self.collideRocksAndBullets()
        self.collideShipAndBullets()
        self.collideShipAndRocks()
        self.removeInactiveObjects()
    
    def draw(self, surface):
        rect = pygame.Rect(0,0, self.mWorldWidth, self.mWorldHeight)
        pygame.draw.rect(surface, (0,0,0), rect)
        for obj in self.mObjects:
            if obj.getActive():
                obj.draw(surface)
        
        
    
        