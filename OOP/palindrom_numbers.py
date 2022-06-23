
def palindrome_number():
    numbers = []
    for i in range(100, 1000):
        if str(i) == str(i)[::-1]:
            numbers.append(i)
    return len(numbers)


print(palindrome_number())


def palindrome_bigger_number():
    numbers = []
    for i in range(10, 100):
        for j in range(10, 100):
            if str(i * j) == str(i * j)[::-1]:
                numbers.append(i * j)
    return max(numbers)


print(palindrome_bigger_number())