from itertools import groupby


def compress(number):
    list_tupla = list()
    for key, group in groupby(str(number)):
        list_tupla.append((key, len(list(group))))
    return list_tupla


print(compress(12355549855566))
print(compress(111111))
print(compress(1555697777811255))
