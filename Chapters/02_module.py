#module is a file containing python code which can be imported and used in other python files

# using module named pyjokes to print a random joke
# install pyjokes using pip install pyjokes
import pyjokes
print("Printing a random joke:")
joke = pyjokes.get_joke()
print(joke)


# using module named cowsay to print a cow saying hello world
#install cowsay using pip install cowsay
import cowsay
cowsay.cow('Hello World')
cowsay.dragon('Hello World')
