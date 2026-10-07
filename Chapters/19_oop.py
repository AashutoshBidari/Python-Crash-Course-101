# Object Oriented Programming

# class = blueprint for object

class Employee:
    language = "Python" #class attribute
    salary = 9999 #class attribute

joe = Employee()
joe.name = "Joe" #instance attribute
print(joe.name, joe.salary, joe.language)

jack = Employee()
jack.name = "Jack"
print(jack.name, jack.salary, jack.language)

# instance attribute takes preference over class attribute

bob = Employee()
bob.name = "bob"
bob.language = "Java" #instance attribute
print(bob.name, bob.salary, bob.language)

# name is instance(object) attribute and salary and language is class attribute as they directly belong to class


# SELF PARAMETER
# Anything can be written in place of self like slf, name etc but using self is a good practice

class Employee:
    language = "Python" 
    salary = 9999 

    def getInfo(self):#self parameter = needs object
        print(f"The language is {self.language} and salary is {self.salary}")

Oggy = Employee()
Oggy.getInfo() # ==>Employee.getinfo(Oggy)


# Static Method

class Employee:
    language = "Python" 
    salary = 9999 

    def getInfo(self): 
        print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet(): #static method = doesnt need object 
        print("Good Morning!")

Oggy = Employee()
Oggy.greet()


# __init__() Constructor

class Employee:
    language = "Python" 
    salary = 9999 

    def __init__(self, name, language, salary): #dunder method which is automatically called
        self.name = name
        self.language = language
        self. salary = salary
        print("Creating an object...")

    def getInfo(self): 
        print(f"The language is {self.language} and salary is {self.salary}")


dany = Employee("Dany", "Java", "1234")
print(dany.name, dany.salary, dany.language)