#  Write a class "calculator" capable of finding square, cube and square root of a number
# also add a static method to greet the user with hello

class Calculator:

    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square is {self.num*self.num}.")

    def cube(self):
        print(f"The cube is {self.num*self.num*self.num}.")

    def squareroot(self):
        print(f"The square root is {self.num**1/2}.")

    @staticmethod
    def greet():
        print("Hello, Welcome to the calculator.")

a = Calculator(4)
a.greet()
a.square()
a.cube()
a.squareroot()