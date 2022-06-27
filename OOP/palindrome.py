def is_palindrome(number):
    numer_str = str(number)
    if numer_str == numer_str[::-1]:
        return True
    else:
        return False

print(is_palindrome(363))