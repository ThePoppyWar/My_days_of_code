


def wisielec(word: str):

    word = word.upper()
    long_word = len(word)
    display = []
    for _ in range(long_word):
        display.append("_")

    for index in range(long_word):
        letter = word[index]
        if letter == litera:
            display[index] = letter
    return display



litera = input("Podaj literę: ").upper()
print(wisielec("Kawa"))