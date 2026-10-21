#--FŐ ADATOK--
import random
bubi=10
dama=10
kiraly=10
asz = 10
kartyak = [2,3,4,5,6,7,8,9,10,bubi,dama,kiraly,asz]
kiiros_kartyak = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
szinek = ["♥","♠","♦","♣"]
alapzseton = 1000
sajat_pakli=[]
oszto_pakli=[]

#*----------* SZÁMOLÁSOK *----------*
class Kartya():
    def __init__(self,erteke,szine,kiirasa):
        self.erteke=erteke
        self.szine=szine
        self.kiirasa=kiirasa
    def kiir(self):
        print("+-----+")
        print("|",end="")
        print(self.kiirasa,end="")
        if self.kiirasa !='10':
            for c in range(4):
                print(" ",end="")
        else:
            for c in range(3):
                print(" ",end="")
        print("|")
        print(f"|  {self.szine}  |") 
        print("|",end="")
        if self.kiirasa!='10':
            for c in range(4):    
                print(" ",end="")
        else:
            for c in range(3):
                print(" ",end="")
        print(f"{self.kiirasa}|")
        print("+-----+")
class Kimenet():
    def __init__(self,kimenet,zseton):
        self.kimenet=kimenet
        self.zseton=zseton

    def kimenet3(megmaradtzseton,ERTEK,OSZTOERTEK,TET):
        if OSZTOERTEK==21:
            akimenet=Kimenet("Vesztettél!", megmaradtzseton)
        elif ERTEK > 21:
            akimenet=Kimenet("Vesztettél!", megmaradtzseton)
        elif OSZTOERTEK>21:
            megmaradtzseton=megmaradtzseton+(TET*1.5)
            akimenet=Kimenet("Nyertél!", megmaradtzseton)
        elif OSZTOERTEK<ERTEK and ERTEK <=21:
            megmaradtzseton=megmaradtzseton+(TET*1.5)
            akimenet=Kimenet("Nyertél!", megmaradtzseton)
            
        elif OSZTOERTEK>ERTEK and OSZTOERTEK <=21:
            akimenet=Kimenet("Vesztettél!", megmaradtzseton)
            
        elif OSZTOERTEK==ERTEK:
            megmaradtzseton+=TET
            akimenet=Kimenet('Döntetlen!', megmaradtzseton)
        return akimenet

jatek = (input(f'Játszol? ("+"-al indul a játék, pls azt írd be :c) '))
if jatek == "+":
    print("A JÁTÉK ELKEZDŐDÖTT!")
    sajat_pakli
    while jatek=="+":
        sajat_pakli=[]
        oszto_pakli=[]
        print(f"Jelenlegi zsetonjaid: {alapzseton:.0f}")
        TET= int(input("Tedd meg a tétedet: "))
        while TET > alapzseton or TET<0:
            if TET>alapzseton:    
                print("Nincs elég zsetonod. Le vagy égve, még nem jött fizu.")
            elif TET<0:
                print('A téted nem lehet kisebb mint nulla!')
            TET= int(input("Tedd meg a tétedet: " ))
        megmaradtzseton=alapzseton-TET
        print(f'Megmaradt zsetonjaid: {megmaradtzseton}')
        ERTEK=0  
        OSZTOERTEK=0 
        for i in range(2):
            kartyalen=random.randrange(len(kartyak))
            kartya = Kartya(kartyak[kartyalen],random.choice(szinek),kiiros_kartyak[kartyalen])
            sajat_pakli.append(kartya)
            kartya.kiir()
        for k in sajat_pakli:
            ERTEK = ERTEK+k.erteke
        print(f"Kártyáid értéke: {ERTEK}")
                     
        #*----------* Osztó *----------*
        print("Az osztó kártyái: ") 
        kartyalen1=random.randrange(len(kartyak)) 
        kartyalen2=random.randrange(len(kartyak))     
        kartya1 = Kartya(kartyak[kartyalen1],random.choice(szinek),kiiros_kartyak[kartyalen1])
        kartya2 = Kartya(kartyak[kartyalen2],random.choice(szinek),kiiros_kartyak[kartyalen2])
        oszto_pakli.append(kartya1)
        oszto_pakli.append(kartya2)
        kartya1.kiir()
        print(f"+-----+\n|\\   /|\n|  X  |\n|/   \\|\n+-----+")
        for k in oszto_pakli:
            OSZTOERTEK = OSZTOERTEK+k.erteke
        bekert=input('Válassz: HIT (h) / DOUBLE (d) / STAND(minden más) ')
        if bekert == 'h':       
                while bekert=="h":
                    kartyalen=random.randrange(len(kartyak))
                    kartya = Kartya(kartyak[kartyalen],random.choice(szinek),kiiros_kartyak[kartyalen])
                    sajat_pakli.append(kartya)
                    kartya.kiir()
                    ERTEK=0
                    for k in sajat_pakli:
                        ERTEK = ERTEK+k.erteke
                    print(f"Kártyáid értéke: {ERTEK}")
                    
                    if ERTEK >= 21:
                        break
                        
                    bekert=input('Válassz: HIT(h) / STAND(enter) ')
        elif bekert=='d':
            if megmaradtzseton-TET>=0:
                megmaradtzseton-=TET
                TET = TET*2
                kartyalen=random.randrange(len(kartyak))
                kartya = Kartya(kartyak[kartyalen],random.choice(szinek),kiiros_kartyak[kartyalen])
                sajat_pakli.append(kartya)
                kartya.kiir()
                ERTEK=0
                for k in sajat_pakli:
                    ERTEK = ERTEK+k.erteke
                print(f"Kártyáid értéke: {ERTEK}")
            else:
                print('Szegénység van, nincs elég zsetonod!')
        print("Az osztó kártyái: ")
        kartya1.kiir()
        kartya2.kiir()
        print(f"Az osztó kártyáinak értéke: {OSZTOERTEK}")
        if ERTEK !=21:    
            while OSZTOERTEK<17:
                OSZTOERTEK=0
                kartyalen=random.randrange(len(kartyak))
                kartya = Kartya(kartyak[kartyalen],random.choice(szinek),kiiros_kartyak[kartyalen])
                oszto_pakli.append(kartya)
                kartya.kiir()
                for k in oszto_pakli:
                    OSZTOERTEK = OSZTOERTEK+k.erteke
                print(f"Az osztó kártyáinak értéke: {OSZTOERTEK}")
        print(f'{Kimenet.kimenet3(megmaradtzseton,ERTEK,OSZTOERTEK,TET).kimenet}')
        print(f"A megmaradt zsetonjaid: {Kimenet.kimenet3(megmaradtzseton,ERTEK,OSZTOERTEK,TET).zseton:.0f}")   
        jatek = (input(f'Akarod folytatni a játékot? ("+" a folytatáshoz) '))
        alapzseton=Kimenet.kimenet3(megmaradtzseton,ERTEK,OSZTOERTEK,TET).zseton