import re

hovedstader = ['oslo', 'copenhagen', 'goteborg']

brukerHovedstad = input('skriv en hovedstad i skandinavia')

if brukerHovedstad.lower() == hovedstader:
    print('riktig')

for item in hovedstader:
    if isinstance(item, str) and re.search(brukerHovedstad.lower(), item):
        print(brukerHovedstad + ' er en hovedstad i skandinavia, RIKTIG!')
        break

    else:
        print(brukerHovedstad + ' er ikke en hovedstad i skandinavia, FEIL!')
        break

    

