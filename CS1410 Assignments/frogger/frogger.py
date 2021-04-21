from froggerlib import frog, stage, road, car, race_car, dozer, truck, water, home
from froggerlib import grass, log, turtle, text
import pygame
import random

class Frogger:
    
    def __init__(self, width, height, cell_size, rows, cols):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.num_roads = (self.rows - 3) // 2
        self.num_waters = (self.rows - 3) - self.num_roads
        self.frog_dead = False
        self.obj_size = int(self.cell_size * .8)
        self.obj_gap = self.cell_size - self.obj_size
        self.text = ''
        self.win = False
        
        #Frog
        x = (self.cols // 2) * self.cell_size + self.obj_gap
        y = (self.rows - 1) * self.cell_size + self.obj_gap
        w = self.obj_size
        h = self.obj_size 
        dx = x #desired x
        dy = y # desired y
        s = 8
        hg = self.cell_size # horizontal gap
        vg = self.cell_size # vertical gap
        self.frog = frog.Frog(x,y,w,h,dx,dy,s,hg,vg)
        
        #Start stage
        x = 0
        y = (self.rows - 1) * self.cell_size
        w = self.width
        h = self.cell_size
        self.start_stage = stage.Stage(x,y,w,h)
        
        #Road
        self.roads = []
        for i in range(self.num_roads):
            x = 0
            y =(self.rows  - 2 - i ) * self.cell_size
            w = self.width
            h = self.cell_size
            self.roads.append(road.Road(x,y,w,h))
            
        #Car
        self.cars = []
        for i in range(self.num_roads):
            x = random.randrange(self.width)
            y = (self.rows  - 2 - i ) * self.cell_size + self.obj_gap
            w = self.obj_size * 1.5
            h = self.obj_size
            dx = -w-random.randrange(self.cell_size)
            if i % 2 == 0:
                dx = self.width + random.randrange(self.cell_size)
            dy = y
            s = 5
            # 5
            self.cars.append(car.Car(x,y,w,h,dx,dy,s))
            
        #Racecar
        self.racecars = []
        for i in range(self.num_roads):
            x = random.randrange(self.width)
            y = (self.rows  - 2 - i ) * self.cell_size + self.obj_gap
            w = self.obj_size * 1.3
            h = self.obj_size
            dx = -w-random.randrange(self.cell_size)
            if i % 2 == 0:
                dx = self.width + random.randrange(self.cell_size)
            dy = y
            mins = 4
            maxs = 8
            # 6 10
            self.racecars.append(race_car.RaceCar(x,y,w,h,dx,dy,mins,maxs))
            
        #Dozer
        self.dozers = []
        for i in range(2):
            x = random.randrange(self.width)
            y = (self.rows  - 5 - i ) * self.cell_size + self.obj_gap
            w = self.obj_size * 1.6
            h = self.obj_size
            dx = -w-random.randrange(self.cell_size)
            if i % 2 == 0:
                dx = self.width + random.randrange(self.cell_size)
            dy = y
            s = 3
            # 3
            self.dozers.append(dozer.Dozer(x,y,w,h,dx,dy,s))
            
        #Truck
        self.trucks = []
        for i in range(2):
            x = random.randrange(self.width)
            y = (self.rows  - 2 - i ) * self.cell_size + self.obj_gap
            w = self.obj_size * 1.6
            h = self.obj_size
            dx = -w-random.randrange(self.cell_size)
            if i % 2 == 0:
                dx = self.width + random.randrange(self.cell_size)
            dy = y
            s = 5
            # 5
            self.trucks.append(truck.Truck(x,y,w,h,dx,dy,s))
            
        #Water
        self.waters = []
        for i in range(self.num_waters):
            x = 0
            y = (self.rows  - 3 - self.num_roads - i ) * self.cell_size
            w = self.width
            h = self.cell_size
            self.waters.append(water.Water(x,y,w,h))
            
        #Home
        x = 0
        y = 0
        w = self.width
        h = self.cell_size
        self.home = home.Home(x,y,w,h)
        
        #mid
        x = 0
        y = (self.rows  - 2 - self.num_roads) * self.cell_size
        w = self.width
        h = self.cell_size
        self.mid = stage.Stage(x,y,w,h)
        
        #Turtle
        self.turtles = []
        for i in range(self.num_waters):
            x = random.randrange(self.width)
            y = (self.rows  - 3 - self.num_roads - i ) * self.cell_size + self.obj_gap
            w = self.obj_size * 1.33
            h = self.obj_size
            dx = -w-random.randrange(self.cell_size)
            if i % 2 == 0:
                dx = self.width + random.randrange(self.cell_size) 
            dy = y
            s = 2
            self.turtles.append(turtle.Turtle(x,y,w,h,dx,dy,s))
        
        #Log
        self.logs = []
        for i in range(self.num_waters):
            x = random.randrange(self.width)
            y = (self.rows  - 3 - self.num_roads - i ) * self.cell_size + self.obj_gap
            w = self.obj_size * 4
            h = self.obj_size
            dx = -w-random.randrange(self.cell_size)
            if i % 2 == 0:
                dx = self.width + random.randrange(self.cell_size) 
            dy = y
            s = 4
            self.logs.append(log.Log(x,y,w,h,dx,dy,s))
            
        #Grass
        #do a loop and just change the horizontal position of the home
        self.grasses = []
        for i in range(4):
            x = 0 + (i*self.cell_size*self.num_roads)
            y = 0
            w = self.obj_size * 3
            h = self.cell_size
            self.grasses.append(grass.Grass(x,y,w,h))

    
    def up(self):
        self.frog.up()
        
    def down(self):
        self.frog.down()
        
    def left(self):
        self.frog.left()
        
    def right(self):
        self.frog.right()
        
    def evolve(self, dt):
        self.frog.move()
        if self.frog.outOfBounds(self.width, self.height):
            self.frog_dead = True

        for i in range(len(self.waters)):
            water = self.waters[i]
            if water.hits(self.frog):
                self.frog_dead = True

        if self.frog_dead:
            return
        if self.win:
            return
        
        for i in range(len(self.cars)):
            car = self.cars[i]
            if car.hits(self.frog):
                self.frog_dead = True
            if car.atDesiredLocation():
                new_x = self.width + random.randrange(self.cell_size)
                if i % 2 == 0:
                    new_x = -car.getWidth()-random.randrange(self.cell_size)
                car.setX(new_x)
            car.move()
            
        for i in range(len(self.racecars)):
            racecar = self.racecars[i]
            if racecar.hits(self.frog):
                self.frog_dead = True
            if racecar.atDesiredLocation():
                new_x = self.width + random.randrange(self.cell_size)
                if i % 2 == 0:
                    new_x = -racecar.getWidth()-random.randrange(self.cell_size)
                racecar.setX(new_x)   
            racecar.move()
            
        for i in range(len(self.dozers)):
            dozer = self.dozers[i]
            if dozer.hits(self.frog):
                self.frog_dead = True
            if dozer.atDesiredLocation():
                new_x = self.width + random.randrange(self.cell_size)
                if i % 2 == 0:
                    new_x = -dozer.getWidth()-random.randrange(self.cell_size)
                dozer.setX(new_x)
            dozer.move()
            
        for i in range(len(self.trucks)):
            truck = self.trucks[i]
            if truck.hits(self.frog):
                self.frog_dead = True
            if truck.atDesiredLocation():
                new_x = self.width + random.randrange(self.cell_size)
                if i % 2 == 0:
                    new_x = -truck.getWidth()-random.randrange(self.cell_size)
                truck.setX(new_x)
            truck.move()
            
        for i in range(len(self.logs)):
            log = self.logs[i]
            if log.atDesiredLocation():
                new_x = self.width + random.randrange(self.cell_size)
                if i % 2 == 0:
                    new_x = -log.getWidth() - random.randrange(self.cell_size)
                log.setX(new_x)
            log.move()
            log.supports(self.frog)
            
        for i in range(len(self.turtles)):
            turtle = self.turtles[i]
            if turtle.atDesiredLocation():
                new_x = self.width + random.randrange(self.cell_size)
                if i % 2 == 0:
                    new_x = -turtle.getWidth() - random.randrange(self.cell_size)
                turtle.setX(new_x)
            turtle.move()
            turtle.supports(self.frog)
            
        for i in range(len(self.grasses)):
            grass = self.grasses[i]
            if grass.hits(self.frog):
                self.frog_dead = True
                
        if self.home.hits(self.frog):
            self.win = True
            
            
        
            
    def draw(self, surface):
        # draw frog
        rect = pygame.Rect(0,0, self.width, self.height)
        pygame.draw.rect(surface, (255,255,255), rect)
        
        draw_object(surface, self.start_stage, (121, 38, 189))
        
        for road in self.roads:
            draw_object(surface, road, (8, 7, 7))
        for water in self.waters:
            draw_object(surface, water, (50, 121, 168))
            
        for log in self.logs:
            draw_object(surface, log, (102, 66, 11))
        for turtle in self.turtles: 
            draw_object(surface, turtle, (173, 16, 29))
            
        draw_object(surface, self.mid, (121, 38, 189))
        draw_object(surface, self.home, (252, 233, 20))
        
        for grass in self.grasses:
            draw_object(surface, grass, (129, 156, 133))
        
        draw_object(surface, self.frog, (0,255,0))
    
        for car in self.cars:
            draw_object(surface, car, (173, 75, 179))
        for racecar in self.racecars:
            draw_object(surface, racecar, (219, 39, 39))
        for truck in self.trucks:
            draw_object(surface, truck, (243, 247, 242))
        for dozer in self.dozers:
            draw_object(surface, dozer, (221, 227, 59))
            

        if self.frog_dead == True:
            display = text.Text("YOU DIED" , (self.width // 2) ,(self.height // 2) )
            display.draw(surface)
        elif self.win == True:
            display = text.Text("YOU WIN" , (self.width // 2) ,(self.height // 2) )
            display.draw(surface)


        
def draw_object(surface, obj, color):
    rect = pygame.Rect(obj.getX(), obj.getY(), obj.getWidth(), obj.getHeight())
    pygame.draw.rect(surface, color, rect)
        
        