# write a program to read text from a given file "poems.txt" and find out whether it contains word twinkle

with open("poems.txt") as f:
    content = f.read()
    if("twinkle" in content):
        print("The word twinkle is present.")
    else:
        print("The word twinkle is not present.")

