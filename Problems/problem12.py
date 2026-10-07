# write a program to detect double space in a string

x = "joe is a  very good  boy."

print(x.find("  "))

print(x.replace("  ", " ").capitalize()) # replace double space with single one and capitalizes