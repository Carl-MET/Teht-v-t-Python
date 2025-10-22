import math
def muuntaja():
    muunnos=muunnettava*3.785
    return muunnos
muunnettava= float(input('Anna määrä gallonoissa'))
muunnos=muuntaja()
while muunnettava >0:
    muuntaja()
    print(muunnos)
    muunnettava = float(input('Anna määrä gallonoissa'))
