import sys


def milesPerGallon(miles,gallons):
    mph = 0.0
    if miles == 0 or gallons == 0:
        return mph
    mph = float(miles) / float(gallons)
    return round(mph, 2)

##
def createNotebook():
    return []

##
def recordTrip(notebook, date, miles, gallons):
    new_entry = {'date':date,'miles':miles,'gallons':gallons}
    notebook.append(new_entry)

##
def listTrips(notebook):
    holder = ''
    listTrip = []
    for entry in range(len(notebook)):
        for key in notebook[entry]:
            d = notebook[entry]['date']
            m = notebook[entry]['miles']
            g = notebook[entry]['gallons']
            gas_mileage = milesPerGallon(notebook[entry]["miles"],notebook[entry]["gallons"])
        holder = f'On {d}: {m} miles traveled using {g} gallons. Gas mileage: {gas_mileage} MPG'
        listTrip.append(holder)
    return listTrip

##
def calculateMPG(notebook):
    total_miles = 0.0
    total_gallons = 0.0
    if len(notebook) == 0:
        return 0.0
    for i in range(len(notebook)):
        for key in notebook[i]:
            total_miles += notebook[i]['miles']
            total_gallons += notebook[i]['gallons']
    if total_miles == 0 or total_gallons == 0:
        return 0.0
    return total_miles / total_gallons

##
def formatMenu():
    return ['What would you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History', '[c] Calculate Gas Mileage', '[q] Quit']

##
def formatMenuPrompt():
    return 'Enter an option: '
    
##
def getUserString(prompt):
    string = ''
    while string == '':
        string = input(prompt).strip()
    return string

##
def getUserFloat(prompt):
    zeropoint = 0.0
    while True:
        try:
            userfloat = float(input(prompt))
            if userfloat > zeropoint:
                break
            print('Please enter a positive number above 0.')
        except ValueError:
            print('Please enter a positive number above 0.')
    return userfloat

##
def getDate():
    return getUserString('What is the date? ')

##
def getMiles():
    return getUserFloat('How many miles did you drive since last filling up? ')

##
def getGallons():
    return getUserFloat('How many gallons of gas did you add to your tank? ')
    
##
def recordTripAction(notebook):
    date = getDate()
    miles = getMiles()
    gallons = getGallons()
    recordTrip(notebook, date, miles, gallons)
    print('Trip has been saved\n')
    
##
def listTripsAction(notebook):
    if len(notebook) == 0:
        print('There are no trips registered.')
    trips = listTrips(notebook)
    for entry in trips:
        print(entry)
    
##
def calculateMPGAction(notebook):
    if len(notebook) == 0:
        print('There are no trips registered.')
    mpg = calculateMPG(notebook)
    print(f'Average gas mileage: {mpg} MPG')
        
##        
def quitAction(notebook):
    print('Program will now end..')
    sys.exit(0)

##
def applyAction(notebook, string):
    if string == 'q':
        quitAction(notebook)
    elif string == 'r':
        recordTripAction(notebook)
    elif string == 'c':
        calculateMPGAction(notebook)
    elif string == 'l':
        listTripsAction(notebook)
    else:
        print('Please select a valid option.')

def main():
    notebook = createNotebook()
    menu = formatMenu()
    while True:
            
        for i in range(len(menu)):
            print(menu[i])
                
        string = getUserString(formatMenuPrompt())
        applyAction(notebook, string)
        

if __name__ == '__main__':
    main()
