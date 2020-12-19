#Defining Parent class
class Person:
    #Parent class init method
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print("Person init method called")
        print("firstname:", fname)
        print("lastname:", lname)
    #parent class printname method
    def printname(self):
        print("From Parent class")
        print("firstname:", self, self.fname)
        print("lastname:", self, self.lname)

#Defining Child class
class Student(Person):
    #Child class init method
    def __init__(self, fname, lname, gradyear):
        print("Student init method called")
        Person.__init__(self, fname, lname)
        self.gradyear = gradyear
    #child class printname method
    def printname(self):
        print("From student class")
        print("firstname:", self, self.fname)
        print("lastname:", self, self.lname)
        print("graduation year:", self, self.gradyear)

#creating child class object
x = Student("James","Gupta", 2015)
x.printname()
print("===========================")
#creating parent class object
x = Person("Rahul", "Jain")
x.printname()
