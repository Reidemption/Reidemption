import pygame
import random

class Ball:
    #
    def __init__(self,size, min_x, max_x, min_y, max_y, left_paddle_x, right_paddle_x):
        self.mX = min_x
        self.mY = min_y
        self.mSize = size
        self.mDX = 0
        self.mDY = 0
        self.mMinX = min_x
        self.mMaxX = max_x
        self.mMinY = min_y
        self.mMaxY = max_y
        self.mLeftPaddleX = left_paddle_x
        self.mLeftPaddleMinY = min_y
        self.mLeftPaddleMaxY = max_y
        self.mRightPaddleX = right_paddle_x
        self.mRightPaddleMinY = min_y
        self.mRightPaddleMaxY = max_y
    #    
    def getX(self):
        return self.mX
    #
    def getY(self):
        return self.mY
    #
    def getSize(self):
        return self.mSize
    #
    def getDX(self):
        return self.mDX
    #
    def getDY(self):
        return self.mDY
    #
    def getMinX(self):
        return self.mMinX
    #
    def getMinY(self):
        return self.mMinY
    #
    def getMaxX(self):
        return self.mMaxX
    #
    def getMaxY(self):
        return self.mMaxY
    #
    def getLeftPaddleX(self):
        return self.mLeftPaddleX
    #
    def getLeftPaddleMinY(self):
        return self.mLeftPaddleMinY
    #
    def getLeftPaddleMaxY(self):
        return self.mLeftPaddleMaxY
    #
    def getRightPaddleX(self):
        return self.mRightPaddleX
    #
    def getRightPaddleMinY(self):
        return self.mRightPaddleMinY
    #
    def getRightPaddleMaxY(self):
        return self.mRightPaddleMaxY
    #
    def setPosition(self,x,y):
        if x >= self.mMinX and x + self.mSize <= self.mMaxX:
            if y >= self.mMinY and y + self.mSize <= self.mMaxY:
                self.mY = y
                self.mX = x
    #
    def setSpeed(self,dx,dy):
        self.mDX = dx
        self.mDY = dy
    #    
    def setLeftPaddleY(self, paddle_min_y, paddle_max_y):
        if paddle_min_y >= self.mMinY:
            if paddle_max_y <= self.mMaxY:
                if paddle_min_y < paddle_max_y:
                    self.mLeftPaddleMinY = paddle_min_y
                    self.mLeftPaddleMaxY = paddle_max_y
    #                
    def setRightPaddleY(self, paddle_min_y, paddle_max_y):
        if paddle_min_y >= self.mMinY:
            if paddle_max_y <= self.mMaxY:
                if paddle_min_y < paddle_max_y:
                    self.mRightPaddleMinY = paddle_min_y
                    self.mRightPaddleMaxY = paddle_max_y
    #                
    def checkTop(self, new_y):
        if new_y < self.mMinY:
            self.mDY = self.mDY * -1
            holder = self.mMinY - new_y
            holder2 = self.mMinY + holder
            return holder2
        else:
            return new_y
    #        
    def checkBottom(self, new_y):
        if new_y + self.mSize > self.mMaxY:
            self.mDY = self.mDY  * -1
            holder = new_y + self.mSize
            holder2 = self.mMaxY - holder
            holder3 = holder2 + self.mMaxY - self.mSize
            return holder3
        else:
            return new_y
    #
    def checkLeft(self, new_x):
        if new_x > self.mMinX:
            return new_x
        else:
            self.mDX = 0
            self.mDY = 0
            new_x = self.mMinX
            return new_x
    #
    def checkRight(self, new_x):
        if new_x + self.mSize > self.mMaxX:
            self.mDX = 0
            self.mDY = 0
            holder = self.mMaxX - self.mSize
            return holder
        return new_x    
    #        
    def checkLeftPaddle(self, new_x, new_y):
        mid_y = (new_y + self.mY) / 2
        if mid_y >= self.mLeftPaddleMinY:
            if mid_y <= self.mLeftPaddleMaxY:
                if new_x <= self.mLeftPaddleX and self.mX >= self.mLeftPaddleX:
                    self.mDX *= -1
                    holder = self.mLeftPaddleX - new_x
                    holder2 = holder + self.mLeftPaddleX
                    return holder2
        return new_x

    #
    def checkRightPaddle(self, new_x, new_y):
        mid_y = (new_y + self.mY) / 2
        if mid_y >= self.mRightPaddleMinY:
            if mid_y <= self.mRightPaddleMaxY:
                if new_x+self.mSize >= self.mRightPaddleX and \
                        self.mX+self.mSize <= self.mRightPaddleX:
                    self.mDX *= -1
                    holder = self.mRightPaddleX  - (self.mSize + new_x)
                    holder2 = holder + self.mRightPaddleX - self.mSize
                    return holder2
        return new_x
    #
    def move(self, dt):
        new_x = (self.mDX * dt) + self.mX
        new_y = (self.mDY * dt) + self.mY
        
        new_y = self.checkTop(new_y)
        new_y = self.checkBottom(new_y)
        new_x = self.checkLeft(new_x)
        new_x = self.checkRight(new_x)
        new_x = self.checkLeftPaddle(new_x, new_y)
        new_x = self.checkRightPaddle(new_x, new_y)
        
        self.setPosition(new_x, new_y)
        '''
        uses checkTop, checkBottom, checkLeft, checkRight,
        checkLeftPaddle, checkRightPaddle to update values new_x, new_y
        sets mX and mY from values of new_x and new_y
        '''
    #
    def serveLeft(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        y = random.uniform(min_y, max_y)
        self.setPosition(x,y)
        DX = random.uniform(min_dx,max_dx)
        DY = random.uniform(min_dy,max_dy)
        self.setSpeed(DX,DY)
    #    
    def serveRight(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        y = random.uniform(min_y, max_y)
        self.setPosition(x,y)
        DX = random.uniform(min_dx,max_dx)
        DX *= -1
        DY = random.uniform(min_dy,max_dy)
        self.setSpeed(DX,DY)
    
    def draw(self, surface):
        pygame.draw.rect(surface, (255,255,255), pygame.Rect(self.mX, self.mY, self.mSize, self.mSize), 5)