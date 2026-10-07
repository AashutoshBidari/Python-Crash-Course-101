# get input from user use input

a = input("Enter number1: ") # the input is always a string, so if you want to use it as a number, you need to convert it to int or float
b = input("Enter number2: ")

print("Number1: ", a)
print("Number2: ", b)

print(a+b) #this will concatenate the two numbers as strings
# this works as: "1"+"2" = "12"
# "hello" + "world" = "helloworld"

print("................")

a = int(input("Enter number1: ")) # takes input as integer
b = int(input("Enter number2: "))
print("sum = ", a+b)