import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password_generator = ""
# for _ in range(1, nr_letters + 1):
#     password_generator += random.choice(letters)
# for _ in range(1, nr_symbols + 1):
#     password_generator += random.choice(symbols)
# for _ in range(1, nr_numbers + 1):
#     password_generator += random.choice(numbers)
# print(password_generator)

password_generator_2 = []

for sing in range(1, nr_letters + 1):
    password_generator_2.append(random.choice(letters))
for _ in range(1, nr_symbols + 1):
    password_generator_2.append(random.choice(symbols))
for _ in range(1, nr_numbers + 1):
    password_generator_2.append(random.choice(numbers))

random.shuffle(password_generator_2)
print(password_generator_2)

password_end = ""
for char in password_generator_2:
    password_end += char
print(f"Your password is: {password_end}")