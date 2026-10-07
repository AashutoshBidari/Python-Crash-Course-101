# write a program to mine out log file and find if it contains the word python or not
# also find out the line number where the word python is present

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
        
    if ("python" in line):
        print(f"Yes python is present. Line no:{lineno}")
        break
    lineno += 1

else:
    print("No python is not present.")