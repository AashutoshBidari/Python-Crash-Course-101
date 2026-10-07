# wap in python using functions to convert celcius in fahrenheit

def celcius(c):
    return (9*c/5)+32

c = int(input("Enter temperature in celcius: "))
print("Temperature in fahrenheit is: ", celcius(c))