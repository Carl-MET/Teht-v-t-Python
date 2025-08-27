Pituus =int(input("Pituus: "))
Paino = float(input("Paino: "))

bmi = Paino / (Pituus / 100) **2
print("Pituus-paino-indeksisi on", bmi)
print(f"Pituus-paino-indeksisi on, {bmi:10.2f}")

