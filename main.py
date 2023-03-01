import random

import json

nev = input("Adja meg a játékos nevét: ")
print('Üdvözöljük a játékban!! Sok sikert kíván Sebi és csapata')
erosseg = random.randint(5,15)
ugyesseg = random.randint(5,15)
szerencse =random.randint(5,15)

# Kezdeti helyzet
print("Üdvözöllek, " + nev + "! Te egy kalandozó vagy, aki egy sötét barlangban találja magát.")
print("Előtted most egy út áll, lapozz a 41-re")

print("Üdvözöllek a Kalandjátékban! A célod, hogy átkelj a sötét erdőn.")

# az elérhető irányok
lepesek = ["balra", "jobbra"]

# a játékos kezdőpozíciója
pozicio = 0

# a véletlenszerűen generált akadályok
akadalyok = [random.randint(1, 10) for _ in range(5)]

# a játék fő ciklusa
while True:
    print("Jelenleg a(z) " + str(pozicio) + ". pozícióban vagy.")

    # ellenőrizzük, hogy elértük-e a célvonalat
    if pozicio == len(akadalyok):
        print("Gratulálok, átjutottál az erdőn!")
        break

    # megjelenítjük az aktuális akadályt
    print("Ez egy " + str(akadalyok[pozicio]) + " méter magas akadály.")

    # kérjük a játékos választását
    valasztas = input("Merre szeretnél menni? (balra/jobbra) ")

    # ellenőrizzük, hogy a játékos érvényes lépést tett-e
    if valasztas not in lepesek:
        print("Hibás választás! Csak balra vagy jobbra léphetsz.")
        continue

    # végrehajtjuk a játékos lépését
    if valasztas == "balra":
        pozicio -= 1
    elif valasztas == "jobbra":
        pozicio += 1

    # ellenőrizzük, hogy a játékos át tud-e menni az akadályon
    if pozicio < len(akadalyok) and akadalyok[pozicio] > 5:
        print("Sajnos nem tudtál átmenni az akadályon!")
        break


print("Vége a játéknak.")