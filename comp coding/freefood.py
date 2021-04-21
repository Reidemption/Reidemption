'''
3
10 14
13 17
25 26

10
'''

'''
2
1 365
20 28

365
'''
'''
4
29 29
48 48
102 102
94 94

4
'''
import sys

for i in sys.stdin:
    ab = i.split()
    a = int(ab[0])
    b = int(ab[1])

N = int(input())
for i in range(N):
    days = []
    line = input()
    values = line.split()
    start, stop = int(values[0]), int(values[1])+1
    for num in range(start,stop):
        if num not in days:
            days.append(num)

print(len(days))


