#https://open.kattis.com/problems/jackolanternjuxtaposition
#passed

def main():
    pumpkin = input()
    values = pumpkin.split()
    combos = 1
    for i in range(len(values)):
        mat = int(values[i])
        combos *= mat

    print(combos)    

main()