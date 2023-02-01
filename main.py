import random


nev = input('Adja meg a nevét!')
erosseg = random.randint(5,15)
ugyesseg = random.randint(5,15)
szerencse = random.randint(5,15)
print(F'Üdvözlünk a játékban!{nev}')
print('Az alábbi statokkal rendelkezel:')
print(f'Erősség: {erosseg} Ügyesség: {ugyesseg} Szerencse: {szerencse}')
input("ENTER a folytatáshoz")



