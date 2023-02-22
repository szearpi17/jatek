import random
import json

with open ("kaland.json", "r", )as f:
    data = json.load(f)

cards1 = data['cards']

print("cards1")
for cards in cards1:
    print(f"{cards1['szöveg']}, {cards1['ugrás']}")

# Játékos neve
nev = input("Adja meg a játékos nevét: ")
print('Üdvözöljük a játékban!! Sok sikert kíván Sebi és csapata')
erosseg = random.randint(5,15)
ugyesseg = random.randint(5,15)
szerencse =random.randint(5,15)

# Kezdeti helyzet
print("Üdvözöllek, " + nev + "! Te egy kalandozó vagy, aki egy sötét barlangban találja magát.")
print("Előtted most egy út áll, lapozz a 41-re")




# Választás
ut = input(" Győztél? (igen / nem)")

if ut == "i":
    print("Lépj a 85-re kártyára")
elif ut == "n":
    print("Vége a játéknak!")
else:
    print("Vége a játéknak!")

ut = input("A Tolvajnál 3 Aranytallért és gyümölcsöt találtál.  Merre szeretnél menni? (Északra / Nyugatra)")

if ut == "é":
    print("Lépj a 108-as kártyára")
elif ut == "ny":
    print("Lépj a 147-es mezőre")



print("Vége a játéknak.")