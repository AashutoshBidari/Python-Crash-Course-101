# print multiplication table of given number using loop


n = int(input("Enter a number: "))

print("Using FOR loop: ")
for i in range(1, 11):
    # print(n, " * ",i, "=", n*i)
    print(f"{n} X {i} = {n*i}")

print("Using WHILE loop: ")
i = 1
while i<11:
    print(f"{n} X {i} = {n*i}")
    i += 1
