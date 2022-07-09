import random

print("Who have more followers on Instagram")

person = [{"test": "Timothee Chalamet is an american actor and model",
           "follower": 17000000},
          {"test": "Johnny Depp is most popular actor from USA",
           "follower": 26000000},
          {"test": "Kim Kardiashian is popular television person from USA",
           "follower": 322000000},
          {"test": "Blanka Lipińska is a polish writes",
           "follower": 899000},
          {"test": "Cristiano Ronaldo is a Portuguese foodballer",
           "follower": 464000000},
          {"test": "Zendaya is an american actor, model and singer",
           "follower": 147000000},
          {"test": "Cezary Pazura is a polish actor",
           "follower": 416000},
          {"test": "Robert Lewandowski is a pilish footballer",
           "follower": 26000000},
          ]

def get_random_star():
    return random.choice(person)

def format_data(person):
    tekst = person["test"]
    followers = person["follower"]
    return f"{tekst}"


def check_answer(user, first_person, second_person):
    if first_person > second_person:
        return user == "A"
    else:
        return user == "B"


def game():
    score = 0
    game_continue = True
    person_a = get_random_star()
    person_b = get_random_star()

    while person_a == person_b:
        person_b = get_random_star()
    print(f"Compare A: {person_a['test']}")
    print("vs")
    print(f"Against B: {person_b['test']}")

    user = input("Who has more followers? Type 'A' or 'B': ").upper()
    first_person_follower = person_a["follower"]
    second_person_follower = person_b["follower"]
    is_correct = check_answer(user, first_person_follower, second_person_follower)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")



game()




