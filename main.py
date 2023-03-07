import json
import random
from classes.jatekosunk import Jatekos


def dobokocka():
    return random.randint(1, 6)


def duplakockadobas():
    return random.randint(1, 6) + random.randint(1, 6)


def szerencseproba():
    if Jatekos.Elixir:
        if duplakockadobas()+1 <= Jatekos.Luck:
            Jatekos.minuszluck(1)
            print("Szerencséd volt!")
            return True
        else:
            Jatekos.minuszluck(1)
            print("Nem akadt szerencséd!")
            return False
    else:
        if duplakockadobas() <= Jatekos.Luck:
            Jatekos.minuszluck(1)
            print("Szerencséd volt!")
            return True
        else:
            Jatekos.minuszluck(1)
            print("Nem akadt szerencséd!")
            return False


def igv():
    print("Igen vagy Nem?")
    while True:
        inp = input()
        if inp == "Igen":
            return True
        elif inp == "Nem":
            return False
        else:
            print("Hibás bemenet")


def harc(csatamod, nev, hp, skill):
    while True:
        EllensegAttackSTR = duplakockadobas() + skill
        JatekosAttackSTR = duplakockadobas() + Jatekos.Skill
        if Jatekos.combatblessed:
            JatekosAttackSTR = JatekosAttackSTR + 1
        if csatamod > 0:
            JatekosAttackSTR = JatekosAttackSTR - csatamod

        if EllensegAttackSTR < JatekosAttackSTR:
            hp = hp - 2
            print("Megsebezted az ellenfelet!")
            if Jatekos.HP < 1:
                print("A játéknak vége van!")
                Jatekos.gameover()
                return False
            elif hp < 1:
                print("Nyertél!")
                return True
            print("Szeretnél szerencsét próbálni?")
            if not igv():
                print("Nem probáltál szerencsét!")
            else:
                if szerencseproba():
                    print("Súlyos sebzést ejtettél!")
                    hp = hp - 2
                else:
                    print("Nem okoztál nagy sebzést!")
                    hp = hp + 1
        elif EllensegAttackSTR > JatekosAttackSTR:
            Jatekos.jatekosSebzes(2)
            print("Az ellenfél megsebzett téged!")
            if Jatekos.HP < 1:
                print("A játéknak vége van!")
                Jatekos.gameover()
                return False
            elif hp < 1:
                print("Nyertél!")
                return True
            print("Szeretnél szerencsét próbálni?")
            if not igv():
                print("Nem probáltál szerencsét!")
            else:
                if not szerencseproba():
                    print("Erős sebzést kaptál!")
                    Jatekos.jatekosSebzes(2)
                else:
                    print("Nem okoztál nagy sebzést!")
                    Jatekos.jatekosHeal(1)
        else:
            print("Kivédtétek egymás ütését!")
        print(f"{nev} Életereje: {hp}")
        print(f"A játékos életereje: {Jatekos.HP} \n")



Nyert = False
probaltemar = False
pickupk = False
csatamod = 0
input("Az új játék inditásához nyomja meg az [ENTER]-t: ")

Jatekos = Jatekos(duplakockadobas() + 12, dobokocka() + 6, dobokocka() + 6, 20)

with open("Kaland.json", "r", encoding="utf-8") as jsn:
    advDict = json.load(jsn)

while not Nyert:
    LepettEMar = False
    Jatekos.lokaciostr()
    print(advDict['kaland'][Jatekos.lokacio]['szoveg'] + "\n")

    if "eleterovesztes" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.jatekosSebzes(advDict['kaland'][Jatekos.lokacio]['ertek'])

    if "hplossrng" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.jatekosSebzes(dobokocka())

    if "szerencsevesztes" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.minuszluck(advDict['kaland'][Jatekos.lokacio]['ertek'])

    if "Eleteronyeres" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.jatekosHeal(advDict['kaland'][Jatekos.lokacio]['ertek'])

    if "szerencsenyeres" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszluck(advDict['kaland'][Jatekos.lokacio]['ertek'])

    if "luckblessing" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.JatekosBlessing()

    if "combatblessing" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.JatekosCombatBlessing()

    if "kezdetiszerencsenoveles" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.kezdetiszerencsenoveles(advDict['kaland'][Jatekos.lokacio]['ertek'])

    if "szerencse+hpminusz" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.minuszluck(advDict['kaland'][Jatekos.lokacio]['ertek'][0])
        Jatekos.jatekosSebzes(advDict['kaland'][Jatekos.lokacio]['ertek'][1])

    if "elixir" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.SzerencseElixirf()

    if "tortenetkezdes" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.tortenetkezdes()

    # tárgy felvételek
    if "pluszlebeges" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszitem("Lebegés Köpenye")

    if "pluszgyuru" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszitem("Ügyesség Gyürüje")

    if "pluszarany" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszitem("Aranykulcs")

    if "+penz" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszpenz(int(advDict['kaland'][Jatekos.lokacio]['mennyiseg'][0]))

    if "+kristaly" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszcrystal(advDict['kaland'][Jatekos.lokacio]['targy'])
    # harc
    if "csatamod" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        csatamod = int(advDict['kaland'][Jatekos.lokacio]['ertek'][0])

    if "onharc" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        if advDict['kaland'][Jatekos.lokacio]['ellenfelek'] == 1:
            harc(csatamod, "te", Jatekos.HP, Jatekos.Skill)
            csatamod = 0

    if "harc" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        if advDict['kaland'][Jatekos.lokacio]['ellenfelek'] == 1:
            harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel']['nev'],
                 advDict['kaland'][Jatekos.lokacio]['ellenfel']['HP'],
                 advDict['kaland'][Jatekos.lokacio]['ellenfel']['ugyesseg'])
            csatamod = 0
        elif advDict['kaland'][Jatekos.lokacio]['ellenfelek'] == 2:
            if harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel']['nev'],
                    advDict['kaland'][Jatekos.lokacio]['ellenfel']['HP'],
                    advDict['kaland'][Jatekos.lokacio]['ellenfel']['ugyesseg']):
                csatamod = 0
                harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel2']['nev'],
                     advDict['kaland'][Jatekos.lokacio]['ellenfel2']['HP'],
                     advDict['kaland'][Jatekos.lokacio]['ellenfel2']['ugyesseg'])
        elif advDict['kaland'][Jatekos.lokacio]['ellenfelek'] == 3:
            if harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel']['nev'],
                    advDict['kaland'][Jatekos.lokacio]['ellenfel']['HP'],
                    advDict['kaland'][Jatekos.lokacio]['ellenfel']['ugyesseg']):
                csatamod = 0
                if harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel2']['nev'],
                        advDict['kaland'][Jatekos.lokacio]['ellenfel2']['HP'],
                        advDict['kaland'][Jatekos.lokacio]['ellenfel2']['ugyesseg']):
                    harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel3']['nev'],
                         advDict['kaland'][Jatekos.lokacio]['ellenfel3']['HP'],
                         advDict['kaland'][Jatekos.lokacio]['ellenfel3']['ugyesseg'])
    if Jatekos.halott:
        break


    if advDict['kaland'][Jatekos.lokacio]['akcio'] == "gyozelem":
        Nyert = True
        break
    elif advDict['kaland'][Jatekos.lokacio]['akcio'] == "gameover":
        Nyert = False
        Jatekos.gameover()
        break



    if "roll" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        while True:
            if dobokocka()>4:
                LepettEMar = True
                break
            else:
                Jatekos.jatekosSebzes(2)
    if "kisebbnagyonbb" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        if duplakockadobas() > Jatekos.Skill:
            Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['ugras'][0])
            LepettEMar = True
        else:
            Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['ugras'][1])
            LepettEMar = True
    if "szerencseproba" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        if szerencseproba():
            Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['HaVan'])
            LepettEMar = True
    if not probaltemar:
        if "gyuruproba" in advDict['kaland'][Jatekos.lokacio]['akcio']:
            print("Szeretnéd felprobálni a gyűrűt?")
            if igv():
                Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['haszeretne'])
                LepettEMar = True
                probaltemar = True
    if not pickupk:
        if "kopeny" in advDict['kaland'][Jatekos.lokacio]['akcio']:
            print("Szeretnéd felprobálni a köpenyt?")
            if igv():
                Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['haszeretnekopenyt'])
                LepettEMar = True
                pickupk = True
    if "targy" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        if (advDict['kaland'][Jatekos.lokacio]['TargyInfo']['szukseges']) in Jatekos.Items:
            Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['TargyInfo']['HaVan'])
            LepettEMar = True
    if not LepettEMar:
        if len(advDict['kaland'][Jatekos.lokacio]['ugras']) == 1:
            StartInp = input("Folytatáshoz nyomja meg az [ENTER]-t (statok, kilépés): ")
            if StartInp == "statok":
                print(Jatekos)
                print("")
            elif StartInp == "kilépés":
                exit()
            Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['ugras'][0])
        elif len(advDict['kaland'][Jatekos.lokacio]['ugras']) > 1:
            print("Irja be merre szeretne haladni? (Adja meg a számot) [statok, kilépés]?")
            while True:
                inp = input()
                if not inp == "":
                    if inp in str(advDict['kaland'][Jatekos.lokacio]['ugras']):
                        Jatekos.lokaciovaltoztatas(inp)
                        break
                    elif inp == "statok":
                        print(Jatekos)
                        print("")
                    elif inp == "kilépés":
                        exit()
                    else:
                        print("hibás input")
                else:
                    print("hibás input")

if not Nyert:
    print("Vesztettél!")
elif Nyert:
    print("Gratulálunk megnyerted a játékot!")

#
