'''
14. feladat – Kocka
A program olvasson be a konzolról egy egész számot! Ha a szám pozitív, akkor legyen a beolvasott szám egy kocka élének hossza.
A program számítsa ki és írja ki a kocka felszínét, térfogatát a konzolra!
Ha a szám nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kocka élének hossza nem pozitív!"!
'''
def tizennegyedik():
    el_hossz = int(input("Add meg a kocka élének hosszát: "))

    if el_hossz <= 0:
        print("Hiba: a kocka élének hossza nem pozitív!")
    else:
        felszin = 6 * (el_hossz ** 2)
        terfogat = el_hossz ** 3

        print("A kocka felszíne: " + str(felszin))
        print("A kocka térfogata: " + str(terfogat))
