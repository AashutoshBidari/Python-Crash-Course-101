# to save in disk

# opening file.txt and accessing its data

f = open("file.txt")
data = f.read()
print(data)
f.close() # will work without closing but closing is good habit


# writing in a file
 
st = "This is awesome"

a = open("newfile.txt", "w")
a.write(st)

#lines

b = open("file.txt")
lines = b.readlines()
print(lines, type(lines))

b.close()

c = open("file.txt")
line1 = c.readline()
print(line1, type(line1))
line2 = c.readline()
print(line2, type(line2))
line3 = c.readline()
print(line3, type(line3))
line4 = c.readline()
print(line4, type(line4)) # empty string

c.close()

#in a loop

d = open("file.txt")
l = d.readline()
while(l != ""):
    print(l)
    l = d.readline()
d.close()


# appending in a file

st = "This is awesome"

a = open("newfile.txt", "a")
a.write(st)


# modes for opening file
# r = open for read (by default)
# w = open for write
# a = open for appending
# + = open for updating
# rb = open for read in binary
# rt = open for read in text



# With statement

f = open("file.txt")
print(f.read())
f.close()
#The same can be done using with statement:
with open("file.txt") as f:
    print(f.read())
# no need to close the file

