#write a program to check whether a given username contains less than 10 characters or not

user = input("Enter username: ")

if(len(user) < 10):
    print("Your username contains less than 10 characters.")
else:
    print("Your username contains more than or equal to 10 characters!")