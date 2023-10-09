
poengsum = 0

oppgave1 = input('hva er hovedstaden i Norge?')

if oppgave1.lower() == 'oslo':
    print('RIKTIG!')
    poengsum += 1
else:
    print('FEIL!')

oppgave2 = input('hva er adressen til akademiet bislett')

if oppgave2.lower() == 'pilestredet 52':
    print('RIKTIG!')
    poengsum += 1
else:
    print('FEIL!')

oppgave3 = float(input('hva er 2+2?'))

if oppgave3 == 4:
    print('RIKTIG!')
    poengsum += 1
else:
    print('FEIL!')

print('du fikk', poengsum,'/3 poeng')