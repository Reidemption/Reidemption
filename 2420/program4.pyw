import time, sys
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
    with open("InsertNames.txt","r") as f:
        for line in f:
            words = line.split()
            #check if s if a duplicate before adding it to the list
            #print name of the duplicate student
            if any(words[2] == s.ssn for s in sList):
                print(f"Error: {words[2]} already registered.")
            else:
                s = Student(*words)
                sList.append(s)

    print(time.time() - time1)


if __name__ == '__main__':
    main()