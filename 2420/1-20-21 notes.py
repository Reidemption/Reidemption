'''
log2N binarysearch
N linearsort
N^2 bubble sort
N^3 max sequence
2^N towers of hanoi
'''
#takes a list (A) and the value you're looking for (X) and returns the index of X
def linearsearch(A,X):
    for i in range(len(A)):
        if A[i] == X:
            return i
    return -1

def linearsearch2(A,X):
    return A.find(X)

#binarysearch
#uses logN

#mergesort
'''breaks the list into 2 pieces L and R

A = [4,2,3,1,1,7,2,0]
L = [4,2,3,1] = [1,2,3,4] - index i keeps track
R = [1,7,2,0] = [0,1,2,7] - index j keeps track
uses value of i[0] and j[0] and uses the lower value
increments the position of the i or j, whichever gets used
faster than bubblesort
Nlog2N = complexity
'''
def mergesort(A):
    if len(A) <= 1:
        return
    L = A[0:len(A)//2]
    R = A[len(A)//2:]
    #magically sort the lists L + R
    mergesort(L)
    mergesort(R)
    #merge L + R back over the original A
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
    while j <(len(R)):
        A[k] = R[j]
        j += 1
        k += 1
    
    return

A = [5,3,6,7,9,3,2,2]
mergesort(A)
print(A)



#quicksort

#modifiedsort

#countingsort