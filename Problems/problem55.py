# Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, address):

        self.name = name
        self.salary = salary
        self.address = address

p = Programmer("Jack", 10000, "somewheree")
print(p.name, p.salary, p.address, p.company)

q = Programmer("Joe", 99999, "Something")
print(q.name, q.salary, q.address)