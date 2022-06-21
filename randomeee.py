import random

gamer = input("Choise: Heads or Tails ").lower()

computer = random.randint(0, 1)

if computer == 1:
    print("Heads")
else:
    print("Tails")


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

index_names = random.randint(0, (len(names) - 1))
print(f"{names[index_names]} is going to buy the meal today!")

