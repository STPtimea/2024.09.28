'''
7. feladat – Négyzetgyök
A program számítsa ki egy beolvasott valós szám négyzetgyökét!
A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!
'''
import math

def hetedik():
    szam = float(input("Adj meg egy valós számot: "))
    if szam < 0:
     print("Hiba: Negatív szám négyzetgyökét nem lehet számítani!")
    else:
     gyok = math.sqrt(szam)
     print("A(z) " + str(szam) + " négyzetgyöke: " + str(gyok))

'''
import math

def hetedik():
    szam = float(input("Adj meg egy valós számot: "))
    
    if szam < 0:
        print("Hiba: Negatív szám négyzetgyökét nem lehet számítani!")
    else:
        gyok = math.sqrt(szam)
        print(f"A(z) {szam} négyzetgyöke: {gyok}")

hetedik()

'''