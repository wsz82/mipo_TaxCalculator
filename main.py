from tax_calculator import TaxCalculatorFactory, KOD_WYNIKU_DO_OPISU


def main():
    kwota_dochodu: float = 0
    typ_umowy: str = ""
    try:
        kwota_dochodu = float(input("Podaj kwotę dochodu: "))
        typ_umowy = input("Typ umowy: (P)raca, (Z)lecenie: ")[0]
    except ValueError:
        print("Błędna kwota")
    tax_calculator = TaxCalculatorFactory.create_from(typ_umowy)
    if not tax_calculator:
        print("Nieznany typ umowy")
        return
    tax_calculator.podstawa = kwota_dochodu
    kod_skladki_do_skladki = tax_calculator.calculate()

    for key, val in kod_skladki_do_skladki.items():
        print(f'{KOD_WYNIKU_DO_OPISU.get(key)}: {val}')


if __name__ == '__main__':
    main()
