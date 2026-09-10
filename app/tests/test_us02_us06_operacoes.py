# -*- coding: utf-8 -*-
"""
Testes para US02 até US06 — Operações Matemáticas

US02: Subtração
US03: Multiplicação  
US04: Divisão
US05: Negativos
US06: Precisão
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path("app/src")))

from calculator import Calculator
from locale_manager import LocaleManager


def test_all_operations():
    calc = Calculator()
    locale = LocaleManager.get_instance()
    
    all_tests = []
    
    # ====================================================================
    # US02: Subtração
    # ====================================================================
    print("\n[US02] SUBTRACAO\n")
    us02_tests = []
    
    # Caso 1: 10 - 4 = 6
    r = calc.calculate(10, 4, '-')
    us02_tests.append(("10 - 4 = 6", r == 6.0))
    
    # Caso 2: 0 - 0 = 0
    r = calc.calculate(0, 0, '-')
    us02_tests.append(("0 - 0 = 0", r == 0.0))
    
    # Caso 3: 5 - 10 = -5
    r = calc.calculate(5, 10, '-')
    us02_tests.append(("5 - 10 = -5", r == -5.0))
    
    # Caso 4: 15,5 - 5,5 = 10
    r = calc.calculate(15.5, 5.5, '-')
    us02_tests.append(("15,5 - 5,5 = 10", r == 10.0))
    
    # Caso 5: 50 - 0,01 = 49,99
    r = calc.calculate(50, 0.01, '-')
    us02_tests.append(("50 - 0,01 = 49,99", abs(r - 49.99) < 0.0001))
    
    # Fluxo UI
    v1 = locale.parse_number("10")
    v2 = locale.parse_number("4")
    r = calc.calculate(v1, v2, '-')
    d = locale.format_number(r)
    us02_tests.append(("Fluxo '10' - '4' = '6'", d == "6"))
    
    us02_passed = sum(1 for _, result in us02_tests if result)
    
    for desc, result in us02_tests:
        symbol = "[OK]" if result else "[XX]"
        print(f"  {symbol} {desc}")
    
    print(f"  US02: {us02_passed}/{len(us02_tests)} OK\n")
    all_tests.extend(us02_tests)
    
    # ====================================================================
    # US03: Multiplicação
    # ====================================================================
    print("[US03] MULTIPLICACAO\n")
    us03_tests = []
    
    # Caso 1: 7 * 6 = 42
    r = calc.calculate(7, 6, '*')
    us03_tests.append(("7 * 6 = 42", r == 42.0))
    
    # Caso 2: 0 * 100 = 0
    r = calc.calculate(0, 100, '*')
    us03_tests.append(("0 * 100 = 0", r == 0.0))
    
    # Caso 3: 5 * -2 = -10
    r = calc.calculate(5, -2, '*')
    us03_tests.append(("5 * -2 = -10", r == -10.0))
    
    # Caso 4: 2,5 * 4 = 10
    r = calc.calculate(2.5, 4, '*')
    us03_tests.append(("2,5 * 4 = 10", r == 10.0))
    
    # Caso 5: 3,3 * 3 = 9,9
    r = calc.calculate(3.3, 3, '*')
    us03_tests.append(("3,3 * 3 = 9,9", abs(r - 9.9) < 0.0001))
    
    # Fluxo UI
    v1 = locale.parse_number("7")
    v2 = locale.parse_number("6")
    r = calc.calculate(v1, v2, '*')
    d = locale.format_number(r)
    us03_tests.append(("Fluxo '7' * '6' = '42'", d == "42"))
    
    us03_passed = sum(1 for _, result in us03_tests if result)
    
    for desc, result in us03_tests:
        symbol = "[OK]" if result else "[XX]"
        print(f"  {symbol} {desc}")
    
    print(f"  US03: {us03_passed}/{len(us03_tests)} OK\n")
    all_tests.extend(us03_tests)
    
    # ====================================================================
    # US04: Divisão
    # ====================================================================
    print("[US04] DIVISAO\n")
    us04_tests = []
    
    # Caso 1: 20 / 4 = 5
    r = calc.calculate(20, 4, '/')
    us04_tests.append(("20 / 4 = 5", r == 5.0))
    
    # Caso 2: 0 / 10 = 0
    r = calc.calculate(0, 10, '/')
    us04_tests.append(("0 / 10 = 0", r == 0.0))
    
    # Caso 3: -10 / 2 = -5
    r = calc.calculate(-10, 2, '/')
    us04_tests.append(("-10 / 2 = -5", r == -5.0))
    
    # Caso 4: 7,5 / 2,5 = 3
    r = calc.calculate(7.5, 2.5, '/')
    us04_tests.append(("7,5 / 2,5 = 3", r == 3.0))
    
    # Caso 5: 100 / 3 = 33,333333 (precisao)
    r = calc.calculate(100, 3, '/')
    us04_tests.append(("100 / 3 ~= 33,33", abs(r - 33.333333) < 0.001))
    
    # Caso 6: Divisão por zero
    r = calc.calculate(10, 0, '/')
    us04_tests.append(("10 / 0 = Erro", isinstance(r, str) and "Erro" in r))
    
    # Fluxo UI
    v1 = locale.parse_number("20")
    v2 = locale.parse_number("4")
    r = calc.calculate(v1, v2, '/')
    d = locale.format_number(r)
    us04_tests.append(("Fluxo '20' / '4' = '5'", d == "5"))
    
    us04_passed = sum(1 for _, result in us04_tests if result)
    
    for desc, result in us04_tests:
        symbol = "[OK]" if result else "[XX]"
        print(f"  {symbol} {desc}")
    
    print(f"  US04: {us04_passed}/{len(us04_tests)} OK\n")
    all_tests.extend(us04_tests)
    
    # ====================================================================
    # US05: Números Negativos
    # ====================================================================
    print("[US05] NUMEROS NEGATIVOS\n")
    us05_tests = []
    
    # Caso 1: -5 + -3 = -8
    r = calc.calculate(-5, -3, '+')
    us05_tests.append(("-5 + -3 = -8", r == -8.0))
    
    # Caso 2: -10 - -5 = -5
    r = calc.calculate(-10, -5, '-')
    us05_tests.append(("-10 - -5 = -5", r == -5.0))
    
    # Caso 3: -3 * -4 = 12
    r = calc.calculate(-3, -4, '*')
    us05_tests.append(("-3 * -4 = 12", r == 12.0))
    
    # Caso 4: -20 / -4 = 5
    r = calc.calculate(-20, -4, '/')
    us05_tests.append(("-20 / -4 = 5", r == 5.0))
    
    # Caso 5: -0,5 + 1 = 0,5
    r = calc.calculate(-0.5, 1, '+')
    us05_tests.append(("-0,5 + 1 = 0,5", abs(r - 0.5) < 0.0001))
    
    # Fluxo UI com negativo
    r = calc.calculate(-5, 3, '+')
    d = locale.format_number(r)
    us05_tests.append(("Fluxo '-5' + '3' = '-2'", d == "-2"))
    
    us05_passed = sum(1 for _, result in us05_tests if result)
    
    for desc, result in us05_tests:
        symbol = "[OK]" if result else "[XX]"
        print(f"  {symbol} {desc}")
    
    print(f"  US05: {us05_passed}/{len(us05_tests)} OK\n")
    all_tests.extend(us05_tests)
    
    # ====================================================================
    # US06: Precisão
    # ====================================================================
    print("[US06] PRECISAO\n")
    us06_tests = []
    
    # Caso 1: 0,1 + 0,2 = 0,3
    v1 = locale.parse_number("0,1")
    v2 = locale.parse_number("0,2")
    r = calc.calculate(v1, v2, '+')
    d = locale.format_number(r)
    us06_tests.append(("0,1 + 0,2 = 0,3", d == "0,3"))
    
    # Caso 2: 1/3 * 3 = 1
    r1 = calc.calculate(1, 3, '/')
    r2 = calc.calculate(r1, 3, '*')
    us06_tests.append(("1/3*3 ~= 1", abs(r2 - 1.0) < 0.01))
    
    # Caso 3: 0,123456 (6 decimais)
    r = 0.123456
    d = locale.format_number(r)
    us06_tests.append(("Format 6 decimais", "123456" in d))
    
    # Caso 4: 0,1234567 arredondado a 6 decimais
    r = calc.calculate(0.1234567, 0, '+')
    us06_tests.append(("Arredonda 6 decimais", round(r, 6) == 0.123457))
    
    # Caso 5: Muito grande
    r = calc.calculate(999999999, 999999999, '+')
    us06_tests.append(("Numero grande", r == 1999999998.0))
    
    # Caso 6: Muito pequeno
    r = calc.calculate(0.000001, 0.000002, '+')
    us06_tests.append(("Numero pequeno", abs(r - 0.000003) < 0.000001))
    
    us06_passed = sum(1 for _, result in us06_tests if result)
    
    for desc, result in us06_tests:
        symbol = "[OK]" if result else "[XX]"
        print(f"  {symbol} {desc}")
    
    print(f"  US06: {us06_passed}/{len(us06_tests)} OK\n")
    all_tests.extend(us06_tests)
    
    # ====================================================================
    # RESUMO
    # ====================================================================
    
    total_passed = sum(1 for _, result in all_tests if result)
    total_tests = len(all_tests)
    
    print("="*70)
    print(f"RESULTADO FINAL: {total_passed}/{total_tests} testes passaram")
    print("="*70)
    
    print(f"\nUS02 (Subtracao):      {us02_passed}/{len(us02_tests)}")
    print(f"US03 (Multiplicacao):  {us03_passed}/{len(us03_tests)}")
    print(f"US04 (Divisao):        {us04_passed}/{len(us04_tests)}")
    print(f"US05 (Negativos):      {us05_passed}/{len(us05_tests)}")
    print(f"US06 (Precisao):       {us06_passed}/{len(us06_tests)}")
    
    if total_passed == total_tests:
        print(f"\n[SUCESSO] TODAS AS OPERACOES BASICAS FUNCIONAM!\n")
        return 0
    else:
        print(f"\n[FALHA] {total_tests - total_passed} teste(s) falharam\n")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(test_all_operations())
