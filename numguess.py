import random

def numguess():
    print("Welcome to the Guessing Game!")
    guess = int(input("Guess a number between 1 and 9 inclusive "))
    chances = 5
    num = random.randint(1,9)

    while chances > 1:
        if guess != num:
            chances -= 1
            print("Try again!")
            guess = int(input("Guess a number between 1 and 9 inclusive"))
        elif guess == num:
            print("Wonderful! You did it")
            chances = 0
    if not(chances > 1) and guess != num:
        print("Try the game again!")

numguess()
            

