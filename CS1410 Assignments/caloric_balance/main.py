import sys
import caloric_balance

    ##
def formatMenu():
    return ['What would you like to do?', '[f] Record Food Consumption', '[a] Record Physical Activity', '[q] Quit']

    ##
def formatMenuPrompt():
    return 'Enter an option: '

    ##
def formatActivityMenu():
    return ['Choose an activity to record', '[b] Badminton', '[t] Table Tennis', '[s] Squats', '[g] Golf']

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
def createCaloricBalance():
    gender = getUserString('Please enter your gender: ')
    age = getUserFloat('Please enter your age: ')
    height = getUserFloat('Please enter your height in inches: ')
    weight = getUserFloat('Please enter your weight in pounds: ')
    #create an instance of the CaloricBalance and return that instance
    CaloricBalance = caloric_balance.CaloricBalance(gender,age,height,weight)
    return CaloricBalance
    
    ##
def recordActivityAction(CaloricBalance):
    menu = formatActivityMenu()
    for i in menu:
        print(i)
    action = getUserString('Enter an option: ')
    if action == 'b':
        exercise = .044
    elif action == 't':
        exercise = 0.031
    elif action == 's':
        exercise = 0.096
    elif action == 'g':
        exercise = 0.038
    else:
        return print('Please select a valid option.')
    minutes = getUserFloat('How many minutes did you perform this activity? ')
    CaloricBalance.recordActivity(exercise, minutes)
    print(f"Your new caloric balance is: {CaloricBalance.getBalance()}")
    
    ##
def eatFoodAction(CaloricBalance):
    food = getUserFloat("How many calories did you eat? ")
    CaloricBalance.eatFood(food)
    print(f"Your new caloric balance is: {CaloricBalance.getBalance()}")

    ##
def quitAction(CaloricBalance):
    print('Program will now end..')
    sys.exit(0)
    
    ##
def applyAction(CaloricBalance, string):
    if string == 'q':
        quitAction(CaloricBalance)
    elif string == 'f':
        eatFoodAction(CaloricBalance)
    elif string == 'a':
        recordActivityAction(CaloricBalance)
    else:
        print('Please select a valid option.')
        
def main():
    print('Hi! This program will calculate your caloric balance for the day!')
    print('Before we can start, I need some information about you. Be honest! :) \n')
    CaloricBalance = createCaloricBalance()
    print('Thanks! Now, throughout the day, tell me each time you eat or exercise.')
    print(f'Your starting balance is: {CaloricBalance.getBalance()} (You should probably eat something!)')
    menu = formatMenu()
    while True:
        
        print()
        for i in range(len(menu)):
            print(menu[i])
        
        string = getUserString(formatMenuPrompt())
        applyAction(CaloricBalance, string)
        
        
if __name__ == '__main__':
    main()
    
    