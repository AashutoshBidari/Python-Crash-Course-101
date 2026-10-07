# functions in python

# WITHOUT using function
# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
# avg = (a+b+c)/3
# print(average)

# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
# avg = (a+b+c)/3
# print(average)

# it will be many lines if needed to do for many times so use functions

# Using functions

def avg(): #defining function
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b+ c)/3
    print(average)


avg() # calling the function
# avg() 
# avg() 
# avg() 
# avg() 


#functions with argument

def goodday(name):
    print("Good Day, "+name)

goodday("Joe")
goodday("Jack")

def gd(name, ending):
    print("Good Day, "+name)
    print(ending)

gd("Joe", "Thank You!")
gd("Jack", "Thank You!")


# return value

def good(name, ending):
    print("Good Day, "+name)
    print(ending)
    return "done"

a = good("Joe", "thanks")
print(a)


# default parameter value

def goodDay(name, ending = "Thankyou!"):
    print(f"Good Day, {name}, {ending}")

goodDay("Joe")
goodDay("Jack", "Thanks!")


# recursion
# function which calls itself

def fact(n):
    if(n==1 or n==0):
        return 1
    
    return n*fact(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {fact(n)}")


