luvut =[]
luku = (input('anna luku'))
while luku!='':
    luku1= int(luku)
    luvut.append(luku1)
    print(f'kirjoitit luvun{luku}')
    luku =(input(f'anna luku{luku}: '))
print(luvut)
if luvut:
    pienin = min(luvut)
    suurin = max(luvut)
    print(f'pienin {pienin}' )
    print(f'suurin {suurin}' )







