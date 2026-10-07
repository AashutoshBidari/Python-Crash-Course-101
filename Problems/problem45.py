# wap using function to print multiplication table of given number


def table(n):
    for i in range(1, 11):
        print(f"{n}x{i}={n*i}")

n = int(input("Enter a number: "))
table(n)