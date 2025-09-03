sukupuoli = input("kerro sukupuolesi muodossa mies / nainen").lower()
hemoglobiini = int(input("kerro hemoglobiini arvosi g/l"))
if sukupuoli == "nainen" and hemoglobiini<117:
    print("hemoglobiini arvosi on alhainen")
elif sukupuoli == "nainen" and hemoglobiini>175:
    print(f"hemoglobiini arvosi on korkea")
elif sukupuoli == "nainen" and 117<hemoglobiini<175:
    print(f"hemoglobiinisi on normaali")
elif sukupuoli == "mies" and hemoglobiini<134:
    print(f"hemoglobiini arvosi on alhainen")
elif sukupuoli == "mies" and hemoglobiini>195:
    print(f"hemoglobiini arvosi on korkea")
elif sukupuoli == "mies" and 134<hemoglobiini<195:
    print(f"hemoglobiini arvosi on normaali")
else:
    print("tarkista että syötteesi on oikeassa muodossa")


