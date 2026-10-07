a = 1
t = type(a) #<class 'int'>
print(t)

b = "2"
t = type(b) #<class 'str'>
print(t)

c = 2.5
t = type(c) #<class 'float'>
print(t)

d = "Hello"
t = type(d) #<class 'str'>
print(t)


# variable conversion

a = 1
b = str(a) #convert int to str
print(b)
c = float(a) #convert int to float
print(c)

x = "2.5"
y = float(x) #convert str to float
z = int(y) #convert float to int
print(y)
print(z)
t = type(z) #<class 'int'>
print(t)

x = "5"
y = int(x) #convert str to int
print(y)
t = type(y) #<class 'int'>
print(t)