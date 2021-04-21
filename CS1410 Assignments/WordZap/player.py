#Reid Gubler
import random

class Player:
    
        ##
    def __init__(self, name):
        self.name = name
        self.letters = []
        for i in range(7):
            self.drawLetter()
        
        ##    
    def getName(self):
        return self.name
    
        ##
    def getLetters(self):
        return self.letters
    
        ##
    def drawLetter(self):
        letters = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        random_letter = random.choice(letters)
        self.letters.append(random_letter)
        return random_letter
            
        ##  
    def printLetters(self):
        hand = ' '.join(self.letters)
        hand.rstrip()
        return hand
    
        #create a copy of the list (b) and update letters
    ##
    def checkWord(self, word):
        if len(word) > 8:
            return False
        b = self.letters[:]
        for i in word:
            if i in b:
                b.remove(i)
            else:
                return False
        self.letters = b
        return True
