import sys, random

def quicksort(A, low, high):
    if high - low <= 0:
        return
    pivot = low
    lmbt = low + 1
    for i in range(low+1, high+1):
        if A[i] < A[pivot]:
            A[i], A[lmbt] = A[lmbt], A[i]
            lmbt += 1
    pivot = lmbt - 1
    A[low],A[pivot] = A[pivot], A[low]
    quicksort(A, low, pivot-1)
    quicksort(A,pivot+1, high)
    return

def mergesort(A):
    if len(A) <= 1:
        return 
    L = A[:len(A)//2]
    R = A[len(A)//2:]
    mergesort(L)
    mergesort(R)
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            k += 1
        else:
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

def modifiedsort(A, low, high):
    if len(A) <= 1:
        return
    if high - low <= 0:
        return
    mid = (low + high) // 2
    A[low],A[mid] = A[mid], A[low]
    #do 1 pass of the quicksort
    pivot = low # = 0
    lmbt = pivot+1 # = 1
    for i in range(low+1, high+1):
        if A[i] < A[pivot]:
            A[i], A[lmbt] = A[lmbt], A[i]
            lmbt += 1
    pivot = lmbt -1
    A[low], A[pivot] = A[pivot], A[low]
    modifiedsort(A,low, pivot-1)
    modifiedsort(A,pivot+1,high)
    return
    
def modifiedsortR(A):
    modifiedsort(A,0,len(A)-1)
    return

def quicksortR(A):
    quicksort(A,0,len(A)-1)
    return

def countingsort(A):
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

def createRandomList():
    random_list = []
    for num in range(10):
        random_list.append(random.randrange(10))
    return random_list

def main():

    sorts = {
        'countingsort':countingsort,
        'quicksort':quicksortR,
        'modifiedsort':modifiedsortR,
        'mergesort':mergesort
        }
    for sort in sorts:
        A = createRandomList()
        b = A[:]
        sorts[sort](b)
        print(f"Unsorted list A:{A}")
        A.sort()
        print(f"{sort} sorted list A: {b}")
        print(f"Python sorted list A: {A}")
        
        

if __name__ == '__main__':
    main()
