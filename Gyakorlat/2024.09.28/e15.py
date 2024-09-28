'''
15. feladat – Téglalap1
A program olvasson be a konzolról két valós számot!
Ha mindkét szám pozitív, akkor legyenek a beolvasott számok egy téglalap oldalai.
A program számítsa ki a téglalap kerületét, területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra!
Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"!
'''
def tizenotodik():

    a = float(input("Add meg a téglalap egyik oldalát: "))
    b = float(input("Add meg a téglalap másik oldalát: "))

    if a <= 0 or b <= 0:
        print("Hiba: a téglalap oldalai nem pozitívak!")
    else:
        kerulet = 2 * (a + b)
        terulet = a * b

        print("A téglalap kerülete: " + str(round(kerulet, 2)))
        print("A téglalap területe: " + str(round(terulet, 2)))

'''
print(f"A téglalap kerülete: {kerulet:.2f}")
print(f"A téglalap területe: {terulet:.2f}")
'''