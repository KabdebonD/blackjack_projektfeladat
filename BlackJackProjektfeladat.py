#--FŐ ADATOK--
import random
bubi=10
dama=10
kiraly=10
asz = 10
kartyak = [2,3,4,5,6,7,8,9,10,bubi,dama,kiraly,asz]
kiiros_kartyak = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A']
szinek = ["♥","♠","♦","♣"]
alapzseton = 100
sajat_pakli=[]
oszto_pakli=[]
#--SZÁMOLÁSOK--
class Kartya():
    def __init__(self,erteke,szine):
        self.erteke=erteke
        self.szine=szine
    def kiir(self):
        print("+-----+")
        print("|",end="")
        print(self.erteke,end="")
        if self.erteke !=10:
            for c in range(4):
                print(" ",end="")
        else:
            for c in range(3):
                print(" ",end="")
        print("|")
        print(f"|  {self.szine}  |") 
        print("|",end="")
        if self.erteke!=10:
            for c in range(4):    
                print(" ",end="")
        else:
            for c in range(3):
                print(" ",end="")
        print(f"{self.erteke}|")
        print("+-----+")
def rand(kartyak):
    return random.randrange(len(kartyak))


jatek = (input(f'akarsz jatcani? (+igen minden más nem) '))
if jatek == "+":
    print("a jatek elkezdodott")
    sajat_pakli
    while jatek=="+":
        sajat_pakli=[]
        oszto_pakli=[]
        print(f"enyi zsetonod van: {alapzseton}")
        TET= int(input("Tedd meg a téted: "))
        while TET > alapzseton:
            print("nincs ellég pénz")
            TET= int(input("Tedd meg a Tétedet: " ))
        megmaradtzseton=alapzseton-TET
        ERTEK=0  
        OSZTOERTEK=0 
        for i in range(2):
            kartya = Kartya(kartyak[rand(kartyak)],random.choice(szinek))
            sajat_pakli.append(kartya)
            kartya.kiir()
        for k in sajat_pakli:
            ERTEK = ERTEK+k.erteke
        print(f"Kártyáid értéke: {ERTEK}")
          
      
        if ERTEK == 21:
            megmaradtzseton+=(TET*2)
            print(f"nyertel, nyereményed: {TET*2}")
            
            break
        #osztóó
        print("Az osztó kártyái: ")       
        kartya1 = Kartya(kartyak[rand(kartyak)],random.choice(szinek))
        kartya2 = Kartya(kartyak[rand(kartyak)],random.choice(szinek))
        oszto_pakli.append(kartya1)
        oszto_pakli.append(kartya2)
        kartya1.kiir()
        print(f"+-----+\n|\   /|\n|  X  |\n|/   \|\n+-----+")
        for k in oszto_pakli:
            OSZTOERTEK = OSZTOERTEK+k.erteke
        bekert=input('Válassz HIT vagy DOUBLE: ')
        if bekert == 'HIT':
                
                while bekert=="HIT" or bekert=="hit":
                    
                    kartya = Kartya(kartyak[rand(kartyak)],random.choice(szinek))
                    sajat_pakli.append(kartya)
                    kartya.kiir()
                    ERTEK=0
                    for k in sajat_pakli:
                        ERTEK = ERTEK+k.erteke
                    print(f"Kártyáid értéke: {ERTEK}")
                    
                    if ERTEK > 21:
                        print("vesztettél")
                        
                        break
                    elif ERTEK == 21:
                        megmaradtzseton+=(TET*2)
                        print("nyertel")
                        
                        break        
                    bekert=input('Válassz: HIT,STAND,DOUBLE ')
        elif bekert=='DOUBLE' or bekert=='double':
            megmaradtzseton-=TET
            TET = TET*2

        print("Az osztó kártyái: ")
        kartya1.kiir()
        kartya2.kiir()
        print(f"az osztó kártyáinak értéke: {OSZTOERTEK}")
        while OSZTOERTEK<17:
            OSZTOERTEK=0
            kartya = Kartya(kartyak[rand(kartyak)],random.choice(szinek))
            oszto_pakli.append(kartya)
            kartya.kiir()
            for k in oszto_pakli:
                OSZTOERTEK = OSZTOERTEK+k.erteke
            print(f"az osztó kártyáinak értéke: {OSZTOERTEK}")
            if OSZTOERTEK==21:
                print("vesztettél")
                break
            elif OSZTOERTEK>21:
                megmaradtzseton+=(TET*2)
                print("nyertel")
                break   
            elif OSZTOERTEK<ERTEK:
                megmaradtzseton+=(TET*2)
                print("nyertel")
                break  
            elif OSZTOERTEK>ERTEK:
                print("vesztettél")
                break
            elif OSZTOERTEK==ERTEK:
                print("a kártyák értéke egyenlő")
                megmaradtzseton+=TET
        print(f"a megmardt zsetonod: {megmaradtzseton}")   
        jatek = (input(f'akarsz ujj játékot kezdeni? (+igen minden más nem) '))
        alapzseton=megmaradtzseton

""""""
