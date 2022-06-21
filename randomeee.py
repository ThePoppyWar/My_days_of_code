import random


gamer = input("Choise: Heads or Tails ").lower()

computer = random.randint(0, 1)

if computer == 1:
    print("Heads")
else:
    print("Tails")
