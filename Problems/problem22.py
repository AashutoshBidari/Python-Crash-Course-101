#find the greatest of 4 numbers entered by the user

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
num4 = int(input("enter forth number: "))

greatest = num1

if(num2 > greatest):
    greatest = num2
if(num3 > greatest):
    greatest = num3
if(num4 > greatest):
    greatest = num4

print("\nThe greatest number is:",greatest)

# another method
print("\n -another method- \n")

if(num1>num2 and num1>num3 and num1>num4):
    print("greatest number is: ", num1)
elif(num2>num1 and num2>num3 and num2>num4):
    print("greatest number is: ", num2)
elif(num3>num1 and num3>num2 and num3>num4):
    print("greatest number is: ", num3)
else:
    print("greatest number is: ", num4)
