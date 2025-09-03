hytti = input("Kerro hyttiluokkasi").lower()
if hytti == "LUX".lower():
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti == "A".lower():
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B".lower():
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C".lower():
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")