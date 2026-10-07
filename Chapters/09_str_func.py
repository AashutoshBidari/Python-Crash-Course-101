# string functions

name = "harry"  # string

# Length of string
print(len(name))

# Check if string ends with given text
print(name.endswith("y"))
print(name.endswith("rry"))
print(name.endswith("rrya"))

# Check if string starts with given text
print(name.startswith("h"))
print(name.startswith("ha"))
print(name.startswith("H"))

# Capitalize first letter of string
print(name.capitalize())

# Convert string to uppercase
print(name.upper())

# Convert string to lowercase
print(name.lower())

# Capitalize first letter of every word
print(name.title())

# Swap uppercase letters to lowercase and vice versa
print(name.swapcase())

# Replace one part of string with another
print(name.replace("har", "car"))

# Find the first occurrence of a substring
print(name.find("r"))
print(name.find("z"))

# Find the index of a substring (gives an error if not found)
print(name.index("r"))

# Count how many times a substring appears
print(name.count("r"))

text = "  hello world  "

# Remove spaces from both ends of the string
print(text.strip())

# Remove spaces from the left side of the string
print(text.lstrip())

# Remove spaces from the right side of the string
print(text.rstrip())

sentence = "apple,banana,mango"

# Split a string into a list using a separator
print(sentence.split(","))

fruits = ["apple", "banana", "mango"]

# Join list elements into a single string
print(", ".join(fruits))

# Check if all characters are alphabets
print(name.isalpha())
print("harry123".isalpha())

# Check if all characters are digits
print("12345".isdigit())
print("123a".isdigit())

# Check if all characters are letters or numbers
print("harry123".isalnum())
print("harry 123".isalnum())

# Check if the string contains only whitespace
print("   ".isspace())
print(" a ".isspace())

# Pad the string with leading zeros until it reaches the given length
print("42".zfill(5))

# Center the string within the given width
print(name.center(10, "-"))

# Left-align the string within the given width
print(name.ljust(10, "-"))

# Right-align the string within the given width
print(name.rjust(10, "-"))