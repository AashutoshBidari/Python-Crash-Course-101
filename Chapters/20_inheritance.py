class Employee: #base class
    company = "Apple"
    name = "Name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
    
# class Programmer:
#     company = "Apple AI"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#using inheritance

class Programmer(Employee): #derived class
     company = "Apple AI"

a = Employee()
b = Programmer()
a.show()
b.show()
print(a.company, b.company)


#multi-level inheritance

class a:
    pass

class b(a):
    pass

class c(b):
    pass



# Super() Method

class Employee: 

    def __init__(self):
        print("Constructor of employee.")

    a = 1
   
class Programmer(Employee): 

    def __init__(self):
        print("Constructor of programmer.")

    b = 2

class Manager(Programmer):

    def __init__(self):
        super().__init__()
        print("Constructor of manager.")

    c = 3


o = Employee()
print(o.a)

p = Programmer()
print(p.b)

m = Manager()
print(m.c)