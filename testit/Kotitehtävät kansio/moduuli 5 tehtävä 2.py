luvut=[]
luku=input('anna jokin luku')
while True:
    if luku=='':
        break
    luvut.append(int(luku))
    luku=input('anna jokin luku')
luvut.sort(reverse=True)
for numero in luvut[:5]:
    print(numero)




