


def wisielec(word: str):

    word = word.upper()
    long_word = len(word)
    display = []
    for _ in range(long_word):
        display.append("_")

    game_over = False

    if "_" not in display:
        game_over = True
        print("You win!")

    while not game_over:
        litera = input("Podaj literę: ").upper()
        for index in range(long_word):
            letter = word[index]
            if letter == litera:
                display[index] = letter
        return display

print(wisielec("Kawa"))