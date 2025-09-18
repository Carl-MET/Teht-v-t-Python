import random
Arvaa_luku = random.randint(1,10)
arvaus = int(input('arvaa luku 1-10 välillä'))
while arvaus != Arvaa_luku:
    if arvaus < Arvaa_luku:
        print('Liian pieni arvaus')
        arvaus = int(input('arvaa luku 1-10 välillä'))
    if arvaus > Arvaa_luku:
        arvaus = int(input('arvaa luku 1-10 välillä'))
        print('Liian suuri arvaus')
print('Arvasit oikein!')