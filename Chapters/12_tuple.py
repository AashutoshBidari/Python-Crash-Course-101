# tuple
#tuples are immutable data types
# tuple is just like list but list is mutable and tuple is immutable

a = (1, 2, 3, 4, 5)
print(type(a)) # <class 'tuple'>

a = () #empty tuple
print(type(a))

a = (1) #integer
print(type(a))
b = (1,) #tuple
print(type(b))

a = (5, 55.55, False, "Joe", "Jack")
print(a)
print(type(a)) #tuple


#Tuple Methods

a = (5, 55.55, False, "Joe", "Jack", 5, "Barn")

no = a.count(5) # finds how many times the value occurs in the tuple
print(no)
print(a.count(5)) #directly can be done like this
 
x = a.count(23)
print(x)


# tuple operations

t = (7, 53, 2, 65, 23, 8, 43, 1)

print(len(t))  # get the number of elements in the tuple

print(max(t))  # get the largest element

print(min(t))  # get the smallest element

print(sum(t))  # get the sum of all elements

print(sorted(t))  # return a sorted list from the tuple

print(tuple(reversed(t)))  # reverse the tuple

print(23 in t)  # check if an element exists in the tuple

print(100 not in t)  # check if an element does not exist in the tuple



# unpacking of tuple

t = (10, 20, 30)
a, b, c = t  # unpack the tuple into variables
print(a)
print(b)
print(c)


person = ("Harry", 18, "Nepal")
name, age, country = person  # unpack tuple values into variables
print(name)
print(age)
print(country)


numbers = (1, 2, 3, 4, 5)
a, *b = numbers  # first value goes to a, remaining values go to b
print(a)
print(b)


numbers = (1, 2, 3, 4, 5)
*a, b = numbers  # last value goes to b, remaining values go to a
print(a)
print(b)


numbers = (1, 2, 3, 4, 5)
a, *b, c = numbers  # first value to a, last value to c, remaining values to b
print(a)
print(b)
print(c)


# t = (1, 2, 3)

# a, b = t  # Error: too many values to unpack