class TaxCalculator(object):
    podstawa = 0
    umowa = ""
    # składki na ubezpieczenie społeczne
    s_emerytalna = 0 # 9,76% podstawy
    s_rentowa = 0 # 1,5% podstawy
    u_chorobowe = 0 # 2,45% podstawy
    # sładki na ubezpieczenie zdrowotne
    kosztyUzyskania = 111.25
    s_zdrow1 = 0 # od podstawy wymiaru 9%
    s_zdrow2 = 0 # od podstawy wymiaru 7,75%
    zaliczkaNaPod = 0 # zaliczka na podatek dochodowy 18%
    kwotaZmiejsz = 46.33 # kwota zmniejszająca podatek 46,33 PLN
    zaliczkaUS = 0
    zaliczkaUS0 = 0

    @staticmethod
    def main():
        try:
            TaxCalculator.podstawa=float(input("Podaj kwotę dochodu: "))
            TaxCalculator.umowa=input("Typ umowy: (P)raca, (Z)lecenie: ")[0]
        except ValueError:
            print("Błędna kwota")
            return
        if TaxCalculator.umowa=="P":
            print("Umowa o pracę")
            print("Podstawa wymiaru składek ", TaxCalculator.podstawa)
            oPodstawa = TaxCalculator.obliczonaPodstawa(TaxCalculator.podstawa)
            print("Składka na ubezpieczenie emerytalne "+"{0:.2f}".format(TaxCalculator.s_emerytalna))
            print("Składka na ubezpieczenie rentowe    "+"{0:.2f}".format(TaxCalculator.s_rentowa))
            print("Składka na ubezpieczenie chorobowe  "+"{0:.2f}".format(TaxCalculator.u_chorobowe))
            print("Podstawa wymiaru składki na ubezpieczenie zdrowotne: ",oPodstawa)
            TaxCalculator.obliczUbezpieczenia(oPodstawa)
            print("Składka na ubezpieczenie zdrowotne: 9% = " \
                  +"{0:.2f}".format(TaxCalculator.s_zdrow1)+" 7,75% = "+"{0:.2f}".format(TaxCalculator.s_zdrow2))
            print("Koszty uzyskania przychodu w wysokości ",TaxCalculator.kosztyUzyskania)
            podstawaOpodat = oPodstawa - TaxCalculator.kosztyUzyskania
            podstawaOpodat0 = float("{0:.0f}".format(podstawaOpodat))
            print("Podstawa opodatkowania ",podstawaOpodat," zaokrąglona "+"{0:.0f}".format(podstawaOpodat0))
            TaxCalculator.obliczPodatek(podstawaOpodat0)
            print("Zaliczka na podatek dochodowy 18% =",TaxCalculator.zaliczkaNaPod)
            print("Kowta wolna od podatku =",TaxCalculator.kwotaZmiejsz)
            podatekPotracony = TaxCalculator.zaliczkaNaPod - TaxCalculator.kwotaZmiejsz
            print("Podatek potrącony = "+"{0:.2f}".format(podatekPotracony))
            TaxCalculator.obliczZaliczke()
            TaxCalculator.zaliczkaUS0 = float("{0:.0f}".format(TaxCalculator.zaliczkaUS))
            print("Zaliczka do urzędu skarbowego = "+"{0:.2f}".format(TaxCalculator.zaliczkaUS)+\
                  " po zaokrągleniu "+"{0:.0f}".format(TaxCalculator.zaliczkaUS0))
            wynagrodzenie = TaxCalculator.podstawa - ((TaxCalculator.s_emerytalna + TaxCalculator.s_rentowa \
                            + TaxCalculator.u_chorobowe) + TaxCalculator.s_zdrow1 + TaxCalculator.zaliczkaUS0)
            print()
            print("Pracownik otrzyma wynagrodzenie netto w wysokości = "+"{0:.2f}".format(wynagrodzenie))
            

        elif TaxCalculator.umowa=="Z":
            print("UMOWA-ZLECENIE")
            print("Podstawa wymiaru składek",TaxCalculator.podstawa)
            oPodstawa = TaxCalculator.obliczonaPodstawa(TaxCalculator.podstawa)
            print("Składka na ubezpieczenie emerytalne "+"{0:.2f}".format(TaxCalculator.s_emerytalna))
            print("Składka na ubezpieczenie rentowe    "+"{0:.2f}".format(TaxCalculator.s_rentowa))
            print("Składka na ubezpieczenie chorobowe  "+"{0:.2f}".format(TaxCalculator.u_chorobowe))
            print("Podstawa wymiaru składki na ubezpieczenie zdrowotne: ",oPodstawa)
            TaxCalculator.obliczUbezpieczenia(oPodstawa)
            print("Składka na ubezpieczenie zdrowotne: 9% = " \
                  +"{0:.2f}".format(TaxCalculator.s_zdrow1)+" 7,75% = "+"{0:.2f}".format(TaxCalculator.s_zdrow2))
            TaxCalculator.kwotaZmiejsz = 0
            TaxCalculator.kosztyUzyskania = (oPodstawa * 20) / 100
            print("Koszty uzyskania przychodu (stałe)",TaxCalculator.kosztyUzyskania)
            podstawaOpodat = oPodstawa - TaxCalculator.kosztyUzyskania
            podstawaOpodat0 = float("{0:.0f}".format(podstawaOpodat))
            print("Podstawa opodatkowania ",podstawaOpodat," zaokrąglona "+"{0:.0f}".format(podstawaOpodat0))
            TaxCalculator.obliczPodatek(podstawaOpodat0)
            print("Zaliczka na podatek dochodowy 18% =",TaxCalculator.zaliczkaNaPod)
            podatekPotracony = TaxCalculator.zaliczkaNaPod            
            print("Podatek potrącony = "+"{0:.2f}".format(podatekPotracony))
            TaxCalculator.obliczZaliczke()
            TaxCalculator.zaliczkaUS0 = float("{0:.0f}".format(TaxCalculator.zaliczkaUS))
            print("Zaliczka do urzędu skarbowego = "+"{0:.2f}".format(TaxCalculator.zaliczkaUS)+\
                  " po zaokrągleniu "+"{0:.0f}".format(TaxCalculator.zaliczkaUS0))
            wynagrodzenie = TaxCalculator.podstawa - ((TaxCalculator.s_emerytalna + TaxCalculator.s_rentowa \
                          + TaxCalculator.u_chorobowe) + TaxCalculator.s_zdrow1 + TaxCalculator.zaliczkaUS0)
            print()
            print("Pracownik otrzyma wynagrodzenie netto w wysokości = "+"{0:.2f}".format(wynagrodzenie))
             
        else:
            print("Nieznany typ umowy!")
            
    @staticmethod
    def obliczZaliczke():
        TaxCalculator.zaliczkaUS=TaxCalculator.zaliczkaNaPod - TaxCalculator.s_zdrow2 - TaxCalculator.kwotaZmiejsz

    @staticmethod
    def obliczPodatek(podstawa):
        TaxCalculator.zaliczkaNaPod = (podstawa * 18) / 100

    @staticmethod
    def obliczonaPodstawa(podstawa):
        TaxCalculator.s_emerytalna = (podstawa * 9.76) / 100        
        TaxCalculator.s_rentowa = (podstawa * 1.5) / 100
        TaxCalculator.u_chorobowe = (podstawa * 2.45) / 100
        return (podstawa - TaxCalculator.s_emerytalna- TaxCalculator.s_rentowa - TaxCalculator.u_chorobowe)

    @staticmethod
    def obliczUbezpieczenia(podstawa):
        TaxCalculator.s_zdrow1 = (podstawa * 9) / 100
        TaxCalculator.s_zdrow2 = (podstawa * 7.75) / 100

        
if __name__=='__main__':
    TaxCalculator.main()

