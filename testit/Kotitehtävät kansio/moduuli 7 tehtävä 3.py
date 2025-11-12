lentoasemat= {}
while True:
    kysymys= input('lisää uusi lentoasema syöttämällä A. hae lentoasema syöttämällä B.'
                   'Jos haluat lopettaa syötä C ')
    if kysymys== 'A':
        ICAO= input('anna ICAO-Koodi')
        Lentoasema= input('Anna lentoaseman nimi')
        lentoasemat[ICAO]= Lentoasema