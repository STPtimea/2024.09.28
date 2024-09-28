'''
5. feladat – HónapNév
A program  olvasson be a konzolról egy egész számot! Ha a szám 1 és 12 közötti, akkor legyen a beolvasott szám egy hónap sorszáma!
A program írja ki a konzolra a sorszámmal megadott hónap nevét! Hiba esetén legyen hibaüzenet!
'''

def otodik():
    honap_sorszam = int(input("Adj meg egy egész számot (1-12): "))

    if honap_sorszam == 1:
        print("A hónap neve: Január")
    elif honap_sorszam == 2:
        print("A hónap neve: Február")
    elif honap_sorszam == 3:
        print("A hónap neve: Március")
    elif honap_sorszam == 4:
        print("A hónap neve: Április")
    elif honap_sorszam == 5:
        print("A hónap neve: Május")
    elif honap_sorszam == 6:
        print("A hónap neve: Június")
    elif honap_sorszam == 7:
        print("A hónap neve: Július")
    elif honap_sorszam == 8:
        print("A hónap neve: Augusztus")
    elif honap_sorszam == 9:
        print("A hónap neve: Szeptember")
    elif honap_sorszam == 10:
        print("A hónap neve: Október")
    elif honap_sorszam == 11:
        print("A hónap neve: November")
    elif honap_sorszam == 12:
        print("A hónap neve: December")
    else:
        print("Nem jó számot adtál meg. Próbáld újra!")

