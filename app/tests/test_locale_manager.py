"""
Testes unitários para a classe LocaleManager.

Cobre parsing e formatação de números em pt-BR.
"""

import pytest
import sys
from pathlib import Path

# Adicionar src ao path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from locale_manager import LocaleManager


class TestLocaleManagerSingleton:
    """Testes do padrão Singleton."""

    def test_singleton_instance(self, locale_manager):
        """Teste: LocaleManager é singleton"""
        mgr1 = LocaleManager.get_instance()
        mgr2 = LocaleManager.get_instance()
        assert mgr1 is mgr2

    def test_singleton_new(self, locale_manager):
        """Teste: nova instância é a mesma do singleton"""
        mgr = LocaleManager()
        mgr2 = LocaleManager.get_instance()
        assert mgr is mgr2


class TestLocaleManagerParseNumber:
    """Testes de parsing (string → float) em pt-BR."""

    def test_parse_simple_integer(self, locale_manager):
        """Teste: "123" → 123.0"""
        result = locale_manager.parse_number("123")
        assert result == 123.0

    def test_parse_decimal_comma(self, locale_manager):
        """Teste: "123,45" → 123.45"""
        result = locale_manager.parse_number("123,45")
        assert abs(result - 123.45) < 0.000001

    def test_parse_thousand_separator(self, locale_manager):
        """Teste: "1.234,56" → 1234.56"""
        result = locale_manager.parse_number("1.234,56")
        assert abs(result - 1234.56) < 0.000001

    def test_parse_negative_number(self, locale_manager):
        """Teste: "-123,45" → -123.45"""
        result = locale_manager.parse_number("-123,45")
        assert abs(result - (-123.45)) < 0.000001

    def test_parse_large_number(self, locale_manager):
        """Teste: "1.234.567,89" → 1234567.89"""
        result = locale_manager.parse_number("1.234.567,89")
        assert abs(result - 1234567.89) < 0.000001

    def test_parse_zero(self, locale_manager):
        """Teste: "0" → 0.0"""
        result = locale_manager.parse_number("0")
        assert result == 0.0

    def test_parse_with_spaces(self, locale_manager):
        """Teste: parsing com espaços é limpo"""
        result = locale_manager.parse_number("  123,45  ")
        assert abs(result - 123.45) < 0.000001

    def test_parse_invalid_number(self, locale_manager):
        """Teste: string inválida lança ValueError"""
        with pytest.raises(ValueError):
            locale_manager.parse_number("abc")

    def test_parse_empty_string(self, locale_manager):
        """Teste: string vazia lança ValueError"""
        with pytest.raises(ValueError):
            locale_manager.parse_number("")


class TestLocaleManagerFormatNumber:
    """Testes de formatação (float → string) em pt-BR."""

    def test_format_simple_integer(self, locale_manager):
        """Teste: 123.0 → "123" """
        result = locale_manager.format_number(123.0)
        assert result == "123"

    def test_format_decimal_one_place(self, locale_manager):
        """Teste: 123.4 → "123,4" """
        result = locale_manager.format_number(123.4)
        assert result == "123,4"

    def test_format_decimal_multiple_places(self, locale_manager):
        """Teste: 123.45 → "123,45" """
        result = locale_manager.format_number(123.45)
        assert result == "123,45"

    def test_format_thousand_separator(self, locale_manager):
        """Teste: 1234.56 → "1.234,56" """
        result = locale_manager.format_number(1234.56)
        assert result == "1.234,56"

    def test_format_large_number(self, locale_manager):
        """Teste: 1234567.89 → "1.234.567,89" """
        result = locale_manager.format_number(1234567.89)
        assert result == "1.234.567,89"

    def test_format_negative_number(self, locale_manager):
        """Teste: -123.45 → "-123,45" """
        result = locale_manager.format_number(-123.45)
        assert result == "-123,45"

    def test_format_zero(self, locale_manager):
        """Teste: 0.0 → "0" """
        result = locale_manager.format_number(0.0)
        assert result == "0"

    def test_format_very_small_number(self, locale_manager):
        """Teste: 0.001 → "0,001" """
        result = locale_manager.format_number(0.001)
        assert result == "0,001"

    def test_format_precision_truncation(self, locale_manager):
        """Teste: número com muitas casas decimais é truncado (6 casas)"""
        result = locale_manager.format_number(1.123456789)
        # Deve ter no máximo 6 casas decimais
        decimal_part = result.split(',')[1] if ',' in result else ""
        assert len(decimal_part) <= 6

    def test_format_trailing_zeros_removed(self, locale_manager):
        """Teste: zeros à direita são removidos"""
        result = locale_manager.format_number(123.40)
        assert result == "123,4"


class TestLocaleManagerCache:
    """Testes de cache de parsing."""

    def test_cache_stores_parsed_values(self, locale_manager):
        """Teste: valores parseados são armazenados em cache"""
        assert locale_manager.get_cache_size() == 0
        
        locale_manager.parse_number("123,45")
        assert locale_manager.get_cache_size() == 1

    def test_cache_reuses_values(self, locale_manager):
        """Teste: cache reutiliza valores parseados"""
        result1 = locale_manager.parse_number("123,45")
        initial_size = locale_manager.get_cache_size()
        
        result2 = locale_manager.parse_number("123,45")
        
        assert result1 == result2
        assert locale_manager.get_cache_size() == initial_size

    def test_cache_clear(self, locale_manager):
        """Teste: cache pode ser limpo"""
        locale_manager.parse_number("123,45")
        assert locale_manager.get_cache_size() > 0
        
        locale_manager.clear_cache()
        assert locale_manager.get_cache_size() == 0


class TestLocaleManagerIntegration:
    """Testes de integração parsing + formatação."""

    def test_round_trip_integer(self, locale_manager):
        """Teste: parsing e formatting preservam inteiros"""
        original = "1.234.567"
        parsed = locale_manager.parse_number(original)
        formatted = locale_manager.format_number(parsed)
        assert formatted == "1.234.567"

    def test_round_trip_decimal(self, locale_manager):
        """Teste: parsing e formatting preservam decimais"""
        original = "1.234,56"
        parsed = locale_manager.parse_number(original)
        formatted = locale_manager.format_number(parsed)
        assert formatted == original

    def test_parse_format_with_calculation(self, locale_manager):
        """Teste: parse → cálculo → format funciona corretamente"""
        # Parse "5,5" e "2,5"
        a = locale_manager.parse_number("5,5")
        b = locale_manager.parse_number("2,5")
        
        # Somar
        result = a + b
        
        # Formatar
        formatted = locale_manager.format_number(result)
        assert formatted == "8"
