#dictionaries
#list of key values pairs
# it is unordered, mutable, indexed, and it cannot contain duplicate keys

x = {} # enpty dict

marks = {
    "Joe": 10,
    "Bob": 32,
    "Jack": 23
}

print(marks, type(marks))

print(marks["Bob"])

print(len(marks)) #gives length of dict

#dictionary methods


marks = {
    "Joe": 10,
    "Bob": 32,
    "Jack": 23,
    0: "Oggy"
}

print(marks.items())
print(marks.keys())
print("......")
marks.update({"Joe": 49, "Dany": 35})
print(marks)

print(marks.get("Joe"))
print(marks.get("sam"))

# print(marks.get("Joe2")) #gives none if key is not present
# print(marks["Joe2"]) #gives error if key is not present
# Use get() instead of d[key] when you're not sure the key exists.

# more dictionaty methods

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# get()
print(student.get("name"))          # Alice
print(student.get("city", "N/A"))   # N/A

# keys()
print(student.keys())
# dict_keys(['name', 'age', 'grade'])

# values()
print(student.values())
# dict_values(['Alice', 20, 'A'])

# items()
print(student.items())
# dict_items([('name', 'Alice'), ('age', 20), ('grade', 'A')])

# update()
student.update({"age": 21})
print(student)

# pop()
student.pop("grade")
print(student)

# setdefault()
student.setdefault("city", "Boston")
print(student)

# copy()
copy_student = student.copy()

# clear()
copy_student.clear()
print(copy_student)   # {}


#use update() to merge two dictionaries

d1 = {"a": 1}
d2 = {"b": 2}

d1.update(d2)
print(d1)   # {'a': 1, 'b': 2}