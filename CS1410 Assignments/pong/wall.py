import pygame

class Wall():
    #
    def __init__(self, x, y, width, height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
    #    
    def getX(self):
        return self.mX
    #
    def getY(self):
        return self.mY
    #
    def getWidth(self):
        return self.mWidth
    #
    def getHeight(self):
        return self.mHeight
    #
    def getRightX(self):
        return self.mX + self.mWidth
    #
    def getBottomY(self):
        return self.mY + self.mHeight

    def draw(self, surface):
        pygame.draw.rect(surface, (255,255,255), pygame.Rect(self.mX, self.mY, self.mX+self.mWidth, self.mY+self.mHeight))
