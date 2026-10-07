# write a program to know if a post is talking about "Joe" or not

post = input("Enter the post: ")

if("joe" in post.lower()): # .lower is used so that if upper case Joe is in post then it will detect it too.
    print("this post is talking about joe.")
else:
    print("this post is not talking about joe.")