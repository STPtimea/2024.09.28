'''
1. feladat – Abszolútérték1
A program  olvasson be a konzolról egy valós számot!
A program számítsa ki a szám abszolút értékét, és írja ki az eredményeket a konzolra!
A számításhoz a math.fabs használd!
'''

def paros():
    szam = int(input("Adj meg egy egész számot!: "))

    if szam %2 ==0:
        print("A szám páros")
    else:
        print("A szám páratlan")