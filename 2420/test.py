def mergesort(A):
    #check length to make sure is less than eqaul to 1
    if len(A) <= 1:
        return
    #split into left and right sides
    L = A[len(A)//2:]
    R = A[:len(A)//2]
    #resursive
    mergesort(L)
    mergesort(R)
    #assign counters
    a = l = r = 0
    while l < len(L) and r < len(R):
        if L[l] <= R[r]:
            A[a] = L[l]
            l += 1
            a += 1
        else:
