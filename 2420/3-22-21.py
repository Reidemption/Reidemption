#Linked Lists
#rewatch vod
#node is 1 item and 1 address/pointer
#2 reasons why LL might be better than Python List
# 1- Works with fragmented memory; Python list must be continuous in RAM when LL doesn't have to be
# 2- Order doesn't matter
#
#Information about Linked Lists will be on final, Insert and Delete


class Node:
    def __init__(self, item, nxt):
        self.mItem = item
        self.mNext = nxt

class UnorderedUniqueContainer:
    def __init__(self):
        self.mFirst = None
        self.mSize = 0

    def Insert(self,item):
        #return False if duplicate
        if self.Exists(item):
            return False
        n = Node(item, self.mFirst)
        self.mFirst = n
        self.mSize += 1
        return True

    def Delete(self,item):
        #return False if not found
        if not self.Exists(item):
            return False
        
        self.mSize -= 1
        #First Case Scenario (item is in First node)
        if item == self.mFirst.mItem:
            self.mFirst = self.mFirst.mNext
            return True

        #General Case Scenario
        current = self.mFirst
        while current.mNext.mItem != item:
            current = current.mNext
        current.mNext = current.mNext.mNext
        return True

    def Retrieve(self, item):
        #return the item or return None
        current = self.mFirst
        while current != None:
            if current.mItem == item:
                return current.mItem
            current = current.mNext
        return None

    def Size(self):
        #returns the how many items there are
        return self.mSize

    def Exists(self, item):
        #returns False if the item doesn't exist
        current = self.mFirst
        while current != None:
            if current.mItem == item:
                return True
            current = current.mNext
        return False
    
    #enter their function that they want called 1 at a time
    def Traverse(self, callback):
        current = self.mFirst
        while current != None:
            callback(current.mItem)
            current = current.mNext

def PrintName(item):
    print(item)

#easy way
gTotalAge = 0
def AddAges(item):
    global gTotalAge
    gTotalAge += int(item.GetAge())


def main():
    global gTotalAge
    uuc = UnorderedUniqueContainer()
    uuc.Insert("John")
    uuc.Insert("Bob")
    uuc.Insert("Mary")
    uuc.Insert("Bob")
    print(uuc.Exists("John")) #True
    print(uuc.Exists("Sally")) #False
    print(uuc.Size()) #3
    uuc.Traverse(PrintName) #Mary \n Bob \n John

    uuc.Traverse(AddAges)
    print("The average age is: ", gTotalAge / uuc.Size())