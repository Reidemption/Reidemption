#hash function takes a key and converts to an index number
#make the size of the table double and then a prime number
#index = key % table size(which is a prime number)

class Student:
    
    #cast it as an int and remove the '-'
    def __int__(self):
        return self.strip("-")
