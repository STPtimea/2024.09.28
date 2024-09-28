'''
13. feladat – Kör
A program olvassa be a konzolról egy kör sugarát! Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kör sugara nem pozitív!"; egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!
'''
import math

def tizenharmadik():

    radius = float(input("Add meg a kör sugarát: "))

    # Ellenőrzés, hogy a sugár pozitív-e
    if radius <= 0:
        print("Hiba: a kör sugara nem pozitív!")
    else:
        kerulet = 2 * math.pi * radius
        terulet = math.pi * radius ** 2

        print("A kör kerülete: " + str(round(kerulet, 2)))
        print("A kör területe: " + str(round(terulet, 2)))

