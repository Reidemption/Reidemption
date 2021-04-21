import random, sys


def bubblesort(N):
    switched = True
    while switched == True:
        switched = False
        for i in range(len(N)-1):
            if N[i] > N[i+1]:
                N[i], N[i+1] = N[i+1], N[i]
                switched = True
    return N

def shakersort(N):
    switched = True
    while switched == True:
        switched = False
        for i in range(len(N)-1):
            if N[i] > N[i+1]:
                N[i], N[i+1] = N[i+1], N[i]
                switched = True
        for i in range(len(N)-2,-1,-1):
            if N[i] > N[i+1]:
                N[i], N[i+1] = N[i+1], N[i]
                switched = True
    return N

def selectionsort(N):
    for i in range(len(N)-1):
        smallest = i
        for j in range(i, len(N)):
            if N[smallest] > N[j]:
                smallest = j
        N[i], N[smallest] = N[smallest], N[i]
    return N

def main():
    ran = random.randrange(1,25)
    bubblelist = []
    shakerlist = []
    selectorlist = []
    for i in range(0,ran):
        bubblelist.append(random.randrange(99))
        shakerlist.append(random.randrange(200))
        selectorlist.append(random.randrange(74))
    
    A =  bubblelist[:]
    B = shakerlist[:]
    C = selectorlist[:]

    print(bubblelist)
    A.sort()
    print(bubblesort(bubblelist))
    print(A)

    print(shakerlist)
    print(shakersort(shakerlist))
    B.sort()
    print(B)

    print(selectorlist)
    print(selectionsort(selectorlist))
    C.sort()
    print(C)


if __name__ == '__main__':
    main()
