import random

def main():
    guessesTaken = 0
    guess = ''
    number = random.randint(1,100)
    print("Welcome to Ricerca Binaria!")
    print("I will pick a number between 1 and 100, inclusive.")
    print("Try to guess my number in as few guesses as possible.")
    print("Don't worry, I'm a nice program.  I'll give you hints.\n \n")
    
    print("Ok, I've picked my number.")
    while guessesTaken < 1000:
        guess = input("Your guess? ")
        guess = int(guess)
        
        guessesTaken = guessesTaken + 1

        if guess < number:
            print("Too low.")
        if guess > number:
            print("Too high.")
        if guess == number:
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print("That's it!")
        print("")
        print("You guessed my number in " + guessesTaken + " tries!")

main()
