# write a program to generate multiplication table from 2 to 20 and write it to different files.
# place these files in a folder for your kid to read

def generatetable(n):

    table = ""

    for i in range(1, 11):
        table += f"{n}x{i}={n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generatetable(i)