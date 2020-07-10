import random as rnd


def guessing_game():

    number = rnd.randint(0, 100)

    while True:
        guess = int(input("Guess a number: "))

        if guess == number:
            print("Just right!")
            break

        if guess > number:
            print("Too high!")

        if guess < number:
            print("Too low!")


guessing_game()
