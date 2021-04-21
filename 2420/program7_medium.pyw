#check program 5 for outline
#in class questions: How to use error messages when 
import time, bst

class Student:
    def __init__(self, lname, fname, ssn, mail, age):
        self.lname = lname
        self.fname = fname
        self.ssn = ssn
        self.mail = mail
        self.age = age
    
    def __eq__(self, other):
        #print("is overloading")
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
    tree = bst.BinarySearchTree()
    time1 = time.time()
    total_insert_errors = 0
    with open("InsertNamesMedium.txt","r") as f, open("DeleteNamesMedium.txt", "r") as delete, open("RetrieveNamesMedium.txt", "r") as retrieve:
        for line in f:
            words = line.split()
            #check if s if a duplicate before adding it to the list
            #print name of the duplicate student
            s = Student(*words)
            #print(s.ssn)
            s2 = tree.Insert(s)
            if not s2:
                total_insert_errors += 1
        print(f"{total_insert_errors} total insertion errors.")    
        print(time.time() - time1, "seconds for insert.")
        
        #first age
        timetraverse = time.time()
        tree.Traverse(AddAges)
        a = TotalAge / tree.Size()
        print(f"Average age is: {a}")
        print(time.time()-timetraverse, "seconds to traverse.")

        #delete students
        timedelete = time.time()
        total_delete_errors = 0
        for line in delete:
            ssn = line.strip()
            s = Student("","", ssn, "","0")
            s2 = tree.Delete(s)
            if s2 is False:
                total_delete_errors += 1
                
        print(f"{total_delete_errors} total delete errors.")
        print(time.time() - timedelete, "seconds for delete.")
        
        #retrieve students
        total_retrieve_errors = 0
        timeretrieve = time.time()
        age = 0
        count = 0
        for line in retrieve:
            ssn = line.strip()
            s = Student("","", ssn, "","0")
            s2 = tree.Retrieve(s)
            if s2 is None:
                total_retrieve_errors += 1
            else:
                age += int(s2.age)
                count += 1
        print(f"{total_retrieve_errors} total retrieve errors.")
        print("Average age is now:", age/count)
        print(time.time() - timeretrieve, "seconds to retrieve.")
    


if __name__ == '__main__':
    main()