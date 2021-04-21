import pygame
import text

class ScoreBoard():
    #
    def __init__(self, x, y, width, height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mLeftScore = 0
        self.mRightScore = 0
        self.mServeStatus = 1
        '''
        1 = left serve
        2 = right serve
        3 = left win
        4 = right win
        '''
        
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
    def getLeftScore(self):
        return self.mLeftScore
    #
    def getRightScore(self):
        return self.mRightScore
    #
    def getServeStatus(self):
        return self.mServeStatus
    
    def isGameOver(self):
        if self.mServeStatus == 4 or self.mServeStatus == 3:
            return True
        return False
    
    def scoreLeft(self):
        if not self.isGameOver():
            self.mLeftScore += 1
            if self.mLeftScore >= 9:
                self.mServeStatus = 3
                self.isGameOver()
            
            
    def scoreRight(self):
        if not self.isGameOver():
            self.mRightScore += 1
            if self.mRightScore >= 9:
                self.mServeStatus = 4
                self.isGameOver()

            
    def swapServe(self):
        if self.mServeStatus == 2:
            self.mServeStatus = 1
        elif self.mServeStatus == 1:
            self.mServeStatus = 2
                
    def draw(self, surface):
        left = text.Text(str(self.mLeftScore), 200, 100)
        right = text.Text(str(self.mRightScore), 600,100)
        if self.isGameOver():
            left = text.Text('GAME', 200, 100)
            right = text.Text('OVER', 600,100)

        left.draw(surface)
        right.draw(surface)
        