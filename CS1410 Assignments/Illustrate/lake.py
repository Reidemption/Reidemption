import pygame
class Lake:
   def __init__(self, color, left, top, width, height):
       self.left = left
       self.top = top
       self.width = width
       self.height = height
       self.color = color
   def draw(self, surface):
       pygame.draw.rect(surface, self.color, pygame.Rect(self.left, self.top, self.width, self.height))
       

class Dirt:
    def __init__(self, color, left, top, width, height):
       self.left = left
       self.top = top
       self.width = width
       self.height = height
       self.color = color
    def draw(self, surface):
       pygame.draw.rect(surface, self.color, pygame.Rect(self.left, self.top, self.width, self.height))
       
class Sun:
    def __init__(self, color,x,y,size):
        self.color = color
        self.x = x
        self.y = y
        self.size = size
    def draw(self,surface):
        pygame.draw.circle(surface, self.color, (self.x,self.y),self.size)
        
class Tent:
    def __init__(self, color, points):
        self.color = color
        self.points = points
    def draw(self,surface):
        pygame.draw.polygon(surface, self.color, self.points)
        
class Bushes:
    def __init__(self, color, left, top, width, height):
       self.left = left
       self.top = top
       self.width = width
       self.height = height
       self.color = color
       
    def draw(self, surface):
       pygame.draw.ellipse(surface, self.color, pygame.Rect(self.left, self.top, self.width, self.height))
       
class Canoe:
    def __init__(self, color, left, top, width, height, start_angle, stop_angle, swidth):
       self.left = left
       self.top = top
       self.width = width
       self.height = height
       self.color = color
       self.start_angle = start_angle
       self.stop_angle = stop_angle
       self.swidth = swidth
    def draw(self, surface):
        pygame.draw.arc(surface, self.color, pygame.Rect(self.left, self.top, self.width, self.height),
                        self.start_angle, self.stop_angle, self.swidth)
        
        
        
        
        
        