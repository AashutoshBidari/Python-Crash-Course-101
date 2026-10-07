#escape sequence is a combination of characters that represents a special character in a string.
#  It is used to represent characters that are not easily typed or displayed, such as newlines, tabs, and quotes.

a = "hello\nworld" # \n is a newline character
print(a)

b = "1st line\n2nd line\n3rd line" # \n is a newline character
print(b)    

c = "\"hello\""
print(c) # \" is a double quote character

#mostly used escape sequences

# \n  = gives new line
# \t  = gives horizontal tab
# \\  = prints a backslash (\)
# \'  = prints a single quote (')
# \"  = prints a double quote (")



#not mostly used escape sequences

# \r  = carriage return (moves cursor to the beginning of the line)
# \b  = backspace (removes one character)
# \f  = form feed (page break)
# \v  = vertical tab
# \a  = alert/bell sound
# \0  = null character
# \ooo = character with octal value (e.g. \101 = A)
# \xhh = character with hexadecimal value (e.g. \x41 = A)
# \N{name} = Unicode character by name (e.g. \N{BLACK HEART SUIT})
# \uhhhh = Unicode character (16-bit) (e.g. \u2764 = ❤)
# \Uhhhhhhhh = Unicode character (32-bit) (e.g. \U0001F600 = 😀)