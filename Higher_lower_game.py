import random

print("Who have more followers on Instagram")

person = {"Timothee Chalamet is an american actor and model": 17000000,
          "Johnny Depp is most popular actor from USA": 26000000,
          "Kim Kardiashian is popular television person from USA": 322000000,
          "Blanka Lipińska is a polish writes": 899000,
          "Cristiano Ronaldo is a Portuguese foodballer": 464000000,
          "Zendaya is an american actor, model and singer": 147000000,
          "Cezary Pazura is a polish actor": 416000,
          "Robert Lewandowski is a pilish footballer": 26000000
          }

first_person = random.choice(list(person))
second_person = random.choice(list(person))



print(f"Compare A: {first_person}")
print(f"Compare B: {second_person}")


user = input("Whi has more followers? Type 'A' or 'B': ")

