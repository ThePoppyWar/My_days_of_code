def is_palindrome(number):
    numer_str = str(number)
    if numer_str != numer_str[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]

print(is_palindrome(363))