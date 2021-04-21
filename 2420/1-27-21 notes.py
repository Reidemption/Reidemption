#countingsort
#complexity is N

#make sure the values in the list are 1 smaller than the size of the list
#ex list len(9) = num 1-8
A = [3,1,4,1,5,1,2,6]
#f = frequency list
f = [0,0,0,0,0,0,0,0]
#uses the index to keep track of the numbers in the list
f2 = [0,3,1,1,1,1,1,0]



def countingsort(A):
    #make list f full of 0
    f = [0] * (len(A) + 1)
    for i in A:
        f[i] += 1
    num_items_before = 0
    #loop through values of A populating f
    for j, count in enumerate(f):
        f[j] = num_items_before
        num_items_before += count

    sorted_list = [None] * len(A)

    for item in A:
        sorted_list[f[item]] = item

        f[item] += 1

    return sorted_list
    #loop through values of f overwriting A

#famous problems in CS

#travelingsalesmanproblem
#shortest path between multiple points
#N! = N factorial (20*19*18*...)

#SAT Problem
#satisfiability
#combination of boolean expressions

"""
def createrandomlist(N):
    A = []
    while len(A) < N:
        r = random.randrange(0,N):
        if not r in A:
            A.append(r)
    return A
"""
#complexity is N^3