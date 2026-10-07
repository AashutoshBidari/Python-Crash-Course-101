# We are going to write a program that generates a random number and asks the user to guess it.
# If the player's guess is higher than the actual number, the program displays "Lower number please". Similarly, if the user's guess is too low, the program prints "higher number please" When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
# Hint: Use the random module.

import random

number = random.randint(1, 50)
count = 0

player_guess = 0

while (player_guess != number):
    player_guess = int(input("Guess the number from 1 to 50: "))
    count += 1

    if( player_guess > number):
        print("Lower number please!")

    elif( player_guess < number):       
        print("Higher number please!")

    else:        
        print("Correct guess!")

print(f"The number was {number}")
print(f"You took {count} tries.")