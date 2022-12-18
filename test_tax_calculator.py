from unittest import TestCase

import tax_calculator
from tax_calculator import *


class TestTaxCalculator(TestCase):

    def test_employment_contract_base_2756_gives_1987dot12_income(self):
        calculator = EmploymentContractTaxCalculator()
        podstawa = 2756
        calculator.podstawa = podstawa
        results = calculator.calculate()
        assert results.get(tax_calculator.PODSTAWA_KOD) == podstawa
        assert results.get(tax_calculator.SKLADKA_EMERYTALNA_KOD) == 268.99
        assert results.get(tax_calculator.SKLADKA_RENTOWA_KOD) == 41.34
        assert results.get(tax_calculator.UBEZPIECZENIE_CHOROBOWE_KOD) == 67.52
        assert results.get(tax_calculator.PODSTAWA_UBEZPIECZENIA_ZDROWOTNEGO_KOD) == 2378.1524
        assert results.get(tax_calculator.SKLADKA_ZDROWOTNA_9_PROC_KOD) == 214.03
        assert results.get(tax_calculator.SKLADKA_ZDROWOTNA_7_75_PROC_KOD) == 184.31
        assert results.get(tax_calculator.ZALICZKA_US_18_KOD) == 408.06
        assert results.get(tax_calculator.KOSZTY_UZYSKANIA_KOD) == 111.25
        assert results.get(tax_calculator.PODSTAWA_OPODATKOWANIA_KOD) == 2266.9024
        assert results.get(tax_calculator.PODSTAWA_OPODATKOWANIA_ZAOKRAGLONA_KOD) == 2267
        assert results.get(tax_calculator.KWOTA_WOLNA_KOD) == 46.33
        assert results.get(tax_calculator.PODATEK_POTRACONY_KOD) == 361.73
        assert results.get(tax_calculator.ZALICZKA_US_KOD) == 177.42
        assert results.get(tax_calculator.ZALICZKA_US_ZAOKRAGLONA_KOD) == 177
        assert results.get(tax_calculator.WYNAGRODZENIE_KOD) == 1987.12

    def test_employment_contract_base_10654dot15_gives_7490dot05_income(self):
        calculator = EmploymentContractTaxCalculator()
        podstawa = 10654.15
        calculator.podstawa = podstawa
        results = calculator.calculate()
        assert results.get(tax_calculator.PODSTAWA_KOD) == podstawa
        assert results.get(tax_calculator.SKLADKA_EMERYTALNA_KOD) == 1039.85
        assert results.get(tax_calculator.SKLADKA_RENTOWA_KOD) == 159.81
        assert results.get(tax_calculator.UBEZPIECZENIE_CHOROBOWE_KOD) == 261.03
        assert results.get(tax_calculator.PODSTAWA_UBEZPIECZENIA_ZDROWOTNEGO_KOD) == 9193.466035
        assert results.get(tax_calculator.SKLADKA_ZDROWOTNA_9_PROC_KOD) == 827.41
        assert results.get(tax_calculator.SKLADKA_ZDROWOTNA_7_75_PROC_KOD) == 712.49
        assert results.get(tax_calculator.ZALICZKA_US_18_KOD) == 1634.76
        assert results.get(tax_calculator.KOSZTY_UZYSKANIA_KOD) == 111.25
        assert results.get(tax_calculator.PODSTAWA_OPODATKOWANIA_KOD) == 9082.216035
        assert results.get(tax_calculator.PODSTAWA_OPODATKOWANIA_ZAOKRAGLONA_KOD) == 9082
        assert results.get(tax_calculator.KWOTA_WOLNA_KOD) == 46.33
        assert results.get(tax_calculator.PODATEK_POTRACONY_KOD) == 1588.43
        assert results.get(tax_calculator.ZALICZKA_US_KOD) == 875.94
        assert results.get(tax_calculator.ZALICZKA_US_ZAOKRAGLONA_KOD) == 876
        assert results.get(tax_calculator.WYNAGRODZENIE_KOD) == 7490.05

    def test_commission_contract_base_2756_gives_2006dot12_income(self):
        calculator = CommissionContractTaxCalculator()
        podstawa = 2756
        calculator.podstawa = podstawa
        results = calculator.calculate()
        assert results.get(tax_calculator.PODSTAWA_KOD) == podstawa
        assert results.get(tax_calculator.SKLADKA_EMERYTALNA_KOD) == 268.99
        assert results.get(tax_calculator.SKLADKA_RENTOWA_KOD) == 41.34
        assert results.get(tax_calculator.UBEZPIECZENIE_CHOROBOWE_KOD) == 67.52
        assert results.get(tax_calculator.PODSTAWA_UBEZPIECZENIA_ZDROWOTNEGO_KOD) == 2378.1524
        assert results.get(tax_calculator.SKLADKA_ZDROWOTNA_9_PROC_KOD) == 214.03
        assert results.get(tax_calculator.SKLADKA_ZDROWOTNA_7_75_PROC_KOD) == 184.31
        assert results.get(tax_calculator.ZALICZKA_US_18_KOD) == 342.54
        assert results.get(tax_calculator.KOSZTY_UZYSKANIA_PRZYCHODU_STALE_KOD) == 475.63048
        assert results.get(tax_calculator.PODSTAWA_OPODATKOWANIA_KOD) == 1902.52192
        assert results.get(tax_calculator.PODSTAWA_OPODATKOWANIA_ZAOKRAGLONA_KOD) == 1903
        assert results.get(tax_calculator.PODATEK_POTRACONY_KOD) == 342.54
        assert results.get(tax_calculator.ZALICZKA_US_KOD) == 158.23
        assert results.get(tax_calculator.ZALICZKA_US_ZAOKRAGLONA_KOD) == 158
        assert results.get(tax_calculator.WYNAGRODZENIE_KOD) == 2006.12

    def test_commission_contract_base_10654dot15_gives_7755dot05_income(self):
        calculator = CommissionContractTaxCalculator()
        podstawa = 10654.15
        calculator.podstawa = podstawa
        results = calculator.calculate()
        assert results.get(tax_calculator.PODSTAWA_KOD) == podstawa
        assert results.get(tax_calculator.SKLADKA_EMERYTALNA_KOD) == 1039.85
        assert results.get(tax_calculator.SKLADKA_RENTOWA_KOD) == 159.81
        assert results.get(tax_calculator.UBEZPIECZENIE_CHOROBOWE_KOD) == 261.03
        assert results.get(tax_calculator.PODSTAWA_UBEZPIECZENIA_ZDROWOTNEGO_KOD) == 9193.466035
        assert results.get(tax_calculator.SKLADKA_ZDROWOTNA_9_PROC_KOD) == 827.41
        assert results.get(tax_calculator.SKLADKA_ZDROWOTNA_7_75_PROC_KOD) == 712.49
        assert results.get(tax_calculator.ZALICZKA_US_18_KOD) == 1323.9
        assert results.get(tax_calculator.KOSZTY_UZYSKANIA_PRZYCHODU_STALE_KOD) == 1838.6932069999998
        assert results.get(tax_calculator.PODSTAWA_OPODATKOWANIA_KOD) == 7354.772827999999
        assert results.get(tax_calculator.PODSTAWA_OPODATKOWANIA_ZAOKRAGLONA_KOD) == 7355
        assert results.get(tax_calculator.PODATEK_POTRACONY_KOD) == 1323.90
        assert results.get(tax_calculator.ZALICZKA_US_KOD) == 611.41
        assert results.get(tax_calculator.ZALICZKA_US_ZAOKRAGLONA_KOD) == 611
        assert results.get(tax_calculator.WYNAGRODZENIE_KOD) == 7755.05
