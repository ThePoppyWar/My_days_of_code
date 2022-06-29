from itertools import groupby


def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)


print(compress(122235554688))

def decompress_1(compress_numer):
    result = []
    new_result = []
    for number in compress_numer.split("_"):
        result.append(tuple(number))
    for index, number in result:
        new_result.append(index * int(number))
    return int("".join(new_result))

print(decompress_1('15_36_21_33'))


def decompress_2(compress_number):
    result = [tuple(number) for number in compress_number.split('_')]
    result = [i * int(j) for i, j in result]
    return int(''.join(result))

print(decompress_2('15_36_21_33'))

