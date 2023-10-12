#Lager en variabel for poengsummen til brukeren
poengsum = 0

#Spør brukeren tre spørsmål
oppgave1 = input('hva er hovedstaden i Norge?')

if oppgave1.lower() == 'oslo':  #sjekker om svaret var rett
    print('RIKTIG!')    #Om svaret var riktig legger det til ett poeng til poengsummen
    poengsum += 1
else:
    print('FEIL!')      #Er svaret feil skrives det ut feil i terminalen

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

print('du fikk', poengsum,'/3 poeng')   #printer poengsummen til brukeren