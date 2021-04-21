def startup():
    print("Welcome to the highway travel advisor.")
    print("This application has been configured to work")
    print("with travel on I-15 within the state of Utah.")
    print("We'll ask for a few pieces of information, then")
    print("give you advice on your travel.")

def on_I15():
    on_ramp = input("Enter I-15 at what mile marker? ")
    on_ramp = float(on_ramp)
    return on_ramp
def off_I15():
    off_ramp = input("Exit I-15 at what mile marker? ")
    off_ramp = float(off_ramp)
    return off_ramp
def travel_time_input():
    wanted_travel_time = input("How many hours from now do you want to arrive? ")
    wanted_travel_time = float(wanted_travel_time)
    return wanted_travel_time
def desired_average_mph():
    average_mph = input("Expected average speed in MPH? ")
    average_mph = float(average_mph)
    return average_mph
def total_travel_distance(on_ramp, off_ramp):
    if on_ramp > off_ramp:
        total_mileage = on_ramp - off_ramp
        return total_mileage
    else:
        total_mileage = off_ramp - on_ramp
        return total_mileage
def total_travel_time(total_mileage, average_mph):
    travel_time = total_mileage / average_mph
    return travel_time
def will_you_make_it(wanted_travel_time, travel_time):
    time_of_arrival = wanted_travel_time - travel_time
    return time_of_arrival
def traffic_warning(total_mileage, time_of_arrival, speed):
    if speed > 80:
        print("Your speed is dangerously high.  Slow down.")
    elif speed < 60:
        print("Your speed is too slow.  You'll be a hindrance to other traffic.")
    else:
        print("You will be traveling " + str(total_mileage) + " miles")
        if time_of_arrival >= 0:
            print("Leave in the next " + str(time_of_arrival) + " to be on time.")
        else:
            time_of_arrival = time_of_arrival * -1
            print("You won't be able to get there on time.  You'll be " + str(time_of_arrival) + " hours late.")


def done():
    print("Thanks for using the highway travel advisor.")

def main():
    startup()
    on_ramp = on_I15()
    off_ramp = off_I15()
    wanted_travel_time = travel_time_input()
    speed = desired_average_mph()
    total_mileage = total_travel_distance(on_ramp, off_ramp)
    travel_time = total_travel_time(total_mileage, speed)
    time_of_arrival = will_you_make_it(wanted_travel_time, travel_time)
    traffic_warning(total_mileage, time_of_arrival, speed)
    done()

main()
