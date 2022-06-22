

def calculate_n(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(calculate_n(10))


def calculate():
    total = 0
    a = 0
    b = 1
    while a < 1000000:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total


print(calculate())
