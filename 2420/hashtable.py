import math

def isPrime(size):
    square = int(math.sqrt(size))
    for i in range(2,square+1):
        if size % i == 0:
            return False
    return True

#Cannot enter in True, False, or None. Will not function
class HashTable: #classes inserted into the HashTable must overrride their __int__ method to convert key field into an int.
    def __init__(self, size):
        actualSize = size*2+1
        while not isPrime(actualSize):
            actualSize += 2
        self.Table = []
        for i in range(actualSize):
            self.Table.append(None)
        self.mSize = 0

    def Insert(self,item):
        #return False if duplicate
        if self.Exists(item):
            return False
        key = int(item)
        index = key % len(self.Table)
        while self.Table[index]:
            index += 1
            if index >= len(self.Table):
                index -= len(self.Table)
        self.Table[index] = item
        self.mSize += 1
        return True

    def Delete(self,item):
        #return False if not found
        if not self.Exists(item):
            return False
        key = int(item)
        index = key % len(self.Table)
        while not (self.Table[index] and self.Table[index] == item): #While there is something there and it's not the item we're looking for
            index += 1
            if index >= len(self.Table):
                index -= len(self.Table)
        self.Table[index] = False #Use False to be able to tell if something has been deleted, allows the while statement to stop and place an item at that location
        self.mSize -= 1
        return True

    def Retrieve(self, item):
        #return the item or return None
        if not self.Exists(item):
            return None
        key = int(item)
        index = key % len(self.Table)
        while not (self.Table[index] and self.Table[index] == item): #While there is something there and it's not the item we're looking for
            index += 1
            if index >= len(self.Table):
                index -= len(self.Table)
        return self.Table[index]
        
    def Size(self):
        #returns the how many items there are
        return self.mSize

    def Exists(self, item):
        #returns False if the item doesn't exist
        key = int(item)
        index = key % len(self.Table)
        while True:
            if self.Table[index] is None:
                return False
            if self.Table[index] and self.Table[index] == item:
                return True
            index += 1
            if index >= len(self.Table):
                index -= len(self.Table)

    def Traverse(self, callback): #enter their function that they want called 1 at a time
        for item in self.Table:
            if item is not None or False:
                callback(item)