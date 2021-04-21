'''
Complexity
Algorithms
Data Structures
Math - Logs, Exponents

1st assignment - 7 sorting algorithms

Complexity ex: Max Subsequence Problem - takes list A asking for best starting and ending index so numbers add up into the maximum number
List of numbers (positive and negative)

The complexity level of this problem is [N]^3 because it loops through the problem 3 times
'''
A = [2, -3, 4, 1, 2, -4. -3, -6, 3, 1, -2, 5, 1, -2, 5, 3, 2, -3, 6]

maximum = A[0]
for i in range(0, len(A)):
	for j in range(i, len(A)):
		sum = 0
		"use 'add' instead of the 3rd for loop to quicken speed of program"
		for n in range(i, j+1):
			sum += A[n]
		if sum > maximum:
			maximum = sum
			besti = i
			bestj = j
return besti,bestj

'''
Exponent complexity = 2^N
2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64
2^7 = 128
2^8 = 256
2^9 = 512
2^10 = 1028 (1K)
2^11 = 2k
2^12 = 4k
2^13 = 8k
2^20 = 1million
2^30 = 1Billion
2^40 = 1Trillion

Log complexity = log2N
2^24 = 16M
log2 16M = 24
log2 256B = 38
'''
