import random

name = input("Hello! What's your name? ")
number = random.randint(1, 40)
print("Okaaay! The number I'm guessing is between 1 and 40")
print("you have only 6 guesses to answer.")
numofguesses = 6
while(numofguesses > 0):
    print("Guess the number..")

    try:
        guess = int(input())
        if guess < number:
            print("Number is too low")
        elif guess > number:
            print("Number is too high")
        elif guess == number:
            break
    except:
        print("Ugh! You have to enter a number!")
    numofguesses -= 1
    print("You have", numofguesses, "guesses left")

if number == guess:
    print("Yay! You guessed the number in", numofguesses, "guesses")
elif number != guess:
    print("Oops! Unlucky,the number was", number)
