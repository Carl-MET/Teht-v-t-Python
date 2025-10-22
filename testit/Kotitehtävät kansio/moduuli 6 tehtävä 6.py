import math
def pizzalaskuri(halkaisija,hinta):
    hintam2=((halkaisija/2)**2*3.14159)/hinta
    return hintam2

vertaus=[]

halkaisija=float(input('anna ensinmäisen pizzan halkaisija senttimetreissä'))
hinta=float(input('anna ensinmäisen pizzan hinta euroissa'))
hintam2=pizzalaskuri(halkaisija,hinta)
vertaus.append((hintam2,'pizza1'))

halkaisija=float(input('anna toisen pizzan halkaisija senttimetreissä'))
hinta=float(input('anna toisen pizzan hinta euroissa'))
hintam2=pizzalaskuri(halkaisija,hinta)
vertaus.append((hintam2,'pizza2'))
print(max(vertaus))

