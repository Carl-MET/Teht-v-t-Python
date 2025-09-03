vuosi = int(input("Kerro vuosi"))
if vuosi % 400 ==0:
    print("tämä on karkausvuosi")
elif vuosi % 100 != 0:
    print("tämä on karkausvuosi")
else:
    print("tämä ei ole karkausvuosi")