jakajat=[2,3,4,5,6,7,8,9]
luku=int(input('anna jokin luku'))

if luku<2:
    print('luku ei ole alkuluku')
else:
    if any(luku% l ==0 for l in jakajat if l< luku):
        print('luku ei ole alkuluku')
    else:
        print('on alkuluku')










