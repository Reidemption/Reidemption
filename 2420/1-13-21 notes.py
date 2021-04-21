#Learning Bubble Sort, Shaker Sort, and Selection Sort

#bubble sort

def bubblesort(A):
    switched = True
    while switched == True:
        length = len(A)
        switched = False
        for i in range(length-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                switched = True
    return A
    
A = [7,4,6,5,3,1,2,0]
print(bubblesort(A))

#shaker sort
#'order' N^2
#fastest algorithm for lists that are mainly sorted already
def shakersort(A):
    switched = True
    while switched == True:
        length = len(A)
        switched = False
        for i in range(length-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                switched = True
        for i in range(length-2, -1, -1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                switched = True
    return A

A = [7,4,6,5,3,1,2,0]
print(shakersort(A))

#create a deep copy
#A = CreateRandomList(10)
#B = A doesn't work
B = A[:] #THIS DOES WORK
bubblesort(A)
B.sort()
if A != B:
    print("Error in bubblesort.")

#selection sort
#uses 2 for loops
#always N^2

def selectionsort(A):
    for i in range(len(A)-1):
        smallest_index = i
        for j in range(i, len(A)):
            if A[smallest_index] > A[j]:
                smallest_index = j
        A[i], A[smallest_index] = A[smallest_index], A[i]
    return A

'''
#also works

for i in range(len(A)):
    smallest_index = i
    for j in range(i+1, len(A)):
        if A[smallest_index] > A[j]:
            smallest_index = j
    A[i], A[smallest_index] = A[smallest_index], A[i]
return A

'''

A = [5,4,3,1,4,1,5,9,0]
print(selectionsort(A))


