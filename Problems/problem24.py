# a spam comment is determined by following keywords:
# "make a lot of money", "buy now", "subscribe this", "click this"
# make a program to detect these spams

p1 = "make a lot of money"
p2 = "buy now"
p3 =  "subscribe this"
p4 =  "click this"

msg = input("Enter your comment: ")

if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("Spam Alert!!!!!!")
else:
    print("not a spam")