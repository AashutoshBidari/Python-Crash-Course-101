# calculate factorial of a given number using for loop

n = int(input("Enter a number: "))
fact = 1
for i in range (1, n+1):
    fact *= i
print("The factorial is: ", fact)