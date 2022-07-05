import random
from random import randint



hard_level = 5
easy_level = 10




def compare(guess_number, computer_number, lives):
    if guess_number > computer_number:
        print("Too high.")
        return lives - 1
    elif guess_number < computer_number:
        print("Too low!")
        return lives - 1
    else:
        print(f"You win! The answer was {computer_number}")

def leve_difficulty():
    choose = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choose == 'easy':
        return easy_level
    else:
        return hard_level


def play():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    computer_number = random.randint(1, 100)
    appempts = leve_difficulty()
    guess_number = 0
    while guess_number != computer_number:
        print(f"You have {appempts} attempts remaining to guess the number")

        guess_number = int(input("Make a guess:"))
        appempts = compare(guess_number, computer_number, appempts)
        if appempts == 0:
            print('You lose!')
            return
        elif guess_number != computer_number:
            print("Guess again!")

play()



