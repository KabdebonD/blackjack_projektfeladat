#--FŐ ADATOK--
import random
bubi=10
dama=10
kiraly=10
asz = 10
kartyak = [2,3,4,5,6,7,8,9,10,bubi,dama,kiraly,asz]
szinek = ["♥","♠","♦","♣"]
alapzseton = 100
sajat_pakli=[]
sajat_pakli_szine=[]
oszto_pakli=[]
oszto_pakli_szine=[]
#--SZÁMOLÁSOK--

def kiir(sajat_pakli_szine,sajat_pakli):
    for i in range(6):
        if i ==1:
            print(f"|{sajat_pakli[a]}   |")
        elif i ==4:
            print(f"|   {sajat_pakli[a]}|")
        elif i==3:
            print(f"|  {sajat_pakli_szine[a]}  |") 
        elif i==0 or i==5:
            print("+-----+")
        
        
#print(kiir(sajat_pakli_szine,sajat_pakli))
   
jatek = (input(f'akarsz jatcani? (+igen minden más nem) '))
if jatek == "+":
    print("a jatek elkezdodott")
    while jatek=="+":
        TET= int(input("Tedd meg a Tétedet: " ))
        while TET > alapzseton:
            print("nincs ellég pénz")
            TET= int(input("Tedd meg a Tétedet: " ))
        
        ERTEK=0   
        for a in range(2):
            sajat_pakli.append(random.choice(kartyak))
            sajat_pakli_szine.append(random.choice(szinek))
            print(kiir(sajat_pakli_szine,sajat_pakli),end=" ")
            ERTEK = ERTEK+sajat_pakli[a]
            print(f"Kártyáid értéke: {ERTEK}")
            
        print(sajat_pakli,sajat_pakli_szine)
        if ERTEK == 21:
            print("nyertel")
            break
        else:
            huzolmegfel = (input(f"Szeretnél még húzni fel kártyát?(+igen minden más nem) "))
            if huzolmegfel =="+":
                a=2
                while huzolmegfel=="+":
                    
                    sajat_pakli.append(random.choice(kartyak))
                    sajat_pakli_szine.append(random.choice(szinek))
                    print(kiir(sajat_pakli_szine,sajat_pakli))
                    ERTEK = ERTEK+sajat_pakli[a]
                    a+=1
                    if ERTEK > 21:
                        print("vesztettél")
                        break
                    elif ERTEK == 21:
                        print("nyertel")
                        break        
                    huzolmegfel = (input(f"Szeretnél még húzni fel kártyát?(+igen minden más nem) "))
            #osztóó
            
        jatek = (input(f'akarsz ujj játékot kezdeni? (+igen minden más nem) '))
