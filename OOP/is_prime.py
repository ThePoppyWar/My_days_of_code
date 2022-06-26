def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n ==2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def is_prime_2(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(11))
print(is_prime(6))