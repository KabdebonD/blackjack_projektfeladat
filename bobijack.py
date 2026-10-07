#--FŐ ADATOK--
import random
Bubi = 10
Dáma = 10
Király = 10
Ász = 10
Kartyak = [2,3,4,5,6,7,8,9,10,Bubi,Dáma,Király,Ász]
Szinek = ["♥","♦","♦","♣"]
alapzseton = 100

#--SZÁMOLÁSOK--

def Kartya(Kartyak,Szinek):
    erteke = random.choice(Kartyak)
    szine = random.choice(Szinek)
    tejes_kartya = erteke+szine
    return tejes_kartya

#--A FŐ JÁTÉK--
jatek = input("Új játékba kezdel? ('ENTER' a kezdéshez, '-' a kilépéshez! ) ")
while jatek != "-":
    if jatek == "-":
        print(f"VÉGSŐ ZSETONOD: {alapzseton}")
        break
    elif jatek != "" and jatek != "-":
        print("Te kis rafkós, hogy nem az entert nyomtad, de így is elindul a játék!")
        print(f"Jelenlegi zsetonjaid: {alapzseton}")
        tet = int(input("Tedd meg a Tétedet: "))
        megmaradtzseton = alapzseton - tet
        alapzseton = megmaradtzseton
        while alapzseton < 0:
            print("Túl nagy tétet tettél, kisebb téttel játszhatsz csak!")
            tet = int(input("Tedd meg a Tétedet: "))
            megmaradtzseton = alapzseton - tet
            alapzseton = megmaradtzseton

        sajatertek = 0
        osztoertek = 0

        #Kártyák kiválasztása
        elsosajatkartya = Kartya(tejes_kartya)
        masodiksajtkartya = (random.choice(Kartya[tejes_kartya]))
        elsoosztokartya = (random.choice(Kartya[tejes_kartya]))
        masodikosztokartya = (random.choice(Kartya[tejes_kartya]))

        #Saját összegzés
        print(f"Jelenlegi kártyáid -> {elsosajatkartya}, {masodiksajatkartya}")
        sajatertek = elsosajatkartya[erteke] + masodiksajatkartya[erteke]
        print(f"Lapjaid értéke: {sajatertek}")

        #Ellenfél összegzés
        print(f"Az osztó kártyái -> {elsoosztokartya} és ?")

        #Saját rész
        if alapzseton >= tet:
            akcio = input("Mit csinálsz? (DOUBLE/HIT/STAND - nagy betűvel írd be, pls) ")

            if akcio == "DOUBLE":
                tet = tet*2
            elif akcio == "HIT":
                harmadiksajatkartya = random.choice(Kartya[tejes_kartya])