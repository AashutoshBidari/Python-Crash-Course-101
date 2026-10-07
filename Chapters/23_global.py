# a as a local variable

a = 69

def fun():
    a = 3
    print(a)

fun()
print(a)

# using global

b = 69

def funs():
    global b
    b = 3
    print(b)

funs()
print(b)