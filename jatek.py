import random

print("Kalandjáték indítása...")

# Játékos neve
nev = input("Adja meg a játékos nevét: ")
print('Üdvözöljük a játékban!! Sok sikert kíván Sebi és csapata')
erosseg = random.randint(5,15)
ugyesseg = random.randint(5,15)
szerencse =random.randint(5,15)

# Kezdeti helyzet
print("Üdvözöllek, " + nev + "! Te egy kalandozó vagy, aki egy sötét barlangban találja magát.")
print("Előtted 2 út áll: jobbra és balra.")

# Választás
ut = input("Merre szeretnél menni? (jobbra / balra)")

if ut == "j":
    print("Találsz egy aranyat, amit magadhoz vehetsz.")
elif ut == "b":
    print("Egy veszélyes sárkány vár rád, amit legyőzni kell.")
else:
    print("Nem értem, amit mondasz. Vége a játéknak.")

print("Vége a játéknak.")
