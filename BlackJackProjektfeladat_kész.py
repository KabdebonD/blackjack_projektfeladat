#--FŐ ADATOK--
import random
bubi=10
dama=10
kiraly=10
asz = 10
kartyak = [2,3,4,5,6,7,8,9,10,bubi,dama,kiraly,asz]
kiiros_kartyak = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A']
szinek = ["♥","♠","♦","♣"]
alapzseton = 380
sajat_pakli=[]
oszto_pakli=[]
#--SZÁMOLÁSOK--
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
            akimenet=Kimenet("vesztettél",megmaradtzseton)
        elif ERTEK > 21:
            akimenet=Kimenet("vesztettél",megmaradtzseton)
        elif OSZTOERTEK>21:
            megmaradtzseton=megmaradtzseton+(TET*1.5)
            akimenet=Kimenet("nyertél",megmaradtzseton)
        elif OSZTOERTEK<ERTEK and ERTEK <=21:
            megmaradtzseton=megmaradtzseton+(TET*1.5)
            akimenet=Kimenet("nyertél",megmaradtzseton)
            
        elif OSZTOERTEK>ERTEK and OSZTOERTEK <=21:
            akimenet=Kimenet("vesztettél",megmaradtzseton)
            
        elif OSZTOERTEK==ERTEK:
            megmaradtzseton+=TET
            akimenet=Kimenet('az osztó összege pont ugyanannyi mint a te értéked',megmaradtzseton)
        return akimenet

    



jatek = (input(f'akarsz jatszani? (+igen minden más nem) '))
if jatek == "+":
    print("a jatek elkezdodott")
    sajat_pakli
    while jatek=="+":
        sajat_pakli=[]
        oszto_pakli=[]
        print(f"enyi zsetonod van: {alapzseton:.0f}")
        TET= int(input("Tedd meg a téted: "))
        while TET > alapzseton:
            print("nincs ellég pénz")
            TET= int(input("Tedd meg a Tétedet: " ))
        megmaradtzseton=alapzseton-TET
        print(f'A megmaradt zsetonod: {megmaradtzseton}')
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
          
              
        #osztóó
        print("Az osztó kártyái: ") 
        kartyalen1=random.randrange(len(kartyak)) 
        kartyalen2=random.randrange(len(kartyak))     
        kartya1 = Kartya(kartyak[kartyalen1],random.choice(szinek),kiiros_kartyak[kartyalen1])
        kartya2 = Kartya(kartyak[kartyalen2],random.choice(szinek),kiiros_kartyak[kartyalen2])
        oszto_pakli.append(kartya1)
        oszto_pakli.append(kartya2)
        kartya1.kiir()
        print(f"+-----+\n|\   /|\n|  X  |\n|/   \|\n+-----+")
        for k in oszto_pakli:
            OSZTOERTEK = OSZTOERTEK+k.erteke
        bekert=input('Válassz: HIT(h),DOUBLE(d),STAND(enter) ')
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
                        

    
                    bekert=input('Válassz: HIT(h),STAND(enter) ')
        elif bekert=='d':
            if megmaradtzseton-TET>=0:
                megmaradtzseton-=TET
                
                TET = TET*2
            else:
                print('Nincs elég pénzed!')
        print("Az osztó kártyái: ")
        kartya1.kiir()
        kartya2.kiir()
        print(f"az osztó kártyáinak értéke: {OSZTOERTEK}")
        if ERTEK !=21:    
            while OSZTOERTEK<17:
                OSZTOERTEK=0
                kartyalen=random.randrange(len(kartyak))
                kartya = Kartya(kartyak[kartyalen],random.choice(szinek),kiiros_kartyak[kartyalen])
                oszto_pakli.append(kartya)
                kartya.kiir()
                for k in oszto_pakli:
                    OSZTOERTEK = OSZTOERTEK+k.erteke
                print(f"az osztó kártyáinak értéke: {OSZTOERTEK}")
        print(f'{Kimenet.kimenet3(megmaradtzseton,ERTEK,OSZTOERTEK,TET).kimenet}')
        print(f"a megmardt zsetonod: {Kimenet.kimenet3(megmaradtzseton,ERTEK,OSZTOERTEK,TET).zseton:.0f}")   
        jatek = (input(f'akarod folytatni a játékot? (+igen minden más nem) '))
        alapzseton=Kimenet.kimenet3(megmaradtzseton,ERTEK,OSZTOERTEK,TET).zseton


