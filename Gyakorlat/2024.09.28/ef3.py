'''
A program  olvasson be a konzolról egy valós számot!
A program számítsa ki a szám abszolút értékét, és írja ki az eredményeket a konzolra!
A számításhoz a math.fabs() függvény helyett elágazást használjon!
'''
def abszolut():
    szam = float(input("Adj meg egy egész számot!: "))

    if szam > 0:
        eredmeny = szam
        print("|" + str(szam) + "|=" + str(eredmeny))
    else:
        eredmeny = szam *(-1)
        print("|" + str(szam) + "|=" + str(eredmeny))

 # be: 0 ki: |0| = 0.0 működés:
 # be: 6 ki: |6| = 6.0 működés:
 # be: -6 ki: |-6| = 6.0 működés:

 # HÁZI : 5-6-7  11 haladóknak
