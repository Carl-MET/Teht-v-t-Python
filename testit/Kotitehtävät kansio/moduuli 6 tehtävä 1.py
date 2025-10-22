import random
def nopanluku():
    heitto=random.randrange(0,7)
    return heitto
heitto = nopanluku()
while heitto!=6:
    nopanluku()
    heitto = nopanluku()
    print(heitto)