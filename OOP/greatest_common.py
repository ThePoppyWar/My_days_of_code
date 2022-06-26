def greatest_common_divisor(first_number, second_number):
    all_divisor = []
    for n in range(1, first_number + 1):
        if first_number % n == 0 and second_number % n == 0:
            all_divisor.append(n)
    return max(all_divisor)


print(greatest_common_divisor(32, 48))

# or

def greatest_common_divisor_2(a, b):
    while b:
        a, b = b, a % b
    return a

print(greatest_common_divisor_2(32, 48))
