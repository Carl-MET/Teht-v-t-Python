luvut=[]
luku=input('anna jokin luku')
while True:
    if luku=='':
        break
        luvut.append(luku)
    luvut.append(int(luku))
    luku=input('anna jokin luku')
luvut.sort(reverse=True)

print(luvut[0])
print(luvut[1])
print(luvut[2])
print(luvut[3])
print(luvut[4])




