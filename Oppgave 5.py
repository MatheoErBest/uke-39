
alder = float(input('hvor mange år er du'))

if alder <=9:
    print('billeten din er gratis')

elif 9 < alder <= 17:
    print('billeten din koster 20kr')

elif 18 <= alder <= 65:
    print('billeten din koster 40kr')

elif alder >= 65:
    print('billeten din koster 20kr')

