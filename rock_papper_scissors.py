import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gamer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

computer = random.randint(0, 2)
print(f"Computer chose {computer}")

if gamer == computer:
    print("It's a draw")
elif ((gamer == 0) and (computer == 2)):
    print(rock)
    print(scissors)
    print("You lose!")
elif gamer == 2 and computer == 0:
    print(scissors)
    print(rock)
    print("You win!")
elif gamer == 0 and computer == 1:
    print(rock)
    print(paper)
    print("You win!")
elif gamer == 1 and computer == 0:
    print(paper)
    print(rock)
    print("You lose!")
elif gamer == 2 and computer == 1:
    print(scissors)
    print(paper)
    print("You win!")
elif gamer == 1 and computer == 2:
    print(paper)
    print(scissors)
    print("You lose!")
elif gamer >= 2 or gamer < 0:
    print("You typed in invalid number, you lose!")


