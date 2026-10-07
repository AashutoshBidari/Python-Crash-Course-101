# conditionals in python

#syntax
# if (condition1):
#     print("Statement1")

# elif (condition2):
#     print("Statement2")

# else:
#     print("statement3")


#code example

age = int(input("enter your age: "))
if(age>=18):
    print("you are above 18 yrs.")
    print("You can vote.")

elif(age<0):
    print("You are entering invalid age.")

elif(age==0):
    print("You are entering 0, so you are a new born.")

else:
    print("you are child.")

print("Thankyou!")