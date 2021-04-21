import pygame
import lake
import math

pi = math.pi

class Picture:
    def __init__(self, width, height):
       self.width = width
       self.height = height
       self.lakes = [lake.Lake((97, 156, 201),0,self.height//3,self.width,self.height),
               lake.Lake((162, 202, 232),100,(self.height//4) - 100, 400, self.height-200),
               lake.Lake((29, 122, 191),300,(self.height//4)//2,self.width, (self.height//3)//2+250),
               lake.Lake((74, 237, 224),0,0,self.width,300),
               lake.Lake((8, 110, 13),0,252,self.width,self.height//3)
                     ]
       self.sun = lake.Sun((217, 205, 35),300,250,125)
       self.dirt = lake.Dirt((8, 110, 13),0,252,self.width,self.height//3)
       self.tent = [lake.Tent((92, 70, 16), [(self.width//2,(self.height*.5)+65),
                                            (self.width//2+125,self.height*.15),
                                            (self.width//2+250,self.height*.5+65)
                                            ]),
                    lake.Tent((224, 185, 105), [(self.width//2+62.5,(self.height *.5)+65),
                                            (self.width//2+125,150),
                                            (self.width//2+187.5,self.height *.5+65)
                                            ])
                    ]
            #[(x1, y1), (x2, y2), (x3, y3)]                   
       self.bushes = [lake.Bushes((150, 232, 49), 100,350,450,101),
                      lake.Bushes((147, 207, 74), 400,300,500,155)]
       self.canoe = lake.Canoe((92, 70, 16), self.width//2,self.height * .66,self.width//2-300,self.height//4-150, pi, 2*pi,10)
       
    def evolve(self, dt):
       pass
    def draw(self, surface):
       r = pygame.Rect(0, 0, self.width, self.height)
       pygame.draw.rect(surface, (255, 255, 255), r)
       for i in self.lakes:
           i.draw(surface)
       self.sun.draw(surface)
       self.dirt.draw(surface)
       for i in self.bushes:
           i.draw(surface)
       for i in self.tent:
           i.draw(surface)
       self.canoe.draw(surface)
       

