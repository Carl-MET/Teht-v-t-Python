print("valitse mitä toimintoa haluat käyttää\n A on yhteislasku \nB on vähennyslasku"
      " \nC on kertolasku \nD on jakolasku")
valinta = input("valintasi A-D:").upper()

a = float(input("Anna ensimmäinen luku:"))
b = float(input("Anna toinen luku:"))
if valinta == "A":
    print("yhteenlasku",a+b)
elif valinta == "B":
    print("vähennyslasku",a-b)
elif valinta == "C":
    print("kertolasku",a*b)
elif valinta == "D":
    print("jakolasku",a/b)
else:
    print("valintasi on virheellinen")


