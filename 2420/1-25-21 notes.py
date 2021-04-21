#quicksort
#does 1 pass in 1st layer of recursion
#far left item is the pivot item

#not really used because it's not good when there is a low number at the start


A = [4,2,7,3,1,6,5,1]

def quicksort(A,low,high):
    if high - low <= 0:
        return
    #do 1 pass of the quicksort
    pivot = low # = 0
    lmbt = low+1 # = 1
    for i in range(low+1, high+1):
        if A[i] < A[pivot]:
            A[i], A[lmbt] = A[lmbt], A[i]
            lmbt += 1
    pivot = lmbt -1
    A[low], A[pivot] = A[pivot], A[low]
    quicksort(A,low, pivot-1)
    quicksort(A,pivot+1,high)
    return

quicksort(A,0,7)
print(A)

A = []

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

B = [1,5,3,2,7,8,8,6]

modifiedsort(B,0,len(B)-1)
print(B)