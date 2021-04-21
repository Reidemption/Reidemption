import sys
##
def createIndex():
    return {}
#isbn and title are strings
#returns nothing but adds the isbn and title to the dictionary
##
def recordBook(index, isbn, title):
    index[isbn] = title
#returns the book that contains the isbn
#returns empty string if isbn is not there
##
def findBook(index, isbn):
    if isbn in index:
        return index[isbn]
    return ''
#The function listBooks receives one parameter, the index dictionary. The function returns a list of strings. Each string in the list is a line that
#shows a sequence number, the ISBN and the title of a book. See the examples for the format of the lines. If there are no books in the index, this
#function returns an empty list.
#use an fstring and a loop
##
def listBooks(index):
    x = 0
    y = ''
    list1 = []
    if not index:
        return list1
    for i in index:
        y = '{}) {}: {}'.format(x+1, i, index[i])
        list1.append(y)
        #print(f'{x+1}) {index[i]}:{i}')
        x += 1
    return list1
         
##The function formatMenu does not receive any parameters. It must return a list of strings that contains the lines of the menu.
##
def formatMenu():
    return [ '\nWhat would you like to do?', '[r] Record a Book', '[f] Find a Book', '[l] List all Books', '[q] Quit\n' ]

#The function formatMenuPrompt does not receive any parameters. It must return a string that contains the prompt to ask the user which menu
#option they would like to select.
##
def formatMenuPrompt():
    return 'Enter an option: '
    

#The function getUserChoice receives one parameter, a string that contains a prompt for input. It must return
#a string that contains the text input by the user, with any leading and trailing whitespace removed. If the
#user gives an empty string, prompt them again, until they give a non-empty string. Note that this function
#interacts with the user, so there will be output to the screen and input from the keyboard when it is called.
##
def getUserChoice(prompt):
    choice = ''
    while choice == '':
        choice = input(prompt).strip()
    return choice

#The function getISBN does not receive any parameters. It must prompt the user for an ISBN, and return the ISBN input by the user. The user’s
#response must not have any leading or trailing whitespace. It must repeatedly ask the user for an ISBN, until the user gives a non-empty response.
#Note, you should probably call getUserChoice as part of this function.
##
def getISBN():
    isbn = str(getUserChoice('ISBN: \n'))
    return isbn

#The function getTitle does not receive any parameters. It must prompt the user for a book title, and return the title input by the user.
#The user’s response must not have any leading or trailing whitespace. It must repeatedly ask the user for a title, until the user gives a
#non-empty response. Note, you should probably call getUserChoice as part of this function.
##
def getTitle():
    return getUserChoice('Enter book title: \n')
    
#The function recordBookAction receives the index dictionary as a parameter. It must ask the user for the ISBN and title of a book, and add it to
#the dictionary. This function does not return anything. However, it has the side effect of adding an entry to the dictionary. It also interacts
#with the user through input and output. Note you should be using some of the above functions to complete this function.
##
def recordBookAction(index):
    isbn = getISBN()
    title = getTitle()
    index[isbn] = title
    print('Book saved!')

#The function findBookAction receives the index dictionary as a parameter. It must ask the user for the ISBN a book. If the book exists in the
#dictionary, it will display the book. If the book does not exist in the dictionary, it will give the user a message to let them know. The
#function does not return anything, and should not change the index.
##
def findBookAction(index):
    isbn = getISBN()
    if isbn in index.keys():
        print("Book found: ",index[isbn])
    else:
        print('Book not found.')
    
#The function listBooksAction receives the index dictionary as a parameter. It will display all of the books in the dictionary in the format
#shown in the examples. If there are no books in the dictionary, it must display a message to inform the user. The function does not return
#anything. The function must not change the dictionary.
##
def listBooksAction(index):
    if len(index) == 0:
        print('There are no books registered')
    list_of_books = listBooks(index)
    for line in list_of_books:
        print(line)
        
##The function quitAction receives the index dictionary as a parameter. This function will display a message to the user indicating the end of the
#program. It will then terminate the program using sys.exit( 0 ). Be sure to do the correct import statement. This function does not return anything.
##
def quitAction(index):
    print('Program will now end..')
    sys.exit(0)
    
#The function applyAction receives the index dictionary and a choice string as parameters. This function will call the appropriate action function
#based on the choice string. If the choice string does not match any accepted choices, it will display a message to the user. This function does not
#return anything. The dictionary may be changed as a result of the chosen action.

def applyAction(index, choice):
        if choice == 'q':
            quitAction(index)
        elif choice == 'r':
            recordBookAction(index)
        elif choice == 'f':
            findBookAction(index)
        elif choice == 'l':
            listBooksAction(index)
        else:
            print('Please select a valid option.')

#The function main receives no parameters, and returns nothing. This function ties everything together. Creating an index, repeatedly asking the
#user their choice and taking action.
def main():
        index = createIndex()
        menu = formatMenu()
        while True:
            
            for i in range(len(menu)):
                print(menu[i])
                
            choice = getUserChoice(formatMenuPrompt())
            applyAction(index, choice)
        

if __name__ == '__main__':
    main()