def startup():
    print("Welcome to the rainwater tank calculator.")
    print("We'll ask you for a few parameters about your")
    print("rainfall and rain catchment area.  Then, we'll")
    print("tell you how big to make your tank.  We assume")
    print("that your catchment area is rectangular.")


#all multiplied together times 7.48 divided by 12
#def program(rain, wide, length):



def main():
    startup()
    rain = input("How many inches of rain fall in a large storm? ")
    rain = float (rain)
    wide = input("How wide is your catchment area, in feet? ")
    wide = float (wide)
    length = input("How long is your catchment area, in feet? ")
    length = float (length)

    x = (rain * wide * length)

    print("You need a tank with " + str(x * 7.48/12) + " gallons capacity to capture that much rain at one time.")

main()
