print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

check_word = name2 + name1
#TRUE
liter_T = check_word.count("t")
liter_R = check_word.count("r")
liter_U = check_word.count("u")
liter_E = check_word.count("e")

score_true = liter_T + liter_R + liter_U + liter_E
score_true = str(score_true)

#LOVE
liter_L = check_word.count("l")
liter_O = check_word.count("o")
liter_V = check_word.count("v")
liter_E_2 = check_word.count("e")

score_love = liter_L + liter_O + liter_V + liter_E_2
score_love = str(score_love)

result = score_true + score_love
result = int(result)

if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")

