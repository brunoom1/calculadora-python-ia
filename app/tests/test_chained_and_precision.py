"""
Testes para operações encadeadas e refinamentos de separadores/precisão.

Cobre operações consecutivas, separadores de milhar e decimal, e precisão.
"""

import pytest
import sys
from pathlib import Path

# Adicionar src ao path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from calculator import Calculator
from locale_manager import LocaleManager


class TestChainedOperations:
    """Testes de operações encadeadas (T3.4)."""

    def test_chain_two_additions(self, calculator):
        """Teste: 5 + 3 = 8, depois 8 + 2 = 10"""
        result1 = calculator.calculate(5, 3, '+')
        assert result1 == 8
        
        result2 = calculator.calculate(result1, 2, '+')
        assert result2 == 10

    def test_chain_mixed_operations(self, calculator):
        """Teste: 10 - 3 = 7, depois 7 × 2 = 14"""
        result1 = calculator.calculate(10, 3, '-')
        assert result1 == 7
        
        result2 = calculator.calculate(result1, 2, '*')
        assert result2 == 14

    def test_chain_four_operations(self, calculator):
        """Teste: ((10 + 5) - 3) × 2 = 24"""
        # 10 + 5 = 15
        result1 = calculator.calculate(10, 5, '+')
        assert result1 == 15
        
        # 15 - 3 = 12
        result2 = calculator.calculate(result1, 3, '-')
        assert result2 == 12
        
        # 12 × 2 = 24
        result3 = calculator.calculate(result2, 2, '*')
        assert result3 == 24

    def test_chain_with_division(self, calculator):
        """Teste: (20 + 4) ÷ 2 = 12"""
        result1 = calculator.calculate(20, 4, '+')
        result2 = calculator.calculate(result1, 2, '/')
        assert result2 == 12

    def test_chain_preserves_precision(self, calculator):
        """Teste: Precisão mantida em operações encadeadas"""
        # 1 ÷ 3 = 0.333333
        result1 = calculator.calculate(1, 3, '/')
        assert result1 == 0.333333
        
        # 0.333333 × 3 ≈ 1 (com arredondamento)
        result2 = calculator.calculate(result1, 3, '*')
        assert abs(result2 - 1.0) < 0.000001

    def test_chain_negative_intermediate(self, calculator):
        """Teste: Operação encadeada com resultado negativo"""
        # 5 - 10 = -5
        result1 = calculator.calculate(5, 10, '-')
        assert result1 == -5
        
        # -5 × 2 = -10
        result2 = calculator.calculate(result1, 2, '*')
        assert result2 == -10


class TestDecimalSeparator:
    """Testes de separador decimal (vírgula) — T3.1."""

    def test_format_single_decimal(self, locale_manager):
        """Teste: 1.5 → "1,5" """
        result = locale_manager.format_number(1.5)
        assert result == "1,5"

    def test_format_multiple_decimals(self, locale_manager):
        """Teste: 123.456 → "123,456" """
        result = locale_manager.format_number(123.456)
        assert result == "123,456"

    def test_format_max_precision_decimals(self, locale_manager):
        """Teste: 0.123456 → "0,123456" (6 casas máximo)"""
        result = locale_manager.format_number(0.123456)
        assert result == "0,123456"

    def test_parse_single_decimal(self, locale_manager):
        """Teste: "1,5" → 1.5"""
        result = locale_manager.parse_number("1,5")
        assert result == 1.5

    def test_parse_multiple_decimals(self, locale_manager):
        """Teste: "123,456" → 123.456"""
        result = locale_manager.parse_number("123,456")
        assert abs(result - 123.456) < 0.000001

    def test_decimal_with_thousand_separator(self, locale_manager):
        """Teste: "1.234,56" → 1234.56"""
        result = locale_manager.parse_number("1.234,56")
        assert abs(result - 1234.56) < 0.000001

    def test_large_decimal_number(self, locale_manager):
        """Teste: "1.234.567,89" → 1234567.89"""
        result = locale_manager.parse_number("1.234.567,89")
        assert abs(result - 1234567.89) < 0.000001


class TestThousandSeparator:
    """Testes de separador de milhar (ponto) — T3.2."""

    def test_format_thousand_boundary(self, locale_manager):
        """Teste: 1000 → "1.000" """
        result = locale_manager.format_number(1000)
        assert result == "1.000"

    def test_format_multiple_thousands(self, locale_manager):
        """Teste: 1234567 → "1.234.567" """
        result = locale_manager.format_number(1234567)
        assert result == "1.234.567"

    def test_format_thousand_with_decimal(self, locale_manager):
        """Teste: 1234.56 → "1.234,56" """
        result = locale_manager.format_number(1234.56)
        assert result == "1.234,56"

    def test_format_negative_thousand(self, locale_manager):
        """Teste: -1234.56 → "-1.234,56" """
        result = locale_manager.format_number(-1234.56)
        assert result == "-1.234,56"

    def test_parse_thousand_separator(self, locale_manager):
        """Teste: "1.000" → 1000"""
        result = locale_manager.parse_number("1.000")
        assert result == 1000

    def test_parse_multiple_thousand_separators(self, locale_manager):
        """Teste: "1.234.567" → 1234567"""
        result = locale_manager.parse_number("1.234.567")
        assert result == 1234567

    def test_thousand_separator_without_decimals(self, locale_manager):
        """Teste: "10.000" formata como "10.000" (sem casas decimais)"""
        value = 10000.0
        result = locale_manager.format_number(value)
        assert result == "10.000"

    def test_thousand_separator_only_integer_part(self, locale_manager):
        """Teste: 999 não tem separador → "999" """
        result = locale_manager.format_number(999)
        assert result == "999"

    def test_large_number_with_all_separators(self, locale_manager):
        """Teste: 1234567.89 → "1.234.567,89" """
        result = locale_manager.format_number(1234567.89)
        assert result == "1.234.567,89"


class TestPrecision:
    """Testes de precisão até 6 casas decimais — T3.3."""

    def test_precision_six_decimals_exact(self, calculator):
        """Teste: 1 ÷ 3 tem exatamente 6 casas"""
        result = calculator.calculate(1, 3, '/')
        
        # Converter para string para contar casas
        result_str = str(result)
        decimal_places = len(result_str.split('.')[1]) if '.' in result_str else 0
        
        assert decimal_places == 6

    def test_precision_rounding_up(self, calculator):
        """Teste: 2 ÷ 3 = 0.666667 (arredonda para cima)"""
        result = calculator.calculate(2, 3, '/')
        assert result == 0.666667

    def test_precision_rounding_down(self, calculator):
        """Teste: Arredondamento para baixo funciona"""
        result = calculator.calculate(1, 6, '/')
        # 1/6 = 0.166666... deve arredondar para 0.166667
        assert result == 0.166667

    def test_precision_truncates_extra_decimals(self, locale_manager):
        """Teste: Números com mais de 6 decimais são truncados"""
        # Formato tem 6 decimais máximo
        result = locale_manager.format_number(0.123456789)
        
        if ',' in result:
            decimal_part = result.split(',')[1]
            assert len(decimal_part) <= 6

    def test_precision_preserve_small_numbers(self, calculator):
        """Teste: Números pequenos mantêm precisão"""
        result = calculator.calculate(0.000001, 0.000002, '+')
        assert result == 0.000003

    def test_precision_with_large_numbers(self, calculator):
        """Teste: Precisão também vale para números grandes"""
        result = calculator.calculate(1000000.123456, 1, '+')
        # Arredondar para 6 casas
        assert abs(result - 1000001.123456) < 0.000001

    def test_precision_multiple_operations(self, calculator):
        """Teste: Precisão mantida em múltiplas operações"""
        # 1 ÷ 3 = 0.333333
        result1 = calculator.calculate(1, 3, '/')
        # × 2 = 0.666666
        result2 = calculator.calculate(result1, 2, '*')
        # × 3 ≈ 2 (com erro de arredondamento)
        result3 = calculator.calculate(result2, 3, '/')
        
        # Deve estar próximo de 2
        assert abs(result3 - 2.0) < 0.00001


class TestCombinedSeparatorsAndPrecision:
    """Testes combinando separadores e precisão."""

    def test_format_precise_decimal_with_thousand(self, locale_manager):
        """Teste: 1234.123456 → "1.234,123456" """
        result = locale_manager.format_number(1234.123456)
        assert result == "1.234,123456"

    def test_parse_format_round_trip(self, locale_manager):
        """Teste: Parse → Format preserva valor"""
        original = "1.234,56"
        parsed = locale_manager.parse_number(original)
        formatted = locale_manager.format_number(parsed)
        
        assert formatted == original

    def test_calculation_with_separators_precision(self, calculator, locale_manager):
        """Teste: Cálculo com parse/format mantém separadores e precisão"""
        # Parse
        a = locale_manager.parse_number("10.000,50")
        b = locale_manager.parse_number("5.000,25")
        
        # Calcular
        result = calculator.calculate(a, b, '+')
        
        # Formatar
        formatted = locale_manager.format_number(result)
        
        # Deve ter separador e mostrar resultado correto
        assert formatted == "15.000,75"

    def test_division_with_precision_and_separators(self, calculator, locale_manager):
        """Teste: Divisão com 6 casas e separadores"""
        # 1.000 ÷ 3
        result = calculator.calculate(1000, 3, '/')
        
        # Formatar com separadores
        formatted = locale_manager.format_number(result)
        
        # Deve ter vírgula (decimal) e no máximo 6 casas
        assert ',' in formatted
        decimal_part = formatted.split(',')[1]
        assert len(decimal_part) <= 6
