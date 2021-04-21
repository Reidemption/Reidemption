def startup():
    print("Hey Dipper, I'll calculate the temperature for you.")
    print("Using your stopwatch, count how many times the cricket chirps in 13 seconds.")


def program(x):

    if x + 40 < 55:
        return "Too cold for cricket existence."
    else:
        return "It is "+ str(x + 40)+ " degrees."


def main():

    startup()
    x = input("How many chirps did you hear? ")
    x= int(x)
    value = program(x)
    print(value)

main()
