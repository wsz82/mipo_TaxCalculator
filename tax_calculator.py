from typing import Dict

PODSTAWA_KOD = "PODSTW"
SKLADKA_EMERYTALNA_KOD = "S_EM"
SKLADKA_RENTOWA_KOD = "S_RE"
UBEZPIECZENIE_CHOROBOWE_KOD = "U_CH"
PODSTAWA_UBEZPIECZENIA_ZDROWOTNEGO_KOD = "POD_ZDR"
SKLADKA_ZDROWOTNA_9_PROC_KOD = "S_ZDR_1"
SKLADKA_ZDROWOTNA_7_75_PROC_KOD = "S_ZDR_2"
ZALICZKA_US_18_KOD = "ZAL_US_18"
KOSZTY_UZYSKANIA_KOD = "KOSZ_UZ"
PODSTAWA_OPODATKOWANIA_KOD = "PODST_ZAOKR"
PODSTAWA_OPODATKOWANIA_ZAOKRAGLONA_KOD = "PODST_OPO_ZAOKR"
KWOTA_WOLNA_KOD = "KWT_WOL"
PODATEK_POTRACONY_KOD = "PDT_POTR"
ZALICZKA_US_KOD = "ZAL_US"
ZALICZKA_US_ZAOKRAGLONA_KOD = "ZAL_US_ZAOKR"
WYNAGRODZENIE_KOD = "WYNAGR"
KOSZTY_UZYSKANIA_PRZYCHODU_STALE_KOD = "KSZ_UZK_PRZYCH_ST"

_PODSTAWA_SKLADKI_EMERYTALNEJ = 9.76
_PODSTAWA_SKLADKI_RENTOWEJ = 1.5
_PODSTAWA_UBEZPIECZENIA_CHOROBOWEGO = 2.45
_PODSTAWA_WYMIARU_SKLADKI_ZDROWOTNEJ_9 = 9
_PODSTAWA_WYMIARU_SKLADKI_ZDROWOTNEJ_7_75 = 7.75
_PODSTAWA_ZALICZKI_NA_PODATEK = 18
_KWOTA_ZMNIEJSZAJACA_PODATEK_NA_UMOWIE_O_PRACE = 46.33
_KOSZTY_UZYSKANIA_NA_UMOWIE_O_PRACE = 111.25

KOD_WYNIKU_DO_OPISU = dict[str, str]([
    (PODSTAWA_KOD, "Podstawa wymiaru składek"),
    (SKLADKA_EMERYTALNA_KOD, "Składka na ubezpieczenie emerytalne"),
    (SKLADKA_RENTOWA_KOD, "Składka na ubezpieczenie rentowe"),
    (UBEZPIECZENIE_CHOROBOWE_KOD, "Składka na ubezpieczenie chorobowe"),
    (PODSTAWA_UBEZPIECZENIA_ZDROWOTNEGO_KOD, "Podstawa wymiaru składki na ubezpieczenie zdrowotne"),
    (SKLADKA_ZDROWOTNA_9_PROC_KOD, "Składka na ubezpieczenie zdrowotne: 9%"),
    (SKLADKA_ZDROWOTNA_7_75_PROC_KOD, "Składka na ubezpieczenie zdrowotne: 7,75%"),
    (KOSZTY_UZYSKANIA_KOD, "Koszty uzyskania przychodu w wysokości"),
    (PODSTAWA_OPODATKOWANIA_KOD, "Podstawa opodatkowania"),
    (PODSTAWA_OPODATKOWANIA_ZAOKRAGLONA_KOD, "Podstawa opodatkowania zaokrąglona"),
    (ZALICZKA_US_18_KOD, "Zaliczka na podatek dochodowy 18%"),
    (KWOTA_WOLNA_KOD, "Kowta wolna od podatku"),
    (PODATEK_POTRACONY_KOD, "Podatek potrącony"),
    (ZALICZKA_US_KOD, "Zaliczka do urzędu skarbowego"),
    (ZALICZKA_US_ZAOKRAGLONA_KOD, "Zaliczka do urzędu skarbowego zaokrąglona"),
    (WYNAGRODZENIE_KOD, "Pracownik otrzyma wynagrodzenie netto w wysokości"),
    (KOSZTY_UZYSKANIA_PRZYCHODU_STALE_KOD, "Koszty uzyskania przychodu (stałe)"),
])


class TaxCalculator(object):

    def __init__(self):
        self.podstawa: float = 0
        self._kod_wyniku_do_wyniku: Dict[str, float] = dict[str, float]()
        self._podstawa_ubezpieczenia_zdrowotnego = 0
        self._zaliczka_us = 0
        self._zaliczka_us_zaokraglona = 0
        self._zaliczka_na_podatek = 0
        self._skladka_emerytalna = 0
        self._skladka_rentowa = 0
        self._ubezpieczenie_chorobowe = 0
        self._koszty_uzyskania = 0
        self._podstawa_opodatkowania = 0
        self._podstawa_opodatkowania_zaokraglona = 0
        self._podatek_potracony = 0
        self._skladka_zdrowotna_9_procent = 0
        self._skladka_zdrowotna_7_75_procent = 0
        self._wynagrodzenie = 0

    def calculate(self) -> Dict[str, float]:
        pass

    def _add_item(self, code: str, value: float):
        self._kod_wyniku_do_wyniku.update({code: value})

    def _oblicz_zaliczke_na_podatek(self):
        self._zaliczka_na_podatek = (self._podstawa_opodatkowania_zaokraglona * _PODSTAWA_ZALICZKI_NA_PODATEK) / 100

    def _oblicz_podstawe(self):
        self._skladka_emerytalna = (self.podstawa * _PODSTAWA_SKLADKI_EMERYTALNEJ) / 100
        self._skladka_rentowa = (self.podstawa * _PODSTAWA_SKLADKI_RENTOWEJ) / 100
        self._ubezpieczenie_chorobowe = (self.podstawa * _PODSTAWA_UBEZPIECZENIA_CHOROBOWEGO) / 100
        self._podstawa_ubezpieczenia_zdrowotnego = \
            (self.podstawa - self._skladka_emerytalna - self._skladka_rentowa - self._ubezpieczenie_chorobowe)

    def _oblicz_ubezpieczenia(self):
        self._skladka_zdrowotna_9_procent = \
            (self._podstawa_ubezpieczenia_zdrowotnego * _PODSTAWA_WYMIARU_SKLADKI_ZDROWOTNEJ_9) / 100
        self._skladka_zdrowotna_7_75_procent = \
            (self._podstawa_ubezpieczenia_zdrowotnego * _PODSTAWA_WYMIARU_SKLADKI_ZDROWOTNEJ_7_75) / 100


class EmploymentContractTaxCalculator(TaxCalculator):

    def calculate(self):
        self._oblicz_podstawe()
        self._oblicz_ubezpieczenia()
        self._oblicz_podstawe_opodatkowania()
        self._oblicz_zaliczke_na_podatek()
        self._oblicz_podatek_potracony()
        self._oblicz_zaliczke_us()
        self._oblicz_wynagrodzenie()

        self._add_item(PODSTAWA_KOD, self.podstawa)

        self._add_item(SKLADKA_EMERYTALNA_KOD, float("{0:.2f}".format(self._skladka_emerytalna)))
        self._add_item(SKLADKA_RENTOWA_KOD, float("{0:.2f}".format(self._skladka_rentowa)))
        self._add_item(UBEZPIECZENIE_CHOROBOWE_KOD, float("{0:.2f}".format(self._ubezpieczenie_chorobowe)))
        self._add_item(PODSTAWA_UBEZPIECZENIA_ZDROWOTNEGO_KOD, self._podstawa_ubezpieczenia_zdrowotnego)

        self._add_item(SKLADKA_ZDROWOTNA_9_PROC_KOD, float("{0:.2f}".format(self._skladka_zdrowotna_9_procent)))
        self._add_item(SKLADKA_ZDROWOTNA_7_75_PROC_KOD, float("{0:.2f}".format(self._skladka_zdrowotna_7_75_procent)))
        self._add_item(KOSZTY_UZYSKANIA_KOD, _KOSZTY_UZYSKANIA_NA_UMOWIE_O_PRACE)

        self._add_item(PODSTAWA_OPODATKOWANIA_KOD, self._podstawa_opodatkowania)
        self._add_item(PODSTAWA_OPODATKOWANIA_ZAOKRAGLONA_KOD, self._podstawa_opodatkowania_zaokraglona)

        self._add_item(ZALICZKA_US_18_KOD, self._zaliczka_na_podatek)
        self._add_item(KWOTA_WOLNA_KOD, _KWOTA_ZMNIEJSZAJACA_PODATEK_NA_UMOWIE_O_PRACE)

        self._add_item(PODATEK_POTRACONY_KOD, float("{0:.2f}".format(self._podatek_potracony)))

        self._add_item(ZALICZKA_US_KOD, float("{0:.2f}".format(self._zaliczka_us)))
        self._add_item(ZALICZKA_US_ZAOKRAGLONA_KOD, self._zaliczka_us_zaokraglona)

        self._add_item(WYNAGRODZENIE_KOD, float("{0:.2f}".format(self._wynagrodzenie)))
        return self._kod_wyniku_do_wyniku

    def _oblicz_podatek_potracony(self):
        self._podatek_potracony = self._zaliczka_na_podatek - _KWOTA_ZMNIEJSZAJACA_PODATEK_NA_UMOWIE_O_PRACE

    def _oblicz_podstawe_opodatkowania(self):
        self._podstawa_opodatkowania = self._podstawa_ubezpieczenia_zdrowotnego - _KOSZTY_UZYSKANIA_NA_UMOWIE_O_PRACE
        self._podstawa_opodatkowania_zaokraglona = round(self._podstawa_opodatkowania)

    def _oblicz_wynagrodzenie(self):
        self._wynagrodzenie = self.podstawa - (
                (self._skladka_emerytalna + self._skladka_rentowa + self._ubezpieczenie_chorobowe)
                + self._skladka_zdrowotna_9_procent + self._zaliczka_us_zaokraglona)

    def _oblicz_zaliczke_us(self):
        self._zaliczka_us = (self._zaliczka_na_podatek - self._skladka_zdrowotna_7_75_procent -
                             _KWOTA_ZMNIEJSZAJACA_PODATEK_NA_UMOWIE_O_PRACE)
        self._zaliczka_us_zaokraglona = round(self._zaliczka_us)


class CommissionContractTaxCalculator(TaxCalculator):

    def calculate(self):
        self._oblicz_podstawe()
        self._oblicz_ubezpieczenia()
        self._oblicz_koszty_uzyskania()
        self._oblicz_podstawe_opodatkowania()
        self._oblicz_zaliczke_na_podatek()
        self._oblicz_podatek_potracony()
        self._oblicz_zaliczke_us()
        self._oblicz_wynagrodzenie()

        self._add_item(PODSTAWA_KOD, self.podstawa)

        self._add_item(SKLADKA_EMERYTALNA_KOD, float("{0:.2f}".format(self._skladka_emerytalna)))
        self._add_item(SKLADKA_RENTOWA_KOD, float("{0:.2f}".format(self._skladka_rentowa)))
        self._add_item(UBEZPIECZENIE_CHOROBOWE_KOD, float("{0:.2f}".format(self._ubezpieczenie_chorobowe)))
        self._add_item(PODSTAWA_UBEZPIECZENIA_ZDROWOTNEGO_KOD, self._podstawa_ubezpieczenia_zdrowotnego)

        self._add_item(SKLADKA_ZDROWOTNA_9_PROC_KOD, float("{0:.2f}".format(self._skladka_zdrowotna_9_procent)))
        self._add_item(SKLADKA_ZDROWOTNA_7_75_PROC_KOD, float("{0:.2f}".format(self._skladka_zdrowotna_7_75_procent)))

        self._add_item(KOSZTY_UZYSKANIA_PRZYCHODU_STALE_KOD, self._koszty_uzyskania)

        self._add_item(PODSTAWA_OPODATKOWANIA_KOD, self._podstawa_opodatkowania)
        self._add_item(PODSTAWA_OPODATKOWANIA_ZAOKRAGLONA_KOD, self._podstawa_opodatkowania_zaokraglona)

        self._add_item(ZALICZKA_US_18_KOD, self._zaliczka_na_podatek)

        self._add_item(PODATEK_POTRACONY_KOD, float("{0:.2f}".format(self._podatek_potracony)))

        self._add_item(ZALICZKA_US_KOD, float("{0:.2f}".format(self._zaliczka_us)))
        self._add_item(ZALICZKA_US_ZAOKRAGLONA_KOD, self._zaliczka_us_zaokraglona)

        self._add_item(WYNAGRODZENIE_KOD, float("{0:.2f}".format(self._wynagrodzenie)))
        return self._kod_wyniku_do_wyniku

    def _oblicz_podatek_potracony(self):
        self._podatek_potracony = self._zaliczka_na_podatek

    def _oblicz_koszty_uzyskania(self):
        self._koszty_uzyskania = (self._podstawa_ubezpieczenia_zdrowotnego * 20) / 100

    def _oblicz_podstawe_opodatkowania(self):
        self._podstawa_opodatkowania = self._podstawa_ubezpieczenia_zdrowotnego - self._koszty_uzyskania
        self._podstawa_opodatkowania_zaokraglona = round(self._podstawa_opodatkowania)

    def _oblicz_wynagrodzenie(self):
        self._wynagrodzenie = self.podstawa - (
                (self._skladka_emerytalna + self._skladka_rentowa + self._ubezpieczenie_chorobowe)
                + self._skladka_zdrowotna_9_procent + self._zaliczka_us_zaokraglona)

    def _oblicz_zaliczke_us(self):
        self._zaliczka_us = self._zaliczka_na_podatek - self._skladka_zdrowotna_7_75_procent
        self._zaliczka_us_zaokraglona = round(self._zaliczka_us)


class TaxCalculatorFactory:

    @staticmethod
    def create_from(typ_umowy: str):
        if typ_umowy == "P":
            return EmploymentContractTaxCalculator()
        elif typ_umowy == "Z":
            return CommissionContractTaxCalculator()
        else:
            return None
