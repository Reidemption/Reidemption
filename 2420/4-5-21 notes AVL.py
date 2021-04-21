#4-5-21 notes

#AVL Balanced
#Nodes are balanced = Left and Right subtree nodes are within 1 of each other

#2-3 Full
# Full = check depth of the tree and everything has both a left and right node (2^depth - 1) 

#2 nodes = 1 item 2 pointers
#3 nodes = 2 items 3 pointers
#Everything on the left item is less than pointer 1, middle item is between pointers 1 and 2, right item is greater than right pointer
#Always stays full

#size of harddrive/number of items in memory
#Ex: When would a 100 tree be useful: Data is stored on harddrive, when the data is too large to be stored on RAM

#In-Order Traversal: start at root, left children, right children
#Pre-Order Traversal: Me First
#Post-Order Traversal: Me Last

#In-order
def TraverseR(self, callback, current):
    if current:
        self.TraverseR(callback, current.mL)
        callback(current.mL)
        self.TraverseR(callback, current.mL)

#Pre-Order
def TraverseR(self, callback, current):
    if current:
        callback(current.mL)
        self.TraverseR(callback, current.mL)
        
        self.TraverseR(callback, current.mL)

#Post-Order
def TraverseR(self, callback, current):
    if current:
        self.TraverseR(callback, current.mL)
        self.TraverseR(callback, current.mL)
        callback(current.mL)