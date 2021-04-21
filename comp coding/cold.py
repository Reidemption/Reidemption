#https://open.kattis.com/problems/cold
import sys

def main():
    cold = sys.stdin.readlines()[:-1]
    counter = 0
    temps = input()
    tempp = temps.split()
    for temp in tempp:
        if temp < 0:
            counter += 1
    print(counter)

main()