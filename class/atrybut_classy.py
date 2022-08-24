class Phone:
    os = 'android';
    year = 2022;
    color = 'red';

    def describe_class():
        print(f'Operating system: {Phone.os}')
        print(f'{Phone.__name__} class.')


# print(getattr(Phone, 'color'))


# for attr in sorted(Phone.__dict__.keys()):
#     if not attr.startswith('_'):
#         print(f'{attr} -> {getattr(Phone, attr)}')


# print(setattr(Phone, 'color', 'blue'))


# Phone.orginal_country = 'USA'
# print(Phone.__dict__)

# setattr(Phone, 'year_of_production', 2000)
# print(Phone.__dict__)
print('----------------------------------------------------------------')

Phone.describe_class()
print('----------------------------------------------------------------')
getattr(Phone, 'describe_class')()
print('------------------------Phone 1------------------------------')

class Phone1:

    brand = "Apple"

    def __init__(self, brand):
        self.brand = brand


    def print_brand(self):
        print(f"{Phone1.brand} klasa")
        print(f'Instancja {self.brand}')

phone1 = Phone1('Samsung')
phone1.print_brand()

print('------------------------Phone 2------------------------------')

brand2 = "HP"

class Phone2:

    brand = "Apple"
    result1 = [brand] * 5
    result2 = [brand for brand in range(5)]


print(Phone2.__dict__)