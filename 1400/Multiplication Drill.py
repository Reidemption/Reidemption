import time

def intro():
    print("Welcome to Multiplication Quiz\n")
    print("I'll ask you questions, and you answer them.")
    
def usedinput():
    z = int(input("What number do you want to multiply? "))
    while z > 12 or z < 0:
        z = (input("What number do you want to multiply? "))
    return z
    
    
def main():
    startTime = time.time()
    intro()
    x = usedinput()
#    for i in range(0,13):
    a = int(input("What is " + str(x) + " x 0? "))
    while a != 0:
        print("Oops! Try again.")
        a = int(input("What is " + str(x) + " x 0? "))
    b = int(input("What is " + str(x) + " x 1? "))
    while b != 1*x:
        print("Oops! Try again.")
        b = int(input("What is " + str(x) + " x 1? "))
    c = int(input("What is " + str(x) + " x 2? "))
    while c != 2*x:
        print("Oops! Try again.")
        c = int(input("What is " + str(x) + " x 2? "))
    d = int(input("What is " + str(x) + " x 3? "))
    while d != 3*x:
        print("Oops! Try again.")
        d = int(input("What is " + str(x) + " x 3? "))
    e = int(input("What is " + str(x) + " x 4? "))
    while e != 4*x:
        print("Oops! Try again.")
        e = int(input("What is " + str(x) + " x 4? "))
    f = int(input("What is " + str(x) + " x 5? "))
    while f != 5*x:
        print("Oops! Try again.")
        f = int(input("What is " + str(x) + " x 5? "))
    g = int(input("What is " + str(x) + " x 6? "))
    while g != 6*x:
        print("Oops! Try again.")
        g = int(input("What is " + str(x) + " x 6? "))
    h = int(input("What is " + str(x) + " x 7? "))
    while h != 7*x:
        print("Oops! Try again.")
        h = int(input("What is " + str(x) + " x 7? "))
    j = int(input("What is " + str(x) + " x 8? "))
    while j != 8*x:
        print("Oops! Try again.")
        j = int(input("What is " + str(x) + " x 8? "))
    k = int(input("What is " + str(x) + " x 9? "))
    while k != 9*x:
            print("Oops! Try again.")
            k = int(input("What is " + str(x) + " x 9? "))
    l = int(input("What is " + str(x) + " x 10? "))
    while l != 10*x:
        print("Oops! Try again.")
        l = int(input("What is " + str(x) + " x 10? "))
    m = int(input("What is " + str(x) + " x 11? "))
    while m != 11*x:
        print("Oops! Try again.")
        m = int(input("What is " + str(x) + " x 11? "))
    n = int(input("What is " + str(x) + " x 12? "))
    while n != 12*x:
        print("Oops! Try again.")
        n = int(input("What is " + str(x) + " x 12 ? "))
    stopTime = time.time()
    Total_Time_Elapsed = stopTime - startTime
    print('')
    if Total_Time_Elapsed < 25:
        print("Great. That took " + str(Total_Time_Elapsed) + " seconds.")
    elif Total_Time_Elapsed < 40:
        print("Good. That took " + str(Total_Time_Elapsed) + " seconds.")
    elif Total_Time_Elapsed < 60:
        print("That took " + str(Total_Time_Elapsed) + " seconds.")
    else:
        print("That took " + str(Total_Time_Elapsed) + " seconds.\nYou can do better.")
main()             
            
