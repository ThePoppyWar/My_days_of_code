import sys


print(sys.version.split()[0])

def calculate20():
    numbers = []
    for i in range(0, 20):
        if i % 5 == 0 or i % 7 == 0:
            numbers.append(i)
    return sum(numbers)


print(calculate20())

def calculate():
    return sum([i for i in range(100) if i % 5 == 0 or i % 7 == 0])

print(calculate())
