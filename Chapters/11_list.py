#lists
#store values of any data types

friends = ["Apple", "Banana", 5, 7.53, "Bob", "Jack"]
print(friends[0])

friends[0] = "Grapes" # lists are mutable
print(friends[0])

print(friends[1:4]) # slicing of list


#list methods
# list is mutable so when you use list methods the original list changes unlike string which donot change

friends.append("Joe")
print(friends)

l1 = [7, 53, 2, 65, 23, 8, 43, 1]
l1.sort() #sorts the list
print(l1)

l1 = [7, 53, 2, 65, 23, 8, 43, 1]
l1.reverse() #reverses the list
print(l1)

l1 = [7, 53, 2, 65, 23, 8, 43, 1]
l1.insert(3, 324) # inserts 324 in list l1 such that its index is 3
print(l1)

l1 = [7, 53, 2, 65, 23, 8, 43, 1]
l1.pop(3) # removes item at index 3
print(l1)

# use print(l1.pop(3)) to get the item which is at index 3
l1 = [7, 53, 2, 65, 23, 8, 43, 1]
print(l1.pop(3))

l1 = [7, 53, 2, 65, 23, 8, 43, 1]
l1.remove(2) # removes 2 from the list
print(l1)

l1 = [7, 53, 2, 65, 23, 8, 43, 1]
l2 = l1.copy() # copies a list in new variables
print(l2)

# print(dir(list)) to see all list methods