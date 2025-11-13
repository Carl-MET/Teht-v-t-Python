vuodenajat = {    12: 'talvi',1: 'talvi',2: 'talvi',3: 'kevät',4: 'kevät',
                  5: 'kevät',6: 'kesä',7: 'kesä',8: 'kesä',9: 'syksy',10: 'syksy',11: 'syksy'}

vuodenaika =int(input('Minkä kuukauden vuodenajan haluat tarkastaa? anna kuukauden numero muodossa '
                      'esim tammikuu= 1'))

if 1<=vuodenaika<=12:
    print(f'kuukautesi {vuodenaika} on {vuodenajat[vuodenaika]}kuukausi')
else:
    print('numerosi ei vastaa kuukautta')
