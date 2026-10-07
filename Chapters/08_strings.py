name = "joe" # string

# 'hello' is a string
# "hello" is a string
# '''hello''' is a string
# """hello""" is a string

# strings are immutable. so u cant change letters

multi_line_string= """this
    is a multi line string
                       it can be written in multiple lines
                       intendation is preserved
            
"""

name = "portugal" #[01234567]

namelength = len(name) # length of string
print("length of string is: ", namelength)
# slice string = name[start:end] # start index is inclusive, end index is exclusive

name_slice = name[0:3] # slice from index 0 to 2 i.e 3 is not included
print("sliced string is: ", name_slice)

char1 = name[0] # get character at index 0
print("character at index 0 is: ", char1)

char2 = name[6] # get character at index 6
print("character at index 6 is: ", char2)

char3 = name[-1] # get character at index -1 i.e last character
print("character at index -1 is: ", char3)  

# index starts from 0, so index of first character is 0, second character is 1 and so on
# in backward indexing, index of last character is -1, second last character is -2 and so on

#negative slicing

negative_slice = name[-3:-1] # slice from index -3 to -2 i.e -1 is not included
print("negative sliced string is: ", negative_slice)

#name[-3:-1] = name[5:7] = "ga"

# if name[:3] = name[0:3] = "por"
# if name[3:] = name[3:len(name)] = "tugal"

print(name[-3:-1])
print(name[5:7])


# slicing with skip value

a = "abcdefghijklm"
print(a[0:10:2]) # slice from index 0 to 9 with skip value of 2 i.e every second character will be included in the slice

b = "0123456789"
print(b[1:8:3]) # slice from index 1 to 7 with skip value of 3 i.e every third character will be included in the slice

word = "pythons" #[0123456]
print(word[0:7:2]) # slice from index 0 to 6 with skip value of 2 i.e every second character will be included in the slice
