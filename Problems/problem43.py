# write a program to convert inch to cm

def inch(i):
    return i*2.54

i = int(input("Enter value in inches: "))

print(f"The corresponding value in cms is: {inch(i)}")