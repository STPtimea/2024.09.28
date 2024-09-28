'''
4.	Osztályzat2: A program beolvas a konzolról egy egész számot!
Ha a szám 1 és 5 közötti, akkor legyen a beolvasott szám egy osztályzat!
A program írja ki a konzolra a számmal megadott osztályzatot szövegesen (1=elégtelen, …, 5=jeles)!
Ha a szám nem 1 és 5 közötti, akkor a program írja ki konzolra, hogy „érvénytelen osztályzat”!
'''

def negyedik():

    szam = int(input("Adj meg egy egész számot!: "))

    if (szam >= 1) and (szam <= 5):
        if szam ==1:
            print("1 = elégtelen")
        elif szam == 2:
            print("2 = elégséges")
        elif szam == 3:
         print("3 = közepes")
        elif szam == 4:
         print("4 = jó")
        elif szam == 5:
         print("5 = jeles")
    else:
        print("Érvénytelen osztályzat!")
