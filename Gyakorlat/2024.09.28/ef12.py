'''
A program két beolvasott számot összehasonlítva írja közéjük a megfelelő relációs jelet (<, >, =)!
'''
def kisebbnagyobb():
    szam1 = float(input("Adj meg egy egész számot: "))
    szam2 = float(input("Adj meg egy egész számot: "))
    if szam1 == szam2:
        print(str(szam1)+"=" +str(szam2))
    elif szam1 < szam2:
        print(str(szam1)+"<" +str(szam2))
    else:
        print(str(szam1) + ">" + str(szam2))