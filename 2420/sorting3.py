import random, sys, math

#simpliest sort
#while for
def bubblesort(A,C):
    sorted = True
    while sorted:
        sorted = False
        for i in range(len(A)-1):
            C.compares += 1
            if A[i] > A[i+1]:
                C.swaps += 1
                A[i],A[i+1] = A[i+1],A[i]
                sorted = True
    return

#same as bubble, but you also sort going in reverse
#while for for
def shakersort(A,C):
    sorted = True
    while sorted:
        sorted = False
        for i in range(len(A)-1):
            C.compares += 1
            if A[i] > A[i+1]:
                C.swaps += 1
                A[i],A[i+1] = A[i+1],A[i]
                sorted = True
        for i in range(len(A)-2,-1,-1):
            C.compares += 1
            if A[i] > A[i+1]:
                C.swaps += 1
                A[i],A[i+1] = A[i+1],A[i]
                sorted = True
    return 

#loops through list with i the smallest, then loops through with i as the pivot spot
#for for if
def selectionsort(A,C):
    for i in range(len(A)-1):
        smallest = i
        for j in range(i,len(A)):
            C.compares += 1
            if A[smallest] > A[j]:
                smallest = j
        C.swaps += 1
        A[i], A[smallest] = A[smallest],A[i]
    return

#split list into 2 lists
#recursion
#
def mergesort(A,C):
    C.compares += 1
    if len(A) <= 1:
        return
    L = A[:len(A)//2]
    R = A[len(A)//2:]
    mergesort(R,C)
    mergesort(L,C)
    i =j=k= 0
    while i < len(L) and j < len(R):
        C.compares += 1
        if L[i] <= R[j]:
            C.swaps += 1
            A[k] = L[i]
            i += 1
            k += 1
        else:
            C.swaps += 1
            A[k] = R[j]
            j += 1
            k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
    return 


def countingsort(A,C):
    C.compares = len(A) 
    C.swaps = len(A)
    f = []
    #fill with zeros
    for i in range(len(A)):
        f.append(0)
    #for each value of A, increase f at that index
    for value in range(len(A)):
        f[A[value]] += 1 
    #overwrite A
    k = 0
    for i in range(len(f)):
        howmany = f[i]
        for j in range(howmany):
            A[k] = i
            k += 1
    return A

def quicksort(A,C,low,high):
    C.compares += 1
    if high - low <= 0:
        return
    pivot = low
    lmbt = low + 1
    for i in range(low+1, high +1):
        C.compares += 1
        if A[i] < A[pivot]:
            C.swaps += 1
            A[i], A[lmbt] = A[lmbt], A[i]
            lmbt += 1
    pivot = lmbt - 1
    A[low],A[pivot] = A[pivot], A[low]
    C.compares += 2
    quicksort(A, C, low, pivot-1)
    quicksort(A, C,pivot+1, high)
    return

def quicksortR(A,C):
    quicksort(A,C,0,len(A)-1)

def modifiedsort(A,C, low,high):
    C.compares += 1
    if len(A) <= 1:
        return
    C.compares += 1
    if high - low <= 0:
        return
    mid = (low + high) // 2
    A[low],A[mid] = A[mid], A[low]
    pivot = low
    lmbt = low + 1
    for i in range(low+1, high +1):

        if A[i] < A[pivot]:
            C.swaps += 1
            A[i], A[lmbt] = A[lmbt], A[i]
            lmbt += 1
    pivot = lmbt - 1
    A[low],A[pivot] = A[pivot], A[low]
    modifiedsort(A, C, low, pivot-1)
    modifiedsort(A, C, pivot+1, high)
    return

def modifiedsortR(A,C):
    modifiedsort(A,C,0,len(A)-1)

def createRandomList(n):
    random_list = []
    for num in range(n):
        random_list.append(random.randrange(n))
    return random_list

def createMostlyRandomList(n):
    MRL = createRandomList(n)
    MRL.sort()
    MRL[0],MRL[-1] = MRL[-1],MRL[0]
    return MRL

class Counts:
    def __init__(self):
        self.compares = 0
        self.swaps = 0

def main():
    blank = ''
    #print(C.swaps, C.compares)
    sys.setrecursionlimit(5000)
    sorts = {
        'Bubble':bubblesort,
        'Shaker':shakersort,
        'Selection':selectionsort,
        'Quick':quicksortR,
        'Mquick':modifiedsortR,
        'Merge':mergesort,
        'Hash':countingsort,
        }
    print("%11s" % (blank), end = '')
    for name in sorts:
        print("%11s" % (name), end='')
    print()
    for s in range(3,13):
        size = 2 ** s
        print("%11i" %(s), end='')

        for sort in sorts:
            A = createRandomList(size)
            C = Counts()
            sorts[sort](A,C)
            print("%11.2f" % (math.log(C.swaps, 2)), end='')

        print()

if __name__ == '__main__':
    main()
