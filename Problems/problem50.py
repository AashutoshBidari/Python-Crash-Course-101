# write a program that censors a list of word from a file

words = ["donkey", "bad", "rubbish"]

with open("document.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("document.txt", "w") as f:
    f.write(content)
        