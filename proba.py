jatek = int(input('akarsz jatcani? (+igen minden más nem) '))
if jatek == "+":
    print("a jatek elkezdodott")
    while jatek=="+":
        TET= int(input("Tedd meg a Tétedet: " ))
        while TET > alapzseton:
            print("nincs ellég pén")
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