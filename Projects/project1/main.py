'''
logic => 1 = snake, -1 = water and 0 = gun
'''



import random

computer = random.choice([-1, 1, 0])

youstr = input("Enter your choice (s/w/g): ")

youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}

you = youDict[youstr]

print(f"You choose {reverseDict[you]}. \nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw.")
else:
    if(computer == -1 and you == 1):
        print("You won!")
    elif(computer == -1 and you == 0):
        print('You lose!')
    elif(computer == 1 and you == -1):
        print('You lose!')
    elif(computer == 1 and you == 0):
        print('You won!')
    elif(computer == 0 and you == -1):
        print('You won!')
    elif(computer == 0 and you == 1):
        print('You lose!')
    else:
        print("Error!")