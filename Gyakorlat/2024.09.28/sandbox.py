'''
2024.09.28. - Házi feladat ellenőrzése
'''

#5-ös

if szam <= 0 or szam >= 13:
    print("HIBA")
else:
    if szam == 1:
        print("Január")
    elif szam == 2:
        print("Február")
    elif szam == 3:
        print("Március")
    elif szam == 4:
        print("Április")
    elif szam == 5:
        print("Május")
    elif szam == 6:
        print("Június")
    elif szam == 7:
        print("Július")
    elif szam == 8:
        print("Augusztus")
    elif szam == 9:
        print("Szeptember")
    elif szam == 10:
        print("Október")
    elif szam == 11:
        print("November")
    elif szam == 12:
        print("December")

#main: e5.honap()

#6-os feladat (e6.szog()
def szog():

    vSzam = float(input("Kérem adjon meg egy valós számot: "))

    if (vSzam >= 0) and (vSzam <= 360):
        if vSzam == 0:
            print(str(vSzam)+" -> nullszög")
        elif (vSzam>0) and (vSzam<90):
            print(str(vSzam)+" -> hegyesszög")
        elif vSzam == 90:
            print(str(vSzam) + " -> derékszög")
        elif vSzam == 180:
            print(str(vSzam) + " -> egyenesszög")
        elif (vSzam > 180) and (vSzam < 360):
            print(str(vSzam) + " -> homorú szög")
        elif vSzam == 360:
            print(str(vSzam) + " -> teljesszög")
        else:
            print("Nem jó számot adtál meg. Próbáld újra!")


#7-es feladat
# Gyökvonáshoz kell az import math

import math
def negyzetgyok():

    szam = float(input("Adj meg egy számot: "))
    if szam >= 0:
        gyok = math.sqrt(szam)
        print(gyok)
    else:
        print("HIBA! Negatív szám gyökét akarja számolni.")

#13-as feladat
import math
#CÉLZOTT CSOMAGBEKÉRÉS: import pow from math >> Ezzel megttudom mondani melyik csomagot akarom behívni a math-ból

def kor():
    r = float(input("Kérem adjon meg egy kör sugár értékét!"))

    if r>0:
        terület = r ** 2 * math.pi
        #terület2 = r*r * math.pi
        #terület3 = math.pow(r, _y:2) * math.pi
        #terület4 = pow(r,2)* math.pi Ide nem kell csomagot behívni
        kerület = 2 * r * math.pi

        print("A kör területe:" + str(terület) +", a kör kerülete: " + str(kerület) + '.' )

#14-es feladat
def kocka():
    el = int(input("Kérem adjon meg egy él értéket!: "))
    if el <= 0:
        print("HIBA")
    else:
        felszin = 6 * el**2
        terfogat = pow(el,3) #harmadik hatványa
        print("A kocka felszíne: " + str(felszin) + ", térfogata: " + str(terfogat) + ".")

#main-be: e14.kocka()

#15-ös feladat

# FÜGGVÉNY aminek van visszatérési értéke = METÓDUS
def egeszBeolvas():
    szam = float(input("adjon meg egy egész számot: "))
    return szam

def teglalap():

    oldal1 = egeszBeolvas()
    oldal2 = egeszBeolvas()

    if (oldal1 > 0) and (oldal2 > 0):
        kerulet = (oldal1 + oldal2)*2
        terulet = oldal1 * oldal2
        print("A téglalap kerülete: " + str(kerulet) + ", területe: " + str(terulet))
    else:
        print("A téglalap oldalai nem pozitívak!")

#main: e15.teglalap()
