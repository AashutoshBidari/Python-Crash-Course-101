#  Create a class with a class attribute a; create an object from it and set 'a'
# directly using object.ao. Does this change the class attribute? =>no cuz class attribute doesnt change

class demo:
    a = 4

o = demo()
print(o.a) # prints class attribute cuz instance attribute is not present
o.a = 5
print(o.a) # prints instance attribute cuz instance attribute is present

print(demo.a) #prints class attribute