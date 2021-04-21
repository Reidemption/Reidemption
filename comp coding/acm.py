import sys
# https://open.kattis.com/problems/acm
#1
lines = sys.stdin.readlines()[:-1]
submissions = []
correct = []
log = ''
while True:
    log = input()
    if log == '-1':
        break
    values = log.split()
    m = int(values[0])
    letter = values[1]
    good = values[2]   

    #count the minutes
    if letter not in submissions:
        submissions[letter] = 0
    if good == 'right':
        submissions[letter] += m
        correct.append(letter)
    else:
        submissions[letter] += 20

score = 0
for problem in correct:  
    score += submissions[problem]

print(len(correct), score) 