import random
import json


with open("kaland.json", "r", encoding='utf-8') as f:
    data = json.load(f)






# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(data)

print("Kalandjáték indítása...")

# Játékos neve
nev = input("Adja meg a játékos nevét: ")

erosseg = random.randint(5,15)
ugyesseg = random.randint(5,15)
szerencse =random.randint(5,15)


# Kezdeti helyzet
print("Üdvözöllek, " + nev + "! Te egy kalandozó vagy, aki egy sötét barlangban találja magát.")
print("tovabbhaladsz a 41-re")

# Választás
tov = input("tovabbhaladashoz nyomja meg az 'ENTERT'")


# Player stats
player_hp = 100
player_strength = 10
player_luck = 5

# Boss stats
boss_hp = 150
boss_strength = 20
boss_luck = 10

# Function to calculate damage done
def calculate_damage(attacker_strength, defender_hp):
    damage = attacker_strength - defender_hp // 2
    if damage <= 0:
        damage = 1
    return damage

# Function to check if a lucky event happens
def is_lucky(luck):
    if random.randint(1, 10) <= luck:
        return True
    else:
        return False

# Game loop
while player_hp > 0 and boss_hp > 0:
    # Player's turn
    player_damage = calculate_damage(player_strength, boss_hp)
    if is_lucky(player_luck):
        player_damage *= 2
        print("Szereztél egy szerencsés ütést!")
    boss_hp -= player_damage
    print("Sebeztél:", player_damage, "ennyit sebeztél a Boss-ba Boss HP:", boss_hp)

    # Boss's turn
    boss_damage = calculate_damage(boss_strength, player_hp)
    if is_lucky(boss_luck):
        boss_damage *= 2
        print("A boss szerzett egy szerencsés ütést!")
    player_hp -= boss_damage
    print("Boss sebzett", boss_damage,"-at/ot beléd. Életerőd: :", player_hp)

# Game over
if player_hp <= 0:
    print("Elvesztetted a játékot!")
else:
    print("Megnyerted a küzdelmet a Boss ellen")


ut = input('tovabbhaladsz')
if ut == "j":
    print("Találsz egy aranyat, amit magadhoz vehetsz.")
elif ut == "b":
    print("Egy veszélyes sárkány vár rád, amit legyőzni kell.")
else:
    print("Nem értem, amit mondasz. Vége a játéknak.")
print("haladsz tovább")
ut2 = input("Merre szeretnél menni? (jobbra / balra)")
if ut == "j":
    print("Találsz egy sárkányt, amkivel meg kell kuzdened.")
elif ut == "b":
    print("Egy veszélyes sárkány vár rád, amit legyőzni kell.")





else:
    print("Nem értem, amit mondasz. Vége a játéknak.")




print("Vége a játéknak.")


