#--FŐ ADATOK--
import random
J=10
Q=10
K=10
A=10
kartyak = [2,3,4,5,6,7,8,9,10,J,Q,K,A]
szinek = ["♥","♠","♦","♣"]
alapzseton = 100
megmaradtzseton = 100
sajat_pakli=[]
sajat_pakli_szine=[]

#--SZÁMOLÁSOK--
class KARTYA():
    def __init__(self, KartyaErtek, Szinek):
        self.KartyaErtek = KartyaErtek
        self.Szinek = Szinek
def RandomKartya(Kartyaszam):
    Kartyaszam = Kartyaszam(random.choice(kartyak))
    return Kartyaszam
def RandomSzin(Kartyaszin):
    Kartyaszin = Kartyaszin(random.choice(szinek))
    return Kartyaszin
#--A FŐ JÁTÉK--
while megmaradtzseton != 0:
    jatek = input("Új játékba kezdel? ('ENTER' a kezdéshez, '-' a kilépéshez! ) ")
    if jatek == "-":
        print(f"VÉGSŐ ZSETONOD: {alapzseton}")
        break
    elif jatek != "" and jatek != "-":
        print("Te kis rafkós, hogy nem az entert nyomtad, de így is elindul a játék!")
        print(f"Jelenlegi zsetonjaid: {alapzseton}")
        tet = int(input("Tedd meg a Tétedet: "))
        megmaradtzseton = alapzseton - tet
        while megmaradtzseton < 0:
            megmaradtzseton = alapzseton  
            print("Túl nagy tétet tettél, kisebb téttel játszhatsz csak!")
            tet = int(input("Tedd meg a Tétedet: "))
            megmaradtzseton = alapzseton - tet

        sajatertek = 0
        osztoertek = 0

        #Kártyák kiválasztása
        elsosajatkartya = KARTYA(RandomKartya, RandomSzin)
        masodiksajatkartya = KARTYA(RandomKartya, RandomSzin)
        elsoosztokartya = KARTYA(RandomKartya, RandomSzin)
        masodikosztokartya = KARTYA(RandomKartya, RandomSzin)

        #Saját összegzés
        print(f"Jelenlegi kártyáid -> {elsosajatkartya}, {masodiksajatkartya}")
        sajatertek = elsosajatkartya[0] + masodiksajatkartya[0]
        print(f"Lapjaid értéke: {sajatertek}")

        #Ellenfél összegzés
        print(f"Az osztó kártyái -> {elsoosztokartya} és ?")

        #Saját rész
        if alapzseton >= tet:
            akcio = input("Mit csinálsz? (DOUBLE/HIT/STAND - nagy betűvel írd be, pls) ")

            if alapzseton/2 > tet and akcio == "DOUBLE":
                tet = tet*2
            elif akcio == "HIT":
                harmadiksajatkartya = Kartya
