#we need to have the algorithms memorized, not the code
#Sorting3 Notes

def bubblesort(A,C):
    switched = True
    while switched:
        switched = False
        for i in range(len(A)-1):
            #make sure to increment the DATA compare BEFORE each if statement
            C.compares += 1
            if A[i] > A[i+1]:
                #make sure to increment the swap AFTER each if statement
                C.swaps += 1
                A[i], A[i+1] = A[i+1], A[i]
                switched = True
    return
'''
mergesort(A,C)
L = ...
R = ...
C.swaps += len(A)
...
while
while
while
C.swaps += len(A)
return

countingsort(A,C)
#does no data compares
#does no data swaps
C.compares = len(A)
C.swaps = len(A)
return

def quicksortR(A,C,low,high,mod)


#create this function inbetween main and quicksort
#have it use recursion; same with modified quicksort
def quicksort(A,C):
    quicksortrecursion(A,C,0,len(A)-1)

#can reuse the recursive for the modified and regular quicksort functions by adding a boolean statement
#if modify:
    mid = low+high//2
    A[low],A[mid] = A[mid], A[low]
'''

class Counts:
    def __init__(self):
        self.compares = 0
        self.swaps = 0

#call the quicksortR and modquicksortR in main instead of the original
def main():
    A = createrandomlist(10)
    C = Counts()
    bubblesort(A,C)
    print(C.swaps, C.compares)
    quicksort(A,C)


'''
import math
def main():

    sorts = [Bubblesort,...]
    for name in sorts:
        print("%10s" % (name), end='')
    print()

    for size in range(3, 13):
        size = 2 ** 6
        print("%10i" %(size), end='')
        for sort in sorts:
            A = createRandomList(size)
            C = Counts()
            sort(A,C)
            #if c.swaps == 0:
                #print(0)
            print("%10.2f" % (math.log(C.compares, 2)), end='')

        print()

'''