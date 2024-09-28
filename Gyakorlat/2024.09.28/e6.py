'''
6. feladat – Szögtípus
A program  kérjen be a konzolról egy valós számot! Ha ez a szám 0 és 360 közé esik, akkor legyen egy szög mértéke (pl. 60 fok), egyébként a program adjon hibaüzenetet!
Ha lehet, a program írja ki a szög mértéke alapján a szög típusát (pl.: 60 -> hegyesszög)!
'''
def hatodik():
    szog = float(input("Adj meg egy valós számot (0-360): "))

    if 0 <= szog <= 360:
        if szog == 0 or szog == 360:
            print("A szög mértéke: 0 fok (nulla szög)")
        elif szog < 90:
            print(f"A szög mértéke: {szog} fok - hegyesszög")
        elif szog == 90:
            print(f"A szög mértéke: {szog} fok - derékszög")
        elif szog < 180:
            print(f"A szög mértéke: {szog} fok - tompaszög")
        elif szog == 180:
            print(f"A szög mértéke: {szog} fok - egyenes szög")
        else:
            print(f"A szög mértéke: {szog} fok - homorú szög")
    else:
        print("Nem jó számot adtál meg. Próbáld újra!")

"""
def szogtipus():
    szog = float(input("Adj meg egy valós számot (0-360): "))

    if 0 <= szog <= 360:
        if szog == 0 or szog == 360:
            print("A szög mértéke: " + str(szog) + " fok (nulla szög)")
        elif szog < 90:
            print("A szög mértéke: " + str(szog) + " fok - hegyesszög")
        elif szog == 90:
            print("A szög mértéke: " + str(szog) + " fok - derékszög")
        elif szog < 180:
            print("A szög mértéke: " + str(szog) + " fok - tompaszög")
        elif szog == 180:
            print("A szög mértéke: " + str(szog) + " fok - egyenes szög")
        else:
            print("A szög mértéke: " + str(szog) + " fok - homorú szög")
    else:
        print("Nem jó számot adtál meg. Próbáld újra!")

"""
