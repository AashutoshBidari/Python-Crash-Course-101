# loops in python

print("not using loops: ")
print(1)
print(2)
print(3)
print(4)
print(5)

# loops makes it easy and efficient .
# the same output can be done like this

print("using loop: ")

# for loop: 
for i in range(1, 6): # 6 is not included
    print(i)


#while loop: loops the block of code until the condition is met.
i = 1
while(i<6): 
    print(i)
    i += 1 # i = i+1


# list using while loop

print("\n")

l = [ 1, "Jack", "Joe", 2.5, True, "This"]

i = 0

while(i<len(l)):
    print(l[i])
    i += 1


# For loop

for i in range(4): # 0 to 3
    print(i)

for i in range (0, 100, 4): # skips 3 digits and chooses the 4th one
    print(i)

print("\n")

# for loop iterate

#for loop with list
l = [1, 2, 43, 545, 23.2, "Joe", True]
for i in l:
    print(i)

#for loop with tuple
print("\n")

t = {8, 231, 23, 122}
for i in t:
    print(i)

#for loop with string
print("\n")

s = "String" 
for i in s:
    print(i)


#for loop with else
print("\n")
l = [1, 2, 3, 4, 5]
for num in l:
    print(num)
else:
    print("done")

print("\n")
print("\n")

#Breaks in loop

# break is used to exit the loop when encountered

for i in range (1, 10):
    if(i == 5):
        break # exit the loop right now
    print(i)

print("\n")

#Continue in loop

# continue skips the iteration in loop when encountered

for i in range (1, 10):
    if(i == 5):
        continue # skip this iteration
    print(i)

print("\n")

# PASS in python

# pass is null statement. it says to do nothing. it can be used in a loop if you plan to complete that loop later

for i in range(100):
    pass #skips this loop

i = 0
while(i < 10):
    print(i)
    i += 1

