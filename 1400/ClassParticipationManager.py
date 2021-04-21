import random

def intro():
    print("Welcome to Participation Manager!\n")
    print("I'll read your roll file and randomly pick")
    print("students for you.")
    print()
    print()

def getStudents(filename):
    print(random.choice(list(open(filename))))
    q = input("q to quit: ")
    while q != 'q':
        print(random.choice(list(open(filename))))
        q = input("q to quit: ")
    
        

def main():
    intro()
    filename = input("What is the name of the roll file? ")
    getStudents(filename)

main()
    
    
