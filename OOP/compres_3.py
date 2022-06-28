from itertools import groupby


def compress_3(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, len(list(group))))
    result = ["".join((i, "." * j)) for i, j in result]
    return "".join(result)


print(compress_3(121112122))
