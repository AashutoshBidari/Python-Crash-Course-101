# walrus operator ( := ) 
# assign values to variable as part of expression

# Using walrus operator 
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") # Output: List is too long (5 elements, expected <= 3)


# type definitions in python

n : int = 5
name: str = "Joe"

def  sum(a: int, b: int) -> int:
    return a+b
print(sum(3,2))

# The syntax of types looks something like this:
from typing import List, Tuple, Dict, Union
#List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
#Tuple of a string and an integer  
person: Tuple[str, int] = ("Alice", 30)
# Dictionary with string keys and integer values  
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Union type for variables that can hold multiple types  
identifier: Union[int, str] = "ID123"
identifier = 12345 # Also valid


# match case

def http_status(status): 
    match status:  
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: 
            return "Unknown status"  


print(http_status(5007))


# dictionary merge

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged)

# with statement

with (
    open('file.txt') as f1,
    open("files.txt") as f2
):
    # processes files
    print("Reading files...")
    print(f1.read())
    print(f2.read())


# exception handling in python

try:
    a = int(input("Enter a number: "))
except Exception as e:
    print(e)

print("Thank you!")


# raising exception
a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")


# try with else
try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e) 

else:
    print("I am inside else") #only execute if try was successful


# try with finally

def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

        
    except Exception as e:
        print(e) 
        return


    finally: # will run everytime even with return
        print("Hey I am inside of finally")


main()


# importing modules

from func import func

# list comprehensions

myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)