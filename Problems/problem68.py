# Write a list comprehension to print a list which contains the multiplication table of a user entered number.
# and store the table in a file "Tables.txt"

n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]

with open("Tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)}" + "\n")