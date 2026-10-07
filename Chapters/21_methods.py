# class methods

class Employee:
    age = 19
    # def show(self):
    #     print(f"The age is {self.age}")
    @classmethod # shows class attribute insted of instance attribute during execution 
    def show(clf):
        print(f"The age is {clf.age}")

e = Employee()
e.a = 50
e.show() #output = 50 (instance attribute) without class method


# property decorators

class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Joe Mama"
print(e.fname, e.lname)
print(e.name)

e.show()


# operator overloading in python 

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m) #will give error if there is no __add__ (dunder method)