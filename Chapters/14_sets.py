#sets
#collection of non repetative elements

x = set() #enpty set
print(type(x))

s = {1, 32, 34, 55, 5, 3, 5, 5, 3, "Joe"} #set
print(s, type(s)) # doesnt print repeating elements
# order is not maintained

s.add(343) #adds into set
print(s, type(s))
print(len(s)) #gives length


#set methods

s = {10, 20, 30, 40}

# add() = adds a single element to the set
s.add(50)
print(s)

# update() = adds multiple elements from another iterable
s.update([60, 70, 80])
print(s)

# remove() = removes an element (gives error if element does not exist)
s.remove(20)
print(s)

# discard() = removes an element (does NOT give error if element does not exist)
s.discard(100)
print(s)

# pop() = removes and returns a random element
removed = s.pop()
print(removed)
print(s)

# clear() = removes all elements from the set
temp = {1, 2, 3}
temp.clear()
print(temp)

# copy() = creates a copy of the set
copy_set = s.copy()
print(copy_set)



# set operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# union() = returns all unique elements from both sets
print(a.union(b))

# intersection() = returns common elements
print(a.intersection(b))

# difference() = returns elements in first set but not in second
print(a.difference(b))

# symmetric_difference() = returns elements that are in either set but not both
print(a.symmetric_difference(b))


#Relationship Methods
a = {1, 2}
b = {1, 2, 3, 4}
c = {5, 6}

# issubset() = checks if all elements of first set are in second set
print(a.issubset(b))

# issuperset() = checks if first set contains all elements of second set
print(b.issuperset(a))

# isdisjoint() = checks if two sets have no common elements
print(a.isdisjoint(c))


# In-place Update Methods
a = {1, 2, 3}
b = {3, 4, 5}

# intersection_update() = keeps only common elements
temp = a.copy()
temp.intersection_update(b)
print(temp)

# difference_update() = removes common elements from first set
temp = a.copy()
temp.difference_update(b)
print(temp)

# symmetric_difference_update() = keeps elements not common in both sets
temp = a.copy()
temp.symmetric_difference_update(b)
print(temp)