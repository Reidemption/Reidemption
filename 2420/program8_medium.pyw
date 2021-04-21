#check program 5 for outline
#in class questions: How to use error messages when 
import time, hashtable

class Student:
    def __init__(self, lname, fname, ssn, mail, age):
        self.lname = lname
        self.fname = fname
        self.ssn = ssn
        self.mail = mail
        self.age = age
    
    def __int__(self):
        return int(self.ssn.replace('-',''))
    
    def __eq__(self, other):
        return self.ssn == other.ssn

    def __gt__(self, other):
        if(self.ssn > other.ssn):
            return True
        else:
            return False

    def __lt__(self, other):
        if(self.ssn < other.ssn):
            return True
        else:
            return False

    def __ne__(self, other):
        return self.ssn != other.ssn


    def getSSN(self):
        return self.ssn

TotalAge = 0.0

def AddAges(item):
    global TotalAge
    TotalAge += int(item.age)

def printSSN(item):
    print(item)

def main():
    global TotalAge
    hasht = hashtable.HashTable(3000000)
    time1 = time.time()
    total_in_errors = 0
    with open("InsertNamesMedium.txt","r") as f, open("DeleteNamesMedium.txt", "r") as delete, open("RetrieveNamesMedium.txt", "r") as retrieve:
        for line in f:
            words = line.split()
            #check if s if a duplicate before adding it to the list
            #print name of the duplicate student
            s = Student(*words)
            #print(s.ssn)
            s2 = hasht.Insert(s)
            if not s2:
                total_in_errors += 1
            
        print(f"Total insert errors: {total_in_errors}")
        print(time.time() - time1, "seconds for insert.")
        
        #first age
        timetraverse = time.time()
        hasht.Traverse(AddAges)
        a = TotalAge / hasht.Size()
        print(f"Average age is: {a}")
        print(time.time()-timetraverse, "seconds to traverse.")

        #delete students
        timedelete = time.time()
        total_del = 0
        for line in delete:
            ssn = line.strip()
            s = Student("","", ssn, "","0")
            s2 = hasht.Delete(s)
            if not s2:
                total_del += 1

        print(f"Total delete errors: {total_del}")
        print(time.time() - timedelete, "seconds for delete.")
        
        #retrieve students
        timeretrieve = time.time()
        age = 0
        count = 0
        total_ret = 0
        for line in retrieve:
            ssn = line.strip()
            s = Student("","", ssn, "","0")
            s2 = hasht.Retrieve(s)
            if not s2:
                total_ret += 1
            else:
                age += int(s2.age)
                count += 1
                
        print(f"Total Retrieve Errors: {total_ret}")
        print("Average age is now:", age/count)
        print(time.time() - timeretrieve, "seconds to retrieve.")
    


if __name__ == '__main__':
    main()
