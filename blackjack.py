#--FŐ ADATOK--
import random
bubi=10
dama=10
kiraly=10
asz = 10
kartyak = [2,3,4,5,6,7,8,9,10,bubi,dama,kiraly,asz]
szinek = ["♥","♦","♦","♣"]
alapzseton = 100

#--SZÁMOLÁSOK--

def Kartya(kartyak,szinek):
    erteke = random.randint(kartyak)
    szine = random.randint(szinek)
    tejes_kartya = erteke+szine
    return erteke,szine,tejes_kartya

#--A FŐ JÁTÉK--
while jatek != "-":
    jatek = int(input("Új játékba kezdel? ('ENTER' a kezdéshez, '-' a kilépéshez! )"))
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
        elsosajatkartya = (random.randint(Kartya[tejes_kartya]))
        masodiksajtkartya = (random.randint(Kartya[tejes_kartya]))
        elsoellenfelkartya = (random.randint(Kartya[tejes_kartya]))
        masodikellenfelkartya = (random.randint(Kartya[tejes_kartya]))

        

    else:
        
            
            #print(f"{Kartya.tejes_kartya}")
            #sajatertek = Kartya.erteke + sajatertek
            #print(f"Kártyád jelenlegi értéke: {sajatertek}")

jatek = int(input('akarsz jatcani? (+igen minden más nem) '))
if jatek == "+":
    print("a jatek elkezdodott")
    while jatek=="+":
        TET= int(input("Tedd meg a Tétedet: " ))
        while TET > alapzseton:
            print("nincs el"ég pén)
            TET= int(input("Tedd meg a Tétedet: " ))
        PAKLI = []
        ERTEK=0   
        for i in range(2):
            print(f"{Kartya.tejes_kartya}")
            ERTEK = ERTEK+Kartya.erteke
            PAKLI.append(Kartya.tejes_kartya)
        if ERTEK == 21:
            print("nyertel")
            break
        else:
            huzolmegfel = int(input("Szeretnél még húzni fel kártyát?(+igen minden más nem) "))
            if huzolmegfel =="+":
                while huzolmegfel=="+":
                    print(f"{Kartya.tejes_kartya}")
                    ERTEK = ERTEK+Kartya.erteke
                    PAKLI.append(Kartya.tejes_kartya)
                    if ERTEK > 21:
                        print("vesztettél")
                        break
                    elif ERTEK == 21:
                        print("nyertel")
                        break        
                    
        jatek = int(input('akarsz ujj játékot kezdeni? (+igen minden más nem) '))