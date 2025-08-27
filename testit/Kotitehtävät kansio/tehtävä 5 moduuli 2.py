# yksi luoti on 13,3 grammaa yksi naula on 13,3g*32=425,6g Leiviskä 20*425,6=8512g
luoti = float(input("anna luoti"))
naula = float(input("anna naula"))
leiviska = float(input("anna leiviskat"))
paino = (13.3*luoti)+(425.6*naula)+(8512*leiviska)
kilot = float(paino//1000)
grammat = float(paino % 1000)
print(f"massa nykymittoilla: {kilot} kg {grammat:.1f}g")


