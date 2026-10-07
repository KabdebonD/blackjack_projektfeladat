
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
    erteke = random.choice(kartyak)
    szine = random.choice(szinek)
    tejes_kartya = (str(erteke,szine))
    
jatek = (input(f'akarsz jatcani? (+igen minden más nem) '))
if jatek == "+":
    print("a jatek elkezdodott")
    while jatek=="+":
        TET= int(input("Tedd meg a Tétedet: " ))
        while TET > alapzseton:
            print("nincs ellég pénz")
            TET= int(input("Tedd meg a Tétedet: " ))
        PAKLI = []
        ERTEK=0   
        for i in range(2):
            print(Kartya(kartyak,szinek).tejes_kartya)
            ERTEK = ERTEK+Kartya(kartyak,szinek).erteke
            PAKLI.append(Kartya.tejes_kartya)
        if ERTEK == 21:
            print("nyertel")
            break
        else:
            huzolmegfel = (input(f"Szeretnél még húzni fel kártyát?(+igen minden más nem) "))
            if huzolmegfel =="+":
                while huzolmegfel=="+":
                    print(f"{Kartya(kartyak,szinek).tejes_kartya}")
                    ERTEK = ERTEK+Kartya(kartyak,szinek).erteke
                    PAKLI.append(Kartya(kartyak,szinek).tejes_kartya)
                    if ERTEK > 21:
                        print("vesztettél")
                        break
                    elif ERTEK == 21:
                        print("nyertel")
                        break        
                    
        jatek = (input(f'akarsz ujj játékot kezdeni? (+igen minden más nem) '))
