import re   #importere re bibloteket

hovedstader = ['oslo', 'copenhagen', 'goteborg']    #lager en liste med hovedstadene i skandinavia

brukerHovedstad = input('skriv en hovedstad i skandinavia') #ber brukeren skrive en hovedstad fra skandinavia


for item in hovedstader:    #sjekker om en av hovedstadene fra listen er svaret du ga
    if isinstance(item, str) and re.search(brukerHovedstad.lower(), item):
        print(brukerHovedstad + ' er en hovedstad i skandinavia, RIKTIG!')
        break

    else:   #om svaret ditt er ikke er i listen får du melding om det
        print(brukerHovedstad + ' er ikke en hovedstad i skandinavia, FEIL!')
        break

    

