


def wisielec(sentenc: str):

    sentenc = sentenc.split()
    sentenc_liter = ["_"] * len(sentenc)
    zgadywanie = input("Podaj literę: ").upper()

    if zgadywanie in sentenc:
        litera = []
        for i in range(len(sentenc)):
            if sentenc[i] == zgadywanie:
                litera.append(i)

        for index in litera:
            zgadywanie[index] = sentenc[index]

        return zgadywanie
    else:
        print("Incorrect")

print(wisielec("Kawa"))