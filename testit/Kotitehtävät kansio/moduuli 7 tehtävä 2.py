nimet=set()
while True:
    nimi = input('anna jokin nimi')
    if nimi=='':
        break
    if nimi in nimet:
        print('aiemmin syötetty')
    if nimi not in nimet:
        nimet.add(nimi)
        print('uusi nimi')
print(nimet)