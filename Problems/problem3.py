# use os module to print the contents of a directory
import os

# contents = os.listdir()

# print("Contents of the current directory:")
# for item in contents:
#     print(item)


# specefy the directory
path = '/Python projects'

# list the files in the specified directory
contents = os.listdir(path)

#print file in directory
print(f"Contents of {path}:")
for item in contents:
    print(item)