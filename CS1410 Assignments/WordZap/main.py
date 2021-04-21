#Reid Gubler
import player
import sys

def getUserInt(prompt):
    zeropoint = 0
    while True:
        try:
            userfloat = int(input(prompt))
            if userfloat > zeropoint:
                break
            print('Please enter a positive number above 0.')
        except ValueError:
            print('Please enter a positive number above 0.')
    return userfloat
    
def getUserString(prompt):
    string = input(prompt).strip()
    return string
    
    #have a players list thatll append everytime a new player is created
def getPlayers():
    el = []
    players = getUserInt('How many players will be playing? ')
    for i in range(players):
        player1 = getUserString(f'Enter the name for player {i+1} ')
        el.append(player.Player(player1))
    return el

    ##
def convertToLower(word):
    return word.lower()    
    
def main():
    print('Welcome! Time to play! Try to use all of your letters.')
    print('The first player that uses all of their letters wins!\n')
    play = getPlayers()
    print('\nGreat now we can play!')
    rou = 1
    while True:
        for i in play:
            name = i.getName()
            letters = i.printLetters()
            print()
            print(f'Okey {name} your turn!')
            print(f'your letters are: {letters}')
            x = getUserString('Enter a word to play (or press enter to pass) ')
            x = convertToLower(x)
            if x == '':
                let = i.drawLetter()
                print(f'You get another letter, "{let}"')
                word = True
            else:
                word = i.checkWord(x)
                if word == True: 
                    print('Good job!')
                else:
                    print('Check your letters and try again!\n')
                    while word == False:
                        print(f'Okey {name} your turn!')
                        print(f'your letters are: {letters}')
                        x = getUserString('Enter a word to play (or press enter to pass) ')
                        x = convertToLower(x)
                        if x == '':
                            let = i.drawLetter()
                            print(f'You get another letter, "{let}"')
                            word = True
                        else:
                            word = i.checkWord(x)
                            if word == True: 
                                print('Good job!')
                            else:
                                print('Check your letters and try again!')
            if len(i.getLetters()) == 0:
                print()
                print (f'{name} wins!!')
                sys.exit(0)
        print()
        print('End of round', rou)
        rou += 1
                

if __name__ == '__main__':
    main()
    