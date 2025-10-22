import random
def noppa(luku):
    heitto=random.randrange(0,luku+1)
    return heitto
luku=int(input('anna noppassa esiintyvä suurin luku'))
heitto=noppa(luku)

while heitto!=luku:
    noppa(luku)
    heitto = noppa(luku)
    print("heitto:",heitto)