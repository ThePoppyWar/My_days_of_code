class Phone:
    os = 'android';
    year = 2022;
    color = 'red';


# print(getattr(Phone, 'color'))


# for attr in sorted(Phone.__dict__.keys()):
#     if not attr.startswith('_'):
#         print(f'{attr} -> {getattr(Phone, attr)}')


print(setattr(Phone, 'color', 'blue'))

print(Phone.__dict__)
