"""
Testes unitários para a classe Calculator.

Cobre todas as operações matemáticas conforme histórias de usuário.
"""

import pytest
import sys
from pathlib import Path

# Adicionar src ao path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from calculator import Calculator


class TestCalculatorBasic:
    """Testes básicos de inicialização e estado."""

    def test_init(self):
        """Testa inicialização da calculadora."""
        calc = Calculator()
        assert calc.result == 0.0
        assert calc.get_operation_count() == 0

    def test_reset(self):
        """Testa reset da calculadora."""
        calc = Calculator()
        calc.result = 42.0
        calc.reset()
        assert calc.result == 0.0
        assert calc.get_operation_count() == 0


class TestCalculatorAddition:
    """Testes de adição (US01)."""

    def test_add_positive_numbers(self, calculator):
        """Teste: 5 + 3 = 8"""
        result = calculator.calculate(5, 3, '+')
        assert result == 8

    def test_add_zeros(self, calculator):
        """Teste: 0 + 0 = 0"""
        result = calculator.calculate(0, 0, '+')
        assert result == 0

    def test_add_negative_numbers(self, calculator):
        """Teste: -5 + 10 = 5"""
        result = calculator.calculate(-5, 10, '+')
        assert result == 5

    def test_add_decimal_numbers(self, calculator):
        """Teste: 12,5 + 7,5 = 20"""
        result = calculator.calculate(12.5, 7.5, '+')
        assert result == 20

    def test_add_precision(self, calculator):
        """Teste: 100 + 0,01 = 100,01"""
        result = calculator.calculate(100, 0.01, '+')
        assert abs(result - 100.01) < 0.000001


class TestCalculatorSubtraction:
    """Testes de subtração (US02)."""

    def test_subtract_positive_numbers(self, calculator):
        """Teste: 10 - 3 = 7"""
        result = calculator.calculate(10, 3, '-')
        assert result == 7

    def test_subtract_resulting_negative(self, calculator):
        """Teste: 3 - 10 = -7"""
        result = calculator.calculate(3, 10, '-')
        assert result == -7

    def test_subtract_zeros(self, calculator):
        """Teste: 0 - 0 = 0"""
        result = calculator.calculate(0, 0, '-')
        assert result == 0

    def test_subtract_decimal_numbers(self, calculator):
        """Teste: 10,5 - 5,5 = 5"""
        result = calculator.calculate(10.5, 5.5, '-')
        assert result == 5


class TestCalculatorMultiplication:
    """Testes de multiplicação (US03)."""

    def test_multiply_positive_numbers(self, calculator):
        """Teste: 5 × 3 = 15"""
        result = calculator.calculate(5, 3, '*')
        assert result == 15

    def test_multiply_by_zero(self, calculator):
        """Teste: 100 × 0 = 0"""
        result = calculator.calculate(100, 0, '*')
        assert result == 0

    def test_multiply_negative_numbers(self, calculator):
        """Teste: -5 × 3 = -15"""
        result = calculator.calculate(-5, 3, '*')
        assert result == -15

    def test_multiply_decimal_numbers(self, calculator):
        """Teste: 2,5 × 4 = 10"""
        result = calculator.calculate(2.5, 4, '*')
        assert result == 10


class TestCalculatorDivision:
    """Testes de divisão (US04)."""

    def test_divide_positive_numbers(self, calculator):
        """Teste: 10 ÷ 2 = 5"""
        result = calculator.calculate(10, 2, '/')
        assert result == 5

    def test_divide_resulting_decimal(self, calculator):
        """Teste: 10 ÷ 3 ≈ 3,333333 (6 casas)"""
        result = calculator.calculate(10, 3, '/')
        assert abs(result - 3.333333) < 0.000001

    def test_divide_negative_numbers(self, calculator):
        """Teste: -10 ÷ 2 = -5"""
        result = calculator.calculate(-10, 2, '/')
        assert result == -5

    def test_divide_decimal_numbers(self, calculator):
        """Teste: 7,5 ÷ 2,5 = 3"""
        result = calculator.calculate(7.5, 2.5, '/')
        assert result == 3


class TestCalculatorDivisionByZero:
    """Testes de validação de divisão por zero (US05)."""

    def test_divide_by_zero_error(self, calculator):
        """Teste: 10 ÷ 0 = Erro"""
        result = calculator.calculate(10, 0, '/')
        assert isinstance(result, str)
        assert "Divisão por zero" in result or "zero" in result.lower()

    def test_divide_zero_by_zero_error(self, calculator):
        """Teste: 0 ÷ 0 = Erro"""
        result = calculator.calculate(0, 0, '/')
        assert isinstance(result, str)


class TestCalculatorPrecision:
    """Testes de precisão (até 6 casas decimais)."""

    def test_precision_six_decimals(self, calculator):
        """Teste: resultado com 6 casas decimais"""
        result = calculator.calculate(1, 3, '/')
        # 1/3 = 0.333333... arredonda para 0.333333 (6 casas)
        assert result == 0.333333

    def test_precision_rounding(self, calculator):
        """Teste: arredondamento correto"""
        result = calculator.calculate(2, 3, '/')
        # 2/3 = 0.666666... arredonda para 0.666667 (6 casas)
        assert result == 0.666667


class TestCalculatorOperationCount:
    """Testes de contagem de operações."""

    def test_operation_count_increments(self, calculator):
        """Teste: contador de operações incrementa corretamente"""
        assert calculator.get_operation_count() == 0
        
        calculator.calculate(1, 1, '+')
        assert calculator.get_operation_count() == 1
        
        calculator.calculate(2, 2, '-')
        assert calculator.get_operation_count() == 2

    def test_reset_clears_operation_count(self, calculator):
        """Teste: reset limpa o contador de operações"""
        calculator.calculate(5, 3, '+')
        assert calculator.get_operation_count() == 1
        
        calculator.reset()
        assert calculator.get_operation_count() == 0


class TestCalculatorErrors:
    """Testes de tratamento de erros."""

    def test_invalid_operation(self, calculator):
        """Teste: operação inválida lança ValueError"""
        with pytest.raises(ValueError):
            calculator.calculate(5, 3, '%')

    def test_invalid_operation_in_calculate_returns_error(self, calculator):
        """Teste: operação inválida retorna mensagem de erro"""
        result = calculator.calculate(5, 3, '^')
        assert isinstance(result, str)
        assert "Erro" in result or "inválida" in result.lower()
