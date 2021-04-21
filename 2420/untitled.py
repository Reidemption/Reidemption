import time
class Student:
    def __init__(self, lname, fname, ssn, mail, age):
        self.lname = lname
        self.fname = fname
        self.ssn = ssn
        self.mail = mail
        self.age = age

    def getSSN(self):
        return self.ssn

def main():
    sList = []
    time1 = time.time()
    with open("InsertNames.txt","r") as f, open("DeleteNames.txt", "r") as delete, open("RetrieveNames.txt", "r") as retrieve:
        for line in f:
            words = line.split()
            #check if s if a duplicate before adding it to the list
            #print name of the duplicate student
            if any(words[2] == s.ssn for s in sList):
                print(f"Error: {words[2]} already registered.")
            else:
                s = Student(*words)
                sList.append(s)
        print(time.time() - time1, "seconds for insert.")
        
        #first age
        timetraverse = time.time()
        a = 0.0
        for s in sList:
            t = int(s.age)
            a += t
        a = a/len(sList)
        print(f"Average age is: {a}")
        print(time.time()-timetraverse, "seconds to traverse.")
        #delete students
        timedelete = time.time()
        for line in delete:
            words = line.strip()
            
            DeleteNotFound = True
            for s in sList:
                if words == s.ssn:
                    sList.remove(s)
                    DeleteNotFound = False
            if DeleteNotFound:
                print(f"Error: {words} not registered")

        print(time.time() - timedelete, "seconds for delete.")
        
        #retrieve students
        timeretrieve = time.time()
        ra = 0.0
        lengthcounter = 0
        for line in retrieve:
            words = line.strip()
            RetrieveNotFound = True
            for s in sList:
                if words == s.ssn:
                    ra += int(s.age)
                    lengthcounter += 1
                    RetrieveNotFound = False
            if RetrieveNotFound:
                print(f"Error: {words} never registered")
        print("Average age is now:", ra/lengthcounter)
        print(time.time() - timeretrieve, "seconds to retrieve.")
    


if __name__ == '__main__':
    main()