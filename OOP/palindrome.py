def is_palindrome(number):
    numer_str = str(number)
    if numer_str != numer_str[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]


print(is_palindrome(99))


def palindrome_three_numbers():
    numbers = list()
    for i in range(100, 1000):
        if is_palindrome(i) == True:
            numbers.append(i)
    return numbers


print(palindrome_three_numbers())


# or

def find_three_palindrome():
    return [i for i in range(100, 1000) if is_palindrome(i)]


print(find_three_palindrome())
