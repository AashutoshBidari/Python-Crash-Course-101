# write a recursive function to calculate sum of first n natural numbers

def sum(n):
    if(n == 1):
        return 1
    return sum(n-1)+n

n = int(input("Enter a number: "))
print(f"sum upto {n} is: {sum(n)}")