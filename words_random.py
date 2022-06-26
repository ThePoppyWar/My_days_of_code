word_list = ["aardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")

# display_letter = []
# sum_letter = 0
# for letter in chosen_word:
#     sum_letter += 1
# display_letter.append("_" * sum_letter)
# print(display_letter)

# index_letter = 0
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
