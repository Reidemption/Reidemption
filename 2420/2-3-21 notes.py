#only works if the numbers inside of the list are smaller than the length of the list
#if there may be a number greater than the length of the list, increase the size of f to the greatest number

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

A = [9,8,7,0,4,5,5,0,3,2]
print(A)
print(countingsort(A))

#sys.setrecursionlimit(5000)
#use this line in program3 in the main function


'''
multiply problem
N^2

factoring problem
10^(N/2)

order 1 = list append
list pop

faster to switch position of last and first when trying to pop any item in a list
lists are passed by reference so the same list is being used between functions, while values will be a copy if called

value (copy) = int,char,floats,strings
reference = list, dictionary, objects

order list
1
logN
N
NlogN
N^2
N^3
N^P


2^N
10^(N/2)
N!


'''