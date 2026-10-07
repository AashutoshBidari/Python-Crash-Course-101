# a file contains a word "donkey" multiple times. write a program 
# which replaces the word with ###### and updates in the same file

word = "donkey"

with open("files.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "#####")

with open("files.txt", "w") as f:
    f.write(contentNew)
        