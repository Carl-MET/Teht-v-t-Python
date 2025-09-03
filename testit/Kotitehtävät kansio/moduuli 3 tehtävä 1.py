kuha = int(input("Anna kuhan koko senttimetreissä"))
if kuha<37:
    print(f"kalasi on {37-kuha}cm verran liian lyhyt. Laske se takaisin!")
elif kuha>100:
    print("vie kaupan puntarille")
else:
    print("kalasi on valtava vonkale, ota kuva someen välittömästi")