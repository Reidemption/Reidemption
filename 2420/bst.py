#does not add duplicates

class Node:
    def __init__(self, item):
        self.mItem = item
        self.mLeft = None
        self.mRight = None

class BinarySearchTree:
    def __init__(self):
        self.mRoot = None
        self.mSize = 0

    def Insert(self,item):
        #return False if duplicate
        if self.Exists(item):
            return False
        n = Node(item)
        self.mRoot = self.InsertRecursive(n, self.mRoot)
        self.mSize += 1
        return True

    def InsertRecursive(self, n, root):
        if root == None:
            root = n
        elif n.mItem < root.mItem:
            root.mLeft = self.InsertRecursive(n, root.mLeft)
        else:
            root.mRight = self.InsertRecursive(n, root.mRight)
        return root

#2 children: replace the item in the node with the in order successor and delete the original and rewire it
#in order successor - go right once then the left most item

    def Delete(self,item):
        #return False if not found
        if not self.Exists(item):
            return False
        self.mSize -= 1
        self.DeleteRecursive(item, self.mRoot)
        return True
    
    def DeleteRecursive(self, item, current):
        if item < current.mItem:
            current.mLeft = self.DeleteRecursive(item, current.mLeft)
        elif item > current.mItem:
            current.mRight = self.DeleteRecursive(item, current.mRight)
        else: #current is pointing to the node with the item to be deleted
            #Case 1: Current has no children
            if current.mLeft is None and current.mRight is None:
                current = None
            #Case 2a : Current has 1 right child:
            elif  current.mLeft is None and current.mRight is not None:
                current = current.mRight
            #Case 2b: Current has 1 left child
            elif  current.mLeft is not None and current.mRight is None:
                current = current.mLeft
            #Case 3: Current has 2 children
            else:
                successor = current.mRight
                while successor.mLeft is not None:
                    successor = successor.mLeft
                current.mItem = successor.mItem
                current.mRight = self.DeleteRecursive(successor.mItem, current.mRight)
        return current

    def Retrieve(self, item):
        #return the item or return None
        current = self.mRoot
        while current != None:
            if current.mItem == item:
                return current.mItem
            elif item < current.mItem:
                current = current.mLeft
            else:
                current = current.mRight
        return None

    def Size(self):
        #returns the how many items there are
        return self.mSize

    def Exists(self, item):
        #returns False if the item doesn't exist
        return self.ExistsRecursive(item, self.mRoot)

    def ExistsRecursive(self, item, current):
        if current is None:
            return False
        elif current.mItem == item:
            return True
        elif item < current.mItem:
            return self.ExistsRecursive(item, current.mLeft)
        else:
            return self.ExistsRecursive(item, current.mRight)
        
    
    #enter their function that they want called 1 at a time
    def Traverse(self, callback):
        self.TraverseRecursive(callback, self.mRoot)

    def TraverseRecursive(self, callback, current):
        if current is None:
            return
        callback(current.mItem)
        self.TraverseRecursive(callback, current.mLeft)
        self.TraverseRecursive(callback, current.mRight)
