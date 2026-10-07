# create a empty dict. allow 4 friends to enter their favourite food as value and use key as their name. assume the names are different

d = {}

name = input("enter friends name: ")
food = input("enter favourite food: ")
d.update({name:food})

name = input("enter friends name: ")
food = input("enter favourite food: ")
d.update({name:food})

name = input("enter friends name: ")
food = input("enter favourite food: ")
d.update({name:food})

name = input("enter friends name: ")
food = input("enter favourite food: ")
d.update({name:food})

print(d)