def prina_n(n):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k += 1
    return czynniki


print(prina_n(48))


# or

def calculate(number):
    i = 2
    factors = []
    while i * i <= number:
        if not number % i == 0:
            i += 1
        else:
            number = number // i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors


print(calculate(56))


def calculate_2(number):
    all_factors = []
    i = 2
    while number != 1:
       while number % i == 0:
           number //= i
           all_factors.append(i)
       i += 1
    return max(all_factors)

print(calculate_2(13195))

# or
def calculate_3(number):
    i = 2
    factors = []
    while i * i <= number:
        if not number % i == 0:
            i += 1
        else:
            number = number // i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return max(factors)