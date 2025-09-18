käyttäjätunnus='python'
salasana = 'rules'
kirjautumistiedot =käyttäjätunnus+salasana
yritykset=[]
max_yritykset=5
while len(yritykset)<max_yritykset:
    käyttäjätunnus=input('kirjoita käyttäjätunnus')
    salasana=input('kirjoita salasana')
    if kirjautumistiedot==käyttäjätunnus+salasana:
        print('tervetuloa')
        break
    else:
        yritykset.append(kirjautumistiedot)
        print('Pääsy evätty')














