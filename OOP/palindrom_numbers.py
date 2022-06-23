
def palindrome_number():
    numbers = []
    for i in range(100, 1000):
        if str(i) == str(i)[::-1]:
            numbers.append(i)
    return len(numbers)


print(palindrome_number())
